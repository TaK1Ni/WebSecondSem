from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user, AnonymousUserMixin
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from models import db, Course, Category, User, Review
from tools import CoursesFilter, ImageSaver, ReviewOrderer

bp = Blueprint('courses', __name__, url_prefix='/courses')

COURSE_PARAMS = [
    'author_id', 'name', 'category_id', 'short_desc', 'full_desc'
]


def params():
    return {p: request.form.get(p) or None for p in COURSE_PARAMS}


def search_params():
    return {
        'name': request.args.get('name'),
        'category_ids': [x for x in request.args.getlist('category_ids') if x],
    }


@bp.route('/')
def index():
    courses = CoursesFilter(**search_params()).perform()
    pagination = db.paginate(courses)
    courses = pagination.items
    categories = db.session.execute(db.select(Category)).scalars()
    return render_template('courses/index.html',
                           courses=courses,
                           categories=categories,
                           pagination=pagination,
                           search_params=search_params())


@bp.route('/new')
@login_required
def new():
    course = Course()
    categories = db.session.execute(db.select(Category)).scalars()
    users = db.session.execute(db.select(User)).scalars()
    return render_template('courses/new.html',
                           categories=categories,
                           users=users,
                           course=course)


@bp.route('/create', methods=['POST'])
@login_required
def create():
    f = request.files.get('background_img')
    img = None
    course = Course()
    try:
        if f and f.filename:
            img = ImageSaver(f).save()

        image_id = img.id if img else None
        course = Course(**params(), background_image_id=image_id)
        db.session.add(course)
        db.session.commit()
    except IntegrityError as err:
        flash(f'Возникла ошибка при записи данных в БД. Проверьте корректность введённых данных. ({err})', 'danger')
        db.session.rollback()
        categories = db.session.execute(db.select(Category)).scalars()
        users = db.session.execute(db.select(User)).scalars()
        return render_template('courses/new.html',
                               categories=categories,
                               users=users,
                               course=course)

    flash(f'Курс {course.name} был успешно добавлен!', 'success')

    return redirect(url_for('courses.index'))


@bp.route('/<int:course_id>')
def show(course_id):
    course = db.get_or_404(Course, course_id)
    review = None
    reviews = []
    count = 5
    try:
        query = db.select(Review).filter_by(course_id=course_id)
        if current_user.is_authenticated:
            review = db.session.execute(query.filter_by(user_id=current_user.id)).scalar()
            if review:
                count -= 1
                query = query.where(Review.user_id != current_user.id)
        reviews = db.session.execute(query.order_by(Review.created_at).limit(count)).scalars()
    except SQLAlchemyError as err:
        flash(f'Возникла ошибка при записи данных в БД. Проверьте корректность введённых данных. ({err})', 'danger')
    return render_template('courses/show.html', course=course, review=review, reviews=reviews)


@bp.route('/<int:course_id>', methods=['POST'])
@login_required
def add_review(course_id):
    text = request.form["reviewBody"]
    rating = int(request.form["rating"])
    try:
        review = Review(rating=rating, text=text, course_id=course_id, user_id=current_user.id)
        course = db.get_or_404(Course, course_id)
        course.rating_sum += rating
        course.rating_num += 1
        db.session.add(review)
        db.session.commit()
    except IntegrityError as err:
        flash(f'Возникла ошибка при записи данных в БД. Проверьте корректность введённых данных. ({err})', 'danger')
        db.session.rollback()
    return redirect(url_for('courses.show', course_id=course.id))


@bp.route('/<int:course_id>/reviews')
def reviews(course_id):
    review = None
    if current_user.is_authenticated:
        review = db.session.execute(db.select(Review).filter_by(course_id=course_id).filter_by(user_id=current_user.id)).scalar()
    params = {
        'order_by': request.args.get('order_by', 'date'),
        'direction': request.args.get('direction', 'desc'),
        'course_id': course_id,
    }
    reviews = ReviewOrderer(ignore=review.id if review else None, **params).perform()
    pagination = db.paginate(reviews, per_page=10)
    reviews = pagination.items
    return render_template('courses/reviews.html',
                           review=review,
                           reviews=reviews,
                           pagination=pagination,
                           search_params=params)

@bp.route('/<int:course_id>/reviews', methods=['POST'])
def filter(course_id):
    order_num = int(request.form["order"])
    params = {}
    if order_num == 0:
        params['order_by'] = "date"
        params['direction'] = 'desc'
    elif order_num == 1:
        params['order_by'] = "rating"
        params['direction'] = 'desc'
    elif order_num == 2:
        params['order_by'] = "rating"
        params['direction'] = 'asc'
    return redirect(url_for('courses.reviews', course_id=course_id, **params))

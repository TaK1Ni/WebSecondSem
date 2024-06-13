from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import db,Genre, GenreBook
from tools import BookFilter
from flask_login import login_required, current_user, AnonymousUserMixin
from models import Book
from tools import SkinSaver
from datetime import datetime

bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/new')
def new():
    genres = db.session.execute(db.select(Genre)).scalars()
    return render_template(
        'book/new.html',
        genres=genres
        )

@bp.route('/create', methods=['POST'])
@login_required
def create():    
    name = request.form['name']
    author = request.form['author']
    created_year = datetime.strptime(request.form['created'], '%Y')
    publish = request.form['publish']
    pages_count = int(request.form['pagescount'])
    short_desc = request.form['short_desc']
    genres = request.form.getlist('genre')
    background_img = request.files['background_img']

    skin_saver = SkinSaver(background_img)
    skin = skin_saver.save()

    book = Book(
        name=name,
        author=author,
        created_year=created_year,
        publish=publish,
        pages_count=pages_count,
        short_desc=short_desc,
        skin_id=skin.id
    )
    
    db.session.add(book)
    db.session.commit()
    return redirect(url_for('index'))

@bp.route('/show', methods=['POST'])
@login_required
def show():   
    return 0
import hashlib
import uuid
import os
from werkzeug.utils import secure_filename
from flask import current_app
from models import db, Skin, Book, GenreBook

class SkinSaver:
    def __init__(self, file):
        self.file = file

    def save(self):
        self.img = self.__find_by_md5_hash()
        if self.img is not None:
            return self.img
        filename = secure_filename(self.file.filename)

        self.img = Skin(
            id=str(uuid.uuid4()),
            filename=filename,
            mime_type=self.file.mimetype,
            md5_hash=self.md5_hash)
        
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        self.file.save(filepath)
        db.session.add(self.img)
        db.session.commit()
        return self.img

    def __find_by_md5_hash(self):
        self.md5_hash = hashlib.md5(self.file.read()).hexdigest()
        self.file.seek(0)
        return db.session.execute(db.select(Skin).filter(Skin.md5_hash == self.md5_hash)).scalar()
    def drop_skin(skin):
        os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'],skin))


class BookFilter:
    def __init__(self):
        self.bookquery = db.select(Book)
        self.genrequery = db.select(GenreBook)
    
    def find(self, name='', genres_search='', years_search='', kol_from='', kol_to='', author=''):
        if name != '':
            self.bookquery = self.bookquery.filter(Book.name.ilike(f'%{name}%'))
        
        if genres_search != '':
            self.genrequery = self.genrequery.filter(GenreBook.genre_id.in_(genres_search))

        if years_search != '':
            years_search = [int(i) for i in years_search]
            self.bookquery = self.bookquery.filter(Book.created_year.in_(years_search))
        
        if kol_from != '':
            self.bookquery = self.bookquery.filter(Book.pages_count >= int(kol_from))

        if kol_to != '':
            self.bookquery = self.bookquery.filter(Book.pages_count <= int(kol_to))
        
        if author != '':
            self.bookquery = self.bookquery.filter(Book.author.ilike(f'%{author}%'))
        
        return self.bookquery.order_by(Book.created_year.desc())
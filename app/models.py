from app import db


# Модель базыданных для книг
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    is_read = db.Column(db.Boolean, default = False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id',ondelete='SET NULL'))
    genre = db.relationship('Genre',back_populates = 'book')

    def __repr__(self):
        return '<Book name {}>'.format(self.name)


# Модель базыданных для жанров
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    # book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship('Book',back_populates = 'genre')

    def __repr__(self):
        return '<Genre {}>'.format(self.name)
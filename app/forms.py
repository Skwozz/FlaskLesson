# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import SubmitField,widgets, BooleanField,StringField,SelectMultipleField
from wtforms.validators import DataRequired,ValidationError
from app.models import Book,Genre


class AddBookForm(FlaskForm):
    name = StringField('Назавание книги',validators=[DataRequired()])
    genre = StringField('Назавание жанра',validators=[DataRequired()])
    is_read = BooleanField('Прочитано',validators=[DataRequired()])
    submit = SubmitField('Добавить книгу')

    def validate_book(self, name):
        book = Book.query.filter_by(name=name.data).first()
        if book is not None:
            raise ValidationError('Данная книга уже есть в базе данных')




class IsRead(FlaskForm):
    submit = SubmitField('Сохранить')
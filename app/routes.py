from flask import render_template,redirect,request,url_for
from app import app, db
from app.models import Book,Genre
from app.forms import AddBookForm,IsRead
# Главная страница сайта с книгами,где есть форма для сохранения и html-бокс
# с галочкой, которую я не могу привязать к тому,чтобы при её нажатии и сохранении,
# изменяла значение is_read с FALSE НА TRUE
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    name_book = Book.query.all()
    genre_name = Genre.query.all()
    form = IsRead()

    if request.method == 'POST':
    #     value1 = request.form.get('n.name')
    #     value = request.form.getlist('Прочитано')
        # if value[0] == 'yes':
        #
        #     name_book.is_read = True
        #     db.session.commit()
        # print(value1,value)
        return redirect(url_for('index'))
    return render_template('index.html',name_book=name_book,genre_name=genre_name,form=form)


# Страница отвечает за вывод всех книг из определённого жанра, если перейти по ссылке
@app.route('/genre/<int:genre_id>')
def genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return render_template('genre.html',
                           genre_name = genre.name,
                           book_name = genre.book)

# @app.route('/add_book', methods=['GET', 'POST'])
# def add_book():
#     form = AddBookForm()
#
#     if form.validate_on_submit():
#         book = Book(name=form.name.data,is_read=form.is_read.data)
#         db.session.add(book)
#         db.session.commit()
#         genre = Genre(name=form.name.data)
#         db.session.add(genre)
#         db.session.commit()
#         return redirect('/index')
#
#     return render_template('add_book.html',title='Добавить книгу', form=form)
#















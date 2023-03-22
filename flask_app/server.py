from flask import Flask, request, render_template, make_response, redirect, url_for
from flask_restful import Resource, Api
import sqlitedb
import add_some_in_db

app = Flask(__name__)
api = Api(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/addall')
def addall():
    add_some_in_db.add_some_in_db()
    return render_template('index.html')


@app.route('/info')
def info():
    db_table = sqlitedb.read()
    headers = {'Content-Type': 'text/html'}
    return make_response(render_template('info.html', db=db_table), 200, headers)


@app.route('/delete/<int:id>')
def del_book(id):
    sqlitedb.delete(id)
    return redirect(url_for('books'))


class EditBooks(Resource):
    headers = {'Content-Type': 'text/html'}

    def get(self, id):
        data = sqlitedb.read(id)[0]
        print(data)
        return make_response(render_template('edit.html', data=data), 200, EditBooks.headers)

    def post(self, id):
        book = request.form['book']
        author = request.form['author']
        annotation = request.form['annotation']
        count = request.form['count']
        price = request.form['price']
        sqlitedb.update(id, book, author, count, price, annotation)
        return redirect(url_for('books'))


class GetPostBooks(Resource):
    headers = {'Content-Type': 'text/html'}

    def get(self):
        return make_response(render_template('create.html'), 200, GetPostBooks.headers)

    def post(self):
        book = request.form['book']
        author = request.form['author']
        annotation = request.form['annotation']
        count = request.form['count']
        price = request.form['price']
        sqlitedb.create(book, author, count, price, annotation)
        return redirect(url_for('books'))


class Books(Resource):

    def get(self):
        db_table = sqlitedb.read()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('dbfull.html', db=db_table), 200, headers)

    def post(self):
        return redirect(url_for('edit'))


api.add_resource(Books, '/books')
api.add_resource(GetPostBooks, '/editbooks')
api.add_resource(EditBooks, '/edit/<int:id>')
sqlitedb.create_table()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=9999)

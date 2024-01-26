from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    publicationyear = db.Column(db.Integer,primary_key=True)

def create_db():
    with app.app_context():
        db.create_all()


@app.route('/books', methods= ['GET'])
def index():
    users = User.query.all()
    return render_template('books.html', users=users)

@app.route('/add_book', methods=['GET','POST'])
def add_user():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publicationyear = request.form['publicationyear']


        new_user = User(title=title, author=author,publicationyear=publicationyear)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_book.html', title= 'Add a book')

if __name__ == '__main__':
    create_db()
    app.run(port=5000,debug=True)
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80)) 
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f'{self.book_name - self.author - self.publisher}'
    
    def make_book():
        book_name1 = input("Enter book name")
        author1 = input("Enter aithor")
        publisher1 = input("Enter publisher")
        book = Book(book_name= book_name1, author=author1, publisher=publisher1)

        # Add the book to the session
        db.session.add(book)

        # Commit the session to save to the database
        db.session.commit()


print("Current Working Directory:", os.getcwd())

with app.app_context():
    db.create_all()
    print("Database tables created!")

    Book.make_book()

@app.route('/')
def index():
    return "hello"  



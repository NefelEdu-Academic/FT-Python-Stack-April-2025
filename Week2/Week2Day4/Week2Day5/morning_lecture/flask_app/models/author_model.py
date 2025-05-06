from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask_app.models import book_model

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.author_name = data['author_name']
        self.style = data['style']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.my_books = []
        
    @classmethod
    def author_create(cls, data):
        query =""" INSERT INTO authors (author_name, style)
                VALUES (%(author_name)s, %(style)s);"""
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(DB).query_db(query)
        all_authors=[]
        for dict in results:
            author = cls(dict)
            all_authors.append(author)
        return all_authors
    
    @classmethod
    def get_one_by_id_with_books(cls, data):
        query = """SELECT * FROM authors 
                    LEFT JOIN books ON books.author_id=authors.id
                    where authors.id = %(id)s;"""
                    
        results = connectToMySQL(DB).query_db(query, data)
        this_author = cls(results[0])
        for row in results:
            book_data={
                **row,
                "id": row["books.id"],
                "created_at": row["books.created_at"],
                "updated_at": row["books.updated_at"]
            }
            book= book_model.Book(book_data)
            this_author.my_books.append(book)
        return this_author
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.book_name = data['book_name']
        self.nb_of_pages = data['nb_of_pages']
        self.book_type = data['book_type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.author_id = data['author_id']
        
    
    @classmethod
    def create(cls, data):
        query = """INSERT INTO books (book_name, nb_of_pages, book_type, author_id)
                VALUES (%(book_name)s, %(nb_of_pages)s, %(book_type)s, %(author_id)s);
        """
        return connectToMySQL(DB).query_db(query, data)
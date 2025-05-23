from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash # type: ignore 
from flask_app import DB
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    
    @classmethod
    def register(cls, data):
        query= """INSERT INTO users (first_name, last_name, email, password)
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        # insert query return the id of the created object
        return connectToMySQL(DB).query_db(query, data)
    
    
    @classmethod
    def get_by_email(cls, data):
        query="SELECT * FROM users WHERE email = %(email)s;"
        result =connectToMySQL(DB).query_db(query, data)
        if result:
            return cls(result[0])
        return False
    
    @classmethod
    def get_by_id(cls, data):
        query= "SELECT * FROM users WHERE id =%(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        if result:
            return cls(result[0])
        return False
    
    @staticmethod
    def validate_user(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", "email")
            is_valid = False 
        elif User.get_by_email({'email': data['email']}):
            flash("Email already taken", "email")
            is_valid = False
        if len(data['password'])<8:
            flash("Password must contain at least 8 characters!", "password")
            is_valid=False
        elif data['password'] != data['confirm_password']:
            flash("Passwordd and Confirm password doen't match", "confirm_password")
            is_valid= False
        if len(data["first_name"])<2:
            flash("First Name must contain at least 2 charaters", "first_name")
            is_valid=False
        if len(data["last_name"])<2:
            flash("Last Name must contain at least 2 charaters", "last_name")
            is_valid=False
        return is_valid
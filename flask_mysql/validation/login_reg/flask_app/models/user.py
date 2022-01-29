from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    database = "login_reg_schema"

    def __init__(self, data):
        self.id = data['id']

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw_hash = data['pw_hash']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(form_data):
        is_valid = True

        # First Name - letters only(regex?), at least 2 characters, not empty
        if form_data['first_name'] == '':
            flash("Must submit a first name.")
            is_valid = False
        elif len(form_data['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if not form_data['last_name'].isalpha():
            flash("Last name must only consist of letters")
            is_valid = False

        # Last Name - letters only(regex?), at least 2 characters, not empty
        if form_data['last_name'] == '':
            flash("Must submit a last name.")
            is_valid = False
        elif len(form_data['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if not form_data['last_name'].isalpha():
            flash("Last name must only consist of letters")
            is_valid = False

        # Email - Valid Email Format(regex), does not already exist in db, not empty
        if form_data['email'] == '':
            flash('Must submit an email address.')
            is_valid = False
        elif not EMAIL_REGEX.match(form_data['email']):
            flash('Email must be in proper format (ex. name@email.com).')
            is_valid = False

        # Password - at least 8 characters, not empty
        if form_data['password'] == '':
            flash('Must submit a password.')
            is_valid = False
        elif len(form_data['password']) < 8:
            flash('Password must be at least 8 characters.')
            is_valid = False

        # Password Confirm - must match password
        if form_data['pw_confirm'] != form_data['password']:
            flash('Password confirmation must match password.')
            is_valid = False


        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True

        user_in_db = User.get_user_by_email(data)

        # check to see if user exists in database
        if not user_in_db:
            flash('Invalid credentials')
            is_valid = False

        # Check if login password matches password in database
        elif not bcrypt.check_password_hash(user_in_db.pw_hash, data['password']):
            flash('Invalid credentials')
            is_valid = False

        return is_valid

    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at)
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(pw_hash)s, NOW(), NOW())
        """

        results = connectToMySQL(cls.database).query_db(query, data)
        return results

    @classmethod
    def get_user_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"

        result = connectToMySQL(cls.database).query_db(query, data)

        # if user not found in database
        if len(result) < 1:
            return False

        return cls(result[0])

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"

        result = connectToMySQL(cls.database).query_db(query, data)

        # if user not found in database
        if len(result) < 1:
            return False

        return cls(result[0])
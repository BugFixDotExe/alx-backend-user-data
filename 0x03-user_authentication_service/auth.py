#!/usr/bin/env python3
"""
A module that
 returned bytes is a salted hash of the input password,
 hashed with bcrypt.hashpw.
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
        register_user: a method that saves a user to db
        Args:
            email(str): a vaid email
            password: a regular str password
        Returns:
            A User object saved to the db
        '''
        try:
            auth_session = self._db._session
            isUser = self._db.find_user_by(email=email)
            if isUser:
                raise ValueError(f'User {email} already exists')
        except (NoResultFound):
            hashed_password = _hash_password(password)
            saved_user = self._db.add_user(
                email=email, hashed_password=hashed_password)
            return saved_user


def _hash_password(password: str) -> bytes:
    '''
    _hash_password: a function that returns a hashed pass
    Args:
        password(string): the string to be hashed
    Returns:
        A byte repr of password
    '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

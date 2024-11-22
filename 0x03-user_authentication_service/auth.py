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
import uuid


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
        if password is None or len(password) == 0:
            raise ValueError
        if email is None or len(email) == 0:
            raise ValueError
        try:
            self._db._session
            isUser = self._db.find_user_by(email=email)
            if isUser:
                raise ValueError(f'User {email} already exists')
            else:
                raise NoResultFound
        except (NoResultFound):
            hashed_password = _hash_password(password)
            saved_user = self._db.add_user(
                email=email, hashed_password=hashed_password)
            return saved_user

    def valid_login(self, email: str, password: str) -> bool:
        '''
        valid_login: A method that returns a boolean
        it serves the purpose of checking a password againt
        it's hashed variant, using an email as the query
        Args:
            email(string): An email to be used for filtering
            password(string): A non hased password
        Returns:
            A boolean True for match and Flase otherwise
        '''
        try:
            is_user = self._db.find_user_by(email=email)
            status = bcrypt.checkpw(
                password=password.encode('utf-8'),
                hashed_password=is_user.hashed_password)
            return status
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        '''
        create_session: A method. It takes an
        email string argument and returns
        the session ID as a string.
        Args:
            email: an email to query with
        Returns:
            a uuid of the user
        '''
        try:
            is_user = self._db.find_user_by(email=email)
            if is_user:
                session_id = _generate_uuid()
                self._db.update_user(is_user.id, session_id=session_id)
                return session_id
        except NoResultFound:
            return 'None'


def _hash_password(password: str) -> bytes:
    '''
    _hash_password: a function that returns a hashed pass
    Args:
        password(string): the string to be hashed
    Returns:
        A byte repr of password
    '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    '''
    _generate_uuid: generate a str uuid
    Returns:
        A string repr of uuid4
    '''
    return str(uuid.uuid4())

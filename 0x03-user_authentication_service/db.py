#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        '''
        add_user: A method that adds a user to the db
            Args:
                email: an email
                hashed_password: a hashed string
            Returns:
                A type of User
            '''
        if self.__session is None:
            self.__session = self._session
        new_user = User(email=email, hashed_password=hashed_password)
        self.__session.add(new_user)
        self.__session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
            Finds a user by the provided filter criteria.

            Args:
                email (str, optional): The email of the user to find.
                Defaults to None.
                hashed_password (str, optional): The hashed password
                of the user to find.
                Defaults to None.

            Returns:
                User: The User object if found.

            Raises:
                ValueError: If no filter criteria are provided.
                NoResultFound: If no user matches the criteria.
            """
        if self.__session is None:
            self.__session = self._session
        query = None
        for key, value in kwargs.items():
            if not hasattr(User, key):
                raise InvalidRequestError
            if key == 'email':
                query = self.__session.query(User).filter(
                    getattr(User, key) == value)

        if query:
            try:
                return query.one()
            except NoResultFound:
                raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """
            Finds a user by the provided filter criteria.

            Args:
                user_id (int): The id of the user to find.
               kwargs (dict): A dict containing the attr(key)
               and value to be update in the User class

            Returns:
                None

            Raises:
                ValueError: If no or wrong filter criteria are provided.
            """
        if self.__session is None:
            self.__session = self._session
        if type(user_id) is not int:
            raise ValueError
        if not kwargs:
            raise ValueError
        try:
            matched_user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                try:
                    if hasattr(matched_user, key):
                        setattr(matched_user, key, value)
                except (AttributeError, TypeError):
                    raise ValueError
            self.__session.commit()
        except (NoResultFound):
            raise NoResultFound

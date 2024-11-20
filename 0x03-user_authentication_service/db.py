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
        self._engine = create_engine("sqlite:///a.db", echo=True)
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
        session = self._session
        new_user = User(email=email, hashed_password=hashed_password)
        session.add(new_user)
        session.commit()
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
        try:
            session = self._session
            if kwargs:
                for key, value in kwargs.items():
                    query = session.query(User).filter(
                        getattr(User, key) == value)
                if (query.first() is None):
                    raise NoResultFound
                return query.first()
        except(AttributeError):
            raise InvalidRequestError

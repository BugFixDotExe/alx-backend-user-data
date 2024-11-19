"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import (
    ArgumentError, InvalidRequestError,
    NoReferenceError, NoResultFound)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

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

    def find_user_by(self, email: str) -> User:
        '''
        find_user_by: A function that queries for a user
        Args:
            email: the email of the user to query for
        Returns:
            A type User if found
            or raises NoResultFound
            and if  input is invalid an InvalidRequestError
            is raised
        '''
        session = self._session
        try:
            return session.query(User).filter_by(email=email).one()
        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError

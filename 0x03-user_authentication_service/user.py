#!/usr/bin/env python3
'''
A model for the User database
'''
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class User(Base):
    '''
    User: A class that defines the schema using OOP for the User Table
    Args:
        Base: A required type when dealing wiht SQLAlchemy
        id: an int type for representing user ID
        email: a str for user email
        hased_password: a str for user password
        session_id: a string for session id
        reset_token: a str for reset token
    Returns: None
    '''
    '''
    __tablename__ is users
    '''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

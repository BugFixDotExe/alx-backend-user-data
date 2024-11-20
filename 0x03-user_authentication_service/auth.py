#!/usr/bin/env python3
"""
A module that
 returned bytes is a salted hash of the input password,
 hashed with bcrypt.hashpw.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    '''
    _hash_password: a function that returns a hashed pass
    Args:
        password(string): the string to be hashed
    Returns:
        A byte repr of password
    '''
    password_as_bytes = password.encode('utf-8')
    salted_password = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_as_bytes, salted_password)
    return hashed_password

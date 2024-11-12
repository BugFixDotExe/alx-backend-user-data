#!/usr/bin/env python3
"""
A class for managing the API Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    '''
    Auth: A class for verfiying API authenctication
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        require_auth: A function that checks auth
        Args:
            path: the url
            excluded_paths: a list of exclusive path
        Returns:
            A boolen for approved or disapproved access
        '''
        return False

    def authorization_header(self, request=None) -> str:
        '''
        authorization_header: a header checker
        Args:
            request object
        Returns:
            A str
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        current_user: A function for checking the user
        Args:
            a request object
        Returns:
            TypeVar of the Class type User
        '''
        return None

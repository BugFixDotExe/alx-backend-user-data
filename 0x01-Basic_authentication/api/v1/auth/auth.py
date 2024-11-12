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
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        for single_path in excluded_paths:
            if path == single_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        '''
        authorization_header: a header checker
        Args:
            request object
        Returns:
            A str
        '''
        if request is None:
            return None
        if request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        current_user: A function for checking the user
        Args:
            a request object
        Returns:
            TypeVar of the Class type User
        '''
        return None

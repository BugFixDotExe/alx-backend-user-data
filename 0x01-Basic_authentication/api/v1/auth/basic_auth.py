#!/usr/bin/env python3
"""
A class for managing the API Authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''
    BasicAuth a class that inheris from the Auth class
    '''
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        '''
        extract_base_64: a function that returns the
        Base64 part of the Authorization
        header for a Basic Authentication
        Args:
            authorization_header: A header having the Authorization field
        Returns:
            A string of base64, after converting the authroiation_header
        '''
        if authorization_header is None:
            return None
        if issubclass(type(authorization_header), str) is False:
            return None
        split_header = authorization_header.split()
        if len(split_header) <= 1:
            return None
        if "Basic" not in split_header[0]:
            return None
        return split_header[1]

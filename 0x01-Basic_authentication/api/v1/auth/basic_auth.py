#!/usr/bin/env python3
"""
A class for managing the API Authentication
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        '''
        decode_base64_authorization_header: a function that returns the
        Base64 part of the Authorization decoded
        Args:
            authorization_header: A header having the Authorization value
        Returns:
            A decoded string of base64
        '''
        if base64_authorization_header is None:
            return None
        if issubclass(type(base64_authorization_header), str) is False:
            return None
        try:
            isValid = base64.b64decode(
                base64_authorization_header,
                validate=True)
            return isValid.decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        '''
        extract_user_credentials: a function that returns the
        username and string part of the Authorization
        Args:
            authorization_header: A header having the Authorization value
        Returns:
            A tuple containing the username and password
        '''

        if decoded_base64_authorization_header is None:
            return (None, None)
        if issubclass(type(decoded_base64_authorization_header), str) is False:
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        username, password = decoded_base64_authorization_header.split(":")
        return (username, password)

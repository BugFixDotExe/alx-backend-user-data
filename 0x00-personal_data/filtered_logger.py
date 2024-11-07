#!/usr/bin/env python3
'''
A module that contains the function
filter_datum that reuturns the log message
obsfuscated.
'''
from typing import List
import re


def filter_datum(
                fields: List[str],
                redaction: str,
                message: str,
                separator: str):
    '''
        filter_datum: a function that returns a new string with
        it's to be redacted part, redacted
        Args:
            fields: A list of fields to look out for in the sting
            redaction: The readaction to be applied
            message: The message to look into
            separtor: what should be used to end the redacted string
        Returns:
            A string with the redaction take
    '''
    pattern = fr'({fields}=)([^;]*?);'
    matched = re.sub(pattern, fr'\1{redaction}{separator}', message)
    return matched

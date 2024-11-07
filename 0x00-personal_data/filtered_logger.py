#!/usr/bin/env python3
'''
A module that contains the function
filter_datum that reuturns the log message
obsfuscated.
'''
from typing import List
import re
import logging


def filter_datum(fields: List[str],redaction: str,message: str,separator: str):
    for field in fields:
        message = re.sub(fr'({field}=)([^;]*?);', fr'\1{redaction}{separator}', message)
    return message

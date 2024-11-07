#!/usr/bin/env python3
'''
A module that contains the function
filter_datum that reuturns the log message
obsfuscated.
'''
from typing import List
import re
import logging


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    return re.sub(rf"({'|'.join(fields)})=([^;]*)", lambda m: f"{m.group(1)}={redaction}", message)

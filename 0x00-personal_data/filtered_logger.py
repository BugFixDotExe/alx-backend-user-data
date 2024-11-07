#!/usr/bin/env python3
'''
A module that contains the function
filter_datum that reuturns the log message
obsfuscated.
'''
from typing import List
import re
import logging

import re


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    return re.sub(
        r"({})=(.*?)(?={})".format("|".join(fields), separator),
        r"\1={}".format(redaction), message)

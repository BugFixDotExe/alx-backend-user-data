import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    pattern = fr"({'|'.join(fields)})=([^;]*?);"
    return re.sub(pattern, fr"\1{redaction};", message)

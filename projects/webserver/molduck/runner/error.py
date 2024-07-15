from enum import Enum


class ErrorType(Enum):
    BASIS_NOT_FOUND = "BASIS_NOT_FOUND"
    KEYWORD_NOT_FOUND = "KEYWORD_NOT_FOUND"
    METHOD_NOT_FOUND = "METHOD_NOT_FOUND"


class Error:
    error_type: ErrorType
    error_message: str

    def __init__(self, error_type: ErrorType, error_message: str):
        self.error_type = error_type
        self.error_message = error_message

import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Extracts and formats the error message from an exception.
    
    Args:
        error (Exception): The exception object.
        error_detail (sys): The sys module to extract the traceback information.

    Returns:
        str: A formatted string containing the error message and details.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with message: [{str(error)}]"
    return error_message 


class CustomException(Exception):
    """
    Custom exception class that formats error messages for exceptions.

    Args:
        error (Exception): The exception object.
        error_detail (sys): The sys module to extract the traceback information.
    """
    def __init__(self, error, error_detail: sys):
        super().__init__(error)
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        return self.error_message
    


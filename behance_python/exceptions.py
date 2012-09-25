
#   TODO: Create exception classes for each error code

class BehanceException(Exception):
    """Base exception.
    
    Has two attributes:
        self.error_code: HTTP error code as returned by Behance API
        self.msg: message to be printed referencing error code."""
    def __init__(self, error_code):
        self.error_code = error_code
        self.msg = "Behance API threw a %s error." % error_code
    def __str__(self):
        return repr(self.msg)

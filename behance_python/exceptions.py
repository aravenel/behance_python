EXCEPTIONMAPPING = {
        403: 'Forbidden',
        404: 'NotFound',
        429: 'TooManyRequests',
        500: 'InternalServerError',
        503: 'ServiceUnavailable',
        }

class BehanceException(Exception):
    """Base exception.
    
    Has two attributes:
        self.error_code: HTTP error code as returned by Behance API
        self.msg: message to be printed referencing error code."""
    def __init__(self, error_code=None):
        self.error_code = error_code
        if self.error_code:
            self.msg = "Behance API threw a %s error." % error_code
        else:
            self.msg = "Behance API had an unknown error."
    def __str__(self):
        return repr(self.msg)

class Forbidden(BehanceException):
    pass

class NotFound(BehanceException):
    pass

class TooManyRequests(BehanceException):
    pass

class InternalServerError(BehanceException):
    pass

class ServiceUnavailable(BehanceException):
    pass

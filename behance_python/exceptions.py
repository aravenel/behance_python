class BehanceException(Exception):
    """Base exception for inheriting"""
    def __init__(self, error_code):
        self.msg = "Behance API threw a %s error." % error_code

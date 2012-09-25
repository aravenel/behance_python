import requests
import exceptions
from requests.exceptions import ConnectionError, HTTPError, Timeout, TooManyRedirects

class Behance:
    """Base class to be inherited by other Behance classes (project, user, WIP,
    collection). Implements API calling and error handling."""

    def __init__(self, auth_key):
        self.auth_key = auth_key

    def _add_property(self, name, value):
        """Helper function to dynamically add all the JSON data from API response
        to the Project object."""
        setattr(self.__class__, name, value)

    def _get_api_data(self, url):
        """Internal helper to call API and handle exceptions"""
        try:
            _results = requests.get(url)

            if _results.status_code == 200:
                return _results.json
            else:
                #raise BehanceException(_results.status_code)
                #Throw the error corresponding to the correct error code.
                #If unknown error code, throw generic error.
                n = _results.status_code
                try:
                    raise getattr(exceptions, exceptions.EXCEPTIONMAPPING[n])(n)
                except AttributeError:
                    raise exceptions.BehanceException(n)
        except (ConnectionError, HTTPError, Timeout, TooManyRedirects) as e:
            #If requests raises and exception
            raise e

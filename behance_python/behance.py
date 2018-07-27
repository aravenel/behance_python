import requests
import behance_python.exceptions
from requests.exceptions import ConnectionError, HTTPError, Timeout, TooManyRedirects

class Behance(dict):
    """Base class to be inherited by other Behance classes (project, user, WIP,
    collection). Implements API calling and error handling."""

    def __init__(self, auth_key=None, data=None):
        if auth_key:
            self.auth_key = auth_key
        if data:
            self.set_data(data)

    def _add_property(self, name, value):
        """Helper function to dynamically add all the JSON data from API response
        to the Project object."""
        setattr(self.__class__, name, value)

    def _convert_int(self, value):
        """Handle JSON integer keys stored as strings"""
        try:
            return int(value)
        except ValueError:
            return value

    def _parse_data(self, data):
        """Recursively process data to allow object notation"""
        if isinstance(data, dict):
            new_data = Behance(data=data)
        elif isinstance(data, list):
            new_data = [self._parse_data(item) for item in data]
        else:
            new_data = data

        return new_data

    def _get_api_data(self, url):
        """Internal helper to call API and handle exceptions"""
        try:
            _results = requests.get(url)

            if _results.status_code == 200:
                return _results.json()
            else:
                #Throw the error corresponding to the correct error code.
                #If unknown error code, throw generic error.
                n = _results.status_code
                try:
                    raise getattr(behance_python.exceptions, behance_python.exceptions.EXCEPTIONMAPPING[n])(n)
                except AttributeError:
                    raise behance_python.exceptions.BehanceException(n)
        except (ConnectionError, HTTPError, Timeout, TooManyRedirects) as e:
            #If requests raises an exception
            raise e

    def set_data(self, data):
        """Set data after parsing."""
        if isinstance(data, dict):
            for k, v in data.items():
                new_k = self._convert_int(k)
                new_v = self._parse_data(v)
                self.__setattr__(new_k, new_v)
        else:
            raise TypeError('Expected a dict')

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

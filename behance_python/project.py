import requests
from behance_python import ENDPOINTS, url_join
from exceptions import BehanceException
from requests.exceptions import ConnectionError, HTTPError, Timeout, TooManyRedirects

class Project:
    """Class representing a Behance project.API_ENDPOINT
    
    When instantiated, will call API. Instance will have attributes with names
    and values equal to JSON key/values returned from API.
    """

    def __init__(self, project_id, auth_key):
        self.project_id = project_id
        self.auth_key = auth_key

        #Call behance API and populate data
        self._get_project_details()

    def _add_property(self, name, value):
        """Helper function to dynamically add all the JSON data from API response
        to the Project object."""
        setattr(self.__class__, name, value)

    def _get_project_details(self):
        """Internal function to call Behance API and parse data."""
        try:
            #Build the URL
            _url = url_join(ENDPOINTS['api'], ENDPOINTS['project'], 
                    str(self.project_id))
            _url = "%s?api_key=%s" % (_url, self.auth_key)
            #Call the API
            _results = requests.get(_url)

            #Parse the data
            if _results.status_code == 200:
                _project_data = _results.json['project']
                for k, v in _project_data.items():
                    self._add_property(k, v)
            else:
                #If error from API, raise exception
                raise BehanceException(_results.status_code)
        except (ConnectionError, HTTPError, Timeout, TooManyRedirects) as e:
            #If requests raises and exception
            raise e

    def get_comments(self):
        """Gets the comments for the project. Returns list of dicts."""
        try:
            _url = url_join(ENDPOINTS['api'], ENDPOINTS['project'], 
                    str(self.project_id), 'comments')
            _url = "%s?api_key=%s" % (_url, self.auth_key)
            _results = requests.get(_url)
            if _results.status_code == 200:
                return _results.json['comments']
            else:
                raise BehanceException(_results.status_code)
        except (ConnectionError, HTTPError, Timeout, TooManyRedirects) as e:
            #If requests raises an exception
            raise e


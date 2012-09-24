import requests
import exceptions
from behance_python import *
from requests.exceptions import ConnectionError, HTTPError, Timeout, TooManyRedirects

class Project:
    """Class representing a Behance project."""

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
            _url = '/'.join(s.strip('/') for s in [API_ENDPOINT, PROJECT_ENDPOINT, self.project_id])
            _url = "%s?api_key=%s" % (_url, self.auth_key)
            _results = requests.get(_url)
        except (ConnectionError, HTTPError, Timeout, TooManyRedirects), e:
            raise e

        if _results.status_code == 200:
            project_data = _results.json['project']
            self.project_data = project_data
            for k, v in project_data.items():
                self._add_property(k, v)
        else:
            raise exceptions.BehanceException(_results.status_code)

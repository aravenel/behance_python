from behance_python.behance import Behance
from behance_python import ENDPOINTS, url_join

class Project(Behance):
    """Class representing a Behance project.API_ENDPOINT
    
    When instantiated, will call API. Instance will have attributes with names
    and values equal to JSON key/values returned from API.
    """

    def __init__(self, project_id, auth_key):
        Behance.__init__(self, auth_key)
        self.project_id = project_id
        self.base_url = url_join(ENDPOINTS['api'], ENDPOINTS['project'])

        #Call behance API and populate data
        self._get_project_details()

    def _get_project_details(self):
        """Internal function to call Behance API and parse data."""
        #Build the URL
        _url = url_join(self.base_url, str(self.project_id))
        _url = "%s?api_key=%s" % (_url, self.auth_key)
        #Call the API
        _results = self._get_api_data(_url)['project']
        self.set_data(_results)

    def get_comments(self):
        """Returns comments for a project as an attribute. If called more than
        once, will store the value to prevent repeatedly calling the API."""
        _url = url_join(self.base_url, str(self.project_id), 'comments')
        _url = "%s?api_key=%s" % (_url, self.auth_key)
        return self._parse_data(self._get_api_data(_url)['comments'])

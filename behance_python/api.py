import requests
from behance_python import ENDPOINTS, url_join
from project import Project
from exceptions import BehanceException
from requests.exceptions import ConnectionError, HTTPError, Timeout, TooManyRedirects

class API:
    """Base wrapper for the Behance api.
    
    Must be instantiated using your provided auth key."""

    def __init__(self, auth_key):
        self.auth_key = auth_key

    def get_project(self, project_id):
        """Query behance API and return Project instance"""
        return Project(project_id, self.auth_key)

    def project_search(self, *args, **kwargs):
        """Search for projects on Behance. 
        Takes list of plain text search terms, as well as key/value filters.

        Valid filters: [valid values]
            sort: [featured_date, appreciations, views, comments, published_date]
            time: [all, today, week, month]
            field: [URL-encoded field name from Behance list of defined creative fields]
            country: [2-letter FIPS country code]
            state: [State or province name]
            page: [page number of results, 1-indexed]
            tags: [single tag name or pipe separated list of tags]
        """
        try:
            if len(args) == 0:
                #Make sure user provides search terms...
                raise BehanceException(000)

            #Build the URL
            _base_url = url_join(ENDPOINTS['api'], ENDPOINTS['project'])
            _terms = "+".join(arg for arg in args)
            _filters = "&".join("%s=%s" % (k, v) for k, v in kwargs.items())
            _url = '%s?api_key=%s&q=%s&%s' % (_base_url, self.auth_key, _terms, _filters)

            #Get results from API
            _results = requests.get(_url)

            #Parse results
            if _results.status_code == 200:
                return _results.json['projects']
            else:
                raise BehanceException(_results.status_code)
        except (ConnectionError, HTTPError, Timeout, TooManyRedirects) as e:
            raise e

import urllib
import requests
from behance_python import ENDPOINTS, url_join
from behance_python.project import Project
from behance_python.user import User
from behance_python.wip import WIP
from behance_python.collection import Collection
from behance_python.behance import Behance
import behance_python.exceptions
from requests.exceptions import ConnectionError, HTTPError, Timeout, TooManyRedirects

class API:
    """Base wrapper for the Behance api.
    
    Must be instantiated using your provided auth key."""

    def __init__(self, auth_key):
        self.auth_key = auth_key

    def _do_api_search(self, url):
        try:
            #Get results from API
            _results = requests.get(url)

            #Parse results
            if _results.status_code == 200:
                return _results.json()
            else:
                n = _results.status_code
                try:
                    raise getattr(behance_python.exceptions, behance_python.exceptions.EXCEPTIONMAPPING[n])(n)
                except AttributeError:
                    raise behance_python.exceptions.BehanceException(n)
        except (ConnectionError, HTTPError, Timeout, TooManyRedirects) as e:
            raise e


    def get_project(self, project_id):
        """Query behance API and return Project instance"""
        return Project(project_id, self.auth_key)

    def project_search(self, *args, **kwargs):
        """Search for projects on Behance. 
        Takes any number of text search terms, as well as key/value filters.

        Valid filters: [valid values]
            sort: [featured_date, appreciations, views, comments, published_date]
            time: [all, today, week, month]
            field: [URL-encoded field name from Behance list of defined creative fields]
            country: [2-letter FIPS country code]
            state: [State or province name]
            page: [page number of results, 1-indexed]
            tags: [single tag name or pipe separated list of tags]
        """
        if len(args) == 0:
            #Make sure user provides search terms...
            return None
        else:
            #Build the URL
            _base_url = url_join(ENDPOINTS['api'], ENDPOINTS['project'])
            _terms = "+".join(urllib.parse.quote(arg) for arg in args)
            _filters = urllib.parse.urlencode(kwargs)
            _url = '%s?api_key=%s&q=%s&%s' % (_base_url, self.auth_key, _terms, _filters)

            #Get results from API
            return [Behance(data=proj) for proj in self._do_api_search(_url)['projects']]

    def user_search(self, *args, **kwargs):
        """Search for users on Behance.
        Takes any number of text search terms, as well as key/value filters
        as supported by Behance API."""
        if len(args) == 0:
            return None
        else:
            _base_url = url_join(ENDPOINTS['api'], ENDPOINTS['user'])
            _terms = "+".join(urllib.parse.quote(arg) for arg in args)
            _filters = urllib.parse.urlencode(kwargs)
            _url = '%s?api_key=%s&q=%s&%s' % (_base_url, self.auth_key, _terms, _filters)

            #Get results from API
            return [Behance(data=user) for user  in self._do_api_search(_url)['users']]

    def get_user(self, user_id):
        return User(user_id, self.auth_key)

    def wip_search(self, *args, **kwargs):
        if len(args) == 0:
            return None
        else:
            _base_url = url_join(ENDPOINTS['api'], ENDPOINTS['wip'])
            _terms = "+".join(urllib.parse.quote(arg) for arg in args)
            _filters = urllib.parse.urlencode(kwargs)
            _url = '%s?api_key=%s&q=%s&%s' % (_base_url, self.auth_key, _terms, _filters)

            #Get results from API
            return [Behance(data=wip) for wip in self._do_api_search(_url)['wips']]

    def get_wip(self, wip_id):
        return WIP(wip_id, self.auth_key)

    def collection_search(self, *args, **kwargs):
        if len(args) == 0:
            return None
        else:
            _base_url = url_join(ENDPOINTS['api'], ENDPOINTS['collection'])
            _terms = "+".join(urllib.parse.quote(arg) for arg in args)
            _filters = urllib.parse.urlencode(kwargs)
            _url = '%s?api_key=%s&q=%s&%s' % (_base_url, self.auth_key, _terms, _filters)

            #Get results from API
            return [Behance(data=collection) for collection in self._do_api_search(_url)['collections']]

    def get_collection(self, collection_id):
        return Collection(collection_id, self.auth_key)

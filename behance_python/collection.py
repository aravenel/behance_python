import urllib
from behance import Behance
from behance_python import ENDPOINTS, url_join

class Collection(Behance):

    def __init__(self, collection_id, auth_key):
        Behance.__init__(self, auth_key)
        self.collection_id = collection_id
        self.base_url = url_join(ENDPOINTS['api'], ENDPOINTS['collection'])

        self._get_collection_details()

    def _get_collection_details(self):
        _url = url_join(self.base_url, str(self.collection_id))
        _params = self._build_params()

        _results = self._get_api_data(_url, _params)['collection']
        self.set_data(_results)

    def get_projects(self, **kwargs):
        _url = url_join(self.base_url, self.collection_id, 'projects')
        _params = self._build_params(kwargs)

        return self._parse_data(self._get_api_data(_url, _params)['projects'])

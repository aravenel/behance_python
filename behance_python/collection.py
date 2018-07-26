import urllib
from behance_python.behance import Behance
from behance_python import ENDPOINTS, url_join

class Collection(Behance):

    def __init__(self, collection_id, auth_key):
        Behance.__init__(self, auth_key)
        self.collection_id = collection_id
        self.base_url = url_join(ENDPOINTS['api'], ENDPOINTS['collection'])

        self._get_collection_details()

    def _get_collection_details(self):
        _url = url_join(self.base_url, str(self.collection_id))
        _url = "%s?api_key=%s" % (_url, self.auth_key)

        _results = self._get_api_data(_url)['collection']
        self.set_data(_results)

    def get_projects(self, **kwargs):
        _base_url = url_join(self.base_url, self.collection_id, 'projects')
        if len(kwargs) > 0:
            _filters = urllib.urlencode(kwargs)
            _url = '%s?api_key=%s&%s' % (_base_url, self.auth_key, _filters)
        else:
            _url = '%s?api_key=%s' % (_base_url, self.auth_key)

        return self._parse_data(self._get_api_data(_url)['projects'])

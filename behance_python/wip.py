import urllib
from behance_python import ENDPOINTS, url_join
from behance import Behance

class WIP(Behance):

    def __init__(self, wip_id, auth_key):
        #super(Behance, self).__init__(auth_key)
        Behance.__init__(self, auth_key)
        self.wip_id = wip_id
        self.base_url = url_join(ENDPOINTS['api'], ENDPOINTS['wip'])

        self._get_wip_details()

    def _get_wip_details(self):
        _url = url_join(self.base_url, self.wip_id)
        _params = self._build_params()

        _results = self._get_api_data(_url, _params)['wip']
        self.set_data(_results)

    def get_revision(self, revision_id):
        _url = url_join(self.base_url, self.wip_id, str(revision_id))
        _params = self._build_params()

        return self._parse_data(self._get_api_data(_url, _params)['revision'])

    def get_revision_comments(self, revision_id, **kwargs):
        _url = url_join(self.base_url, self.wip_id, str(revision_id), '/comments')
        _params = self._build_params(kwargs)

        return self._parse_data(self._get_api_data(_url, _params)['comments'])

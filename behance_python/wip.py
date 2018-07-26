import urllib
from behance_python import ENDPOINTS, url_join
from behance_python.behance import Behance

class WIP(Behance):

    def __init__(self, wip_id, auth_key):
        #super(Behance, self).__init__(auth_key)
        Behance.__init__(self, auth_key)
        self.wip_id = wip_id
        self.base_url = url_join(ENDPOINTS['api'], ENDPOINTS['wip'])

        self._get_wip_details()

    def _get_wip_details(self):
        _url = url_join(self.base_url, self.wip_id)
        _url = '%s?api_key=%s' % (_url, self.auth_key)
        _results = self._get_api_data(_url)['wip']
        self.set_data(_results)

    def get_revision(self, revision_id):
        _url = url_join(self.base_url, self.wip_id, str(revision_id))
        _url = '%s?api_key=%s' % (_url, self.auth_key)
        return self._parse_data(self._get_api_data(_url)['revision'])

    def get_revision_comments(self, revision_id, **kwargs):
        _base_url = url_join(self.base_url, self.wip_id, str(revision_id), '/comments')
        if len(kwargs) > 0:
            _filters = urllib.urlencode(kwargs)
            _url = '%s?api_key=%s&%s' % (_base_url, self.auth_key, _filters)
        else:
            _url = '%s?api_key=%s' % (_base_url, self.auth_key)

        return self._parse_data(self._get_api_data(_url)['comments'])

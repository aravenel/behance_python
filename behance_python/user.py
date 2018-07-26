import urllib
from behance_python.behance import Behance
from behance_python import ENDPOINTS, url_join

#   TODO: Should get_projects return project objects? How to do this with min overhead?

class User(Behance):

    def __init__(self, user_id, auth_key):
        Behance.__init__(self, auth_key)
        self.user_id = user_id
        self.base_url = url_join(ENDPOINTS['api'], ENDPOINTS['user'])

        self._get_user_details()

    def _get_user_details(self):
        #Build the URL
        _url = url_join(self.base_url, str(self.user_id))
        _url = "%s?api_key=%s" % (_url, self.auth_key)

        #Call the API
        _results = self._get_api_data(_url)['user']
        self.set_data(_results)

    def get_projects(self, **kwargs):

        _base_url = url_join(self.base_url, self.user_id, 'projects')
        if len(kwargs) > 0:
            _filters = urllib.urlencode(kwargs)
            _url = '%s?api_key=%s&%s' % (_base_url, self.auth_key, _filters)
        else:
            _url = '%s?api_key=%s' % (_base_url, self.auth_key)

        return self._parse_data(self._get_api_data(_url)['projects'])

    def get_wips(self, **kwargs):
        _base_url = url_join(self.base_url, self.user_id, 'wips')
        if len(kwargs) > 0:
            _filters = urllib.urlencode(kwargs)
            _url = '%s?api_key=%s&%s' % (_base_url, self.auth_key, _filters)
        else:
            _url = '%s?api_key=%s' % (_base_url, self.auth_key)

        return self._parse_data(self._get_api_data(_url)['wips'])

    def get_appreciations(self, **kwargs):
        _base_url = url_join(self.base_url, self.user_id, 'appreciations')
        if len(kwargs) > 0:
            _filters = urllib.urlencode(kwargs)
            _url = '%s?api_key=%s&%s' % (_base_url, self.auth_key, _filters)
        else:
            _url = '%s?api_key=%s' % (_base_url, self.auth_key)

        return self._parse_data(self._get_api_data(_url)['appreciations'])

    def get_collections(self, **kwargs):
        _base_url = url_join(self.base_url, self.user_id, 'collections')
        if len(kwargs) > 0:
            _filters = urllib.urlencode(kwargs)
            _url = '%s?api_key=%s&%s' % (_base_url, self.auth_key, _filters)
        else:
            _url = '%s?api_key=%s' % (_base_url, self.auth_key)

        return self._parse_data(self._get_api_data(_url)['collections'])

    def get_stats(self):
        _base_url = url_join(self.base_url, self.user_id, 'stats')
        _url = "%s?api_key=%s" % (_base_url, self.auth_key)

        return self._parse_data(self._get_api_data(_url)['stats'])

    def get_followers(self, **kwargs):
        _base_url = url_join(self.base_url, self.user_id, 'followers')
        if len(kwargs) > 0:
            _filters = urllib.urlencode(kwargs)
            _url = '%s?api_key=%s&%s' % (_base_url, self.auth_key, _filters)
        else:
            _url = '%s?api_key=%s' % (_base_url, self.auth_key)

        return self._parse_data(self._get_api_data(_url)['followers'])

    def get_following(self, **kwargs):
        _base_url = url_join(self.base_url, self.user_id, 'following')
        if len(kwargs) > 0:
            _filters = urllib.urlencode(kwargs)
            _url = '%s?api_key=%s&%s' % (_base_url, self.auth_key, _filters)
        else:
            _url = '%s?api_key=%s' % (_base_url, self.auth_key)

        return self._parse_data(self._get_api_data(_url)['following'])

    def get_work_experience(self):
        _base_url = url_join(self.base_url, self.user_id, 'work_experience')
        _url = "%s?api_key=%s" % (_base_url, self.auth_key)

        return self._parse_data(self._get_api_data(_url)['work_experience'])

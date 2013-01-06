import urllib
from behance import Behance
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
        _params = self._build_params()

        #Call the API
        _results = self._get_api_data(_url, _params)['user']
        self.set_data(_results)

    def get_projects(self, **kwargs):
        _url = url_join(self.base_url, self.user_id, 'projects')
        params = self._build_params(kwargs)

        return self._parse_data(self._get_api_data(_url, params)['projects'])

    def get_wips(self, **kwargs):
        _url = url_join(self.base_url, self.user_id, 'wips')
        _params = self._build_params(kwargs)

        return self._parse_data(self._get_api_data(_url, _params)['wips'])

    def get_appreciations(self, **kwargs):
        _url = url_join(self.base_url, self.user_id, 'appreciations')
        _params = self._build_params(kwargs)

        return self._parse_data(self._get_api_data(_url, _params)['appreciations'])

    def get_collections(self, **kwargs):
        _url = url_join(self.base_url, self.user_id, 'collections')
        _params = self._build_params(kwargs)

        return self._parse_data(self._get_api_data(_url, _params)['collections'])

    def get_stats(self):
        _url = url_join(self.base_url, self.user_id, 'stats')
        _params = self._build_params()
        
        return self._parse_data(self._get_api_data(_url, _params)['stats'])

    def get_followers(self, **kwargs):
        _url = url_join(self.base_url, self.user_id, 'followers')
        _params = self._build_params(kwargs)

        return self._parse_data(self._get_api_data(_url, _params)['followers'])

    def get_following(self, **kwargs):
        _url = url_join(self.base_url, self.user_id, 'following')
        _params = self._build_params(kwargs)

        return self._parse_data(self._get_api_data(_url, _params)['following'])

    def get_feedback(self):
        _url = url_join(self.base_url, self.user_id, 'feedback')
        _params = self._build_params()
        
        return self._parse_data(self._get_api_data(_url, _params)['feedback_circle'])

    def get_work_experience(self):
        _url = url_join(self.base_url, self.user_id, 'work_experience')
        _params = self._build_params()
        
        return self._parse_data(self._get_api_data(_url, _params)['work_experience'])

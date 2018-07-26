ENDPOINTS = {
        'api': 'http://www.behance.net/v2',
        'project': '/projects',
        'user': '/users',
        'wip': '/wips',
        'collection': '/collections',
        }

def url_join(*args):
    return "/".join(str(s).strip('/') for s in args)

from behance_python.api import *
from behance_python.project import *
from behance_python.exceptions import *
from behance_python.behance import *

ENDPOINTS = {
        'api': 'http://www.behance.net/v2',
        'project': '/projects',
        'user': '/users',
        'wip': '/wips',
        'collection': '/collections',
        }

def url_join(*args):
    return "/".join(str(s).strip('/') for s in args)

from api import *
from project import *
from exceptions import *
from behance import *

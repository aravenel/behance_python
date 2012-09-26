import unittest
import os
from behance_python.api import API
from behance_python.exceptions import *

API_KEY = os.environ.get('BEHANCE_API_KEY')
PROJECT_ID = '5287059'
USER_NAME = 'MatiasCorea'
WIP_ID = '77'
WIP_REVISION_ID = '177'
COLLECTION_ID = '14373'

#Attributes to check existence of in returned values
#These keys should exist in both "stub" (from search functions) and "full"
#(from get_XXXX functions) values
PROJECT_KEYS = ['id', 'name', 'published_on']
USER_KEYS = ['id', 'username', 'created_on']
WIP_KEYS = ['id', 'title', 'revision_count']
COLLECTION_KEYS = ['id', 'owners', 'stats']

class BehanceTestCase(unittest.TestCase):
    def setUp(self):
        self.api = API(API_KEY)

class TestProject(BehanceTestCase):

    def test_search(self):
        projects = self.api.project_search('apple')
        self.assertEqual(len(projects), 12)
        for project in projects:
            for key in PROJECT_KEYS:
                self.assertTrue(project.has_key(key))

    def test_project(self):
        project = self.api.get_project(PROJECT_ID)
        self.assertIsNotNone(project)
        for key in PROJECT_KEYS:
            self.assertTrue(hasattr(project, key))

    def test_comments(self):
        project = self.api.get_project(PROJECT_ID)
        comments = project.get_comments()
        self.assertGreater(len(comments), 1)
        for comment in comments:
            for key in ['user', 'comment']:
                self.assertTrue(comment.has_key(key))

    def test_exception(self):
        with self.assertRaises(NotFound):
            project = self.api.get_project(1234)
        with self.assertRaises(Forbidden):
            self.api = API('12345')
            projs = self.api.project_search('apple')

class TestUser(BehanceTestCase):

    def test_search(self):
        users = self.api.user_search('alex')
        self.assertEqual(len(users), 12)
        for user in users:
            for key in USER_KEYS:
                self.assertTrue(user.has_key(key))

    def test_user(self):
        user = self.api.get_user(USER_NAME)
        self.assertIsNotNone(user)
        for key in USER_KEYS:
            self.assertTrue(hasattr(user, key))
    
    def test_user_projects(self):
        user = self.api.get_user(USER_NAME)
        projects = user.get_projects()
        self.assertIsNotNone(projects)
        for project in projects:
            for key in PROJECT_KEYS:
                self.assertTrue(project.has_key(key))

    def test_user_wips(self):
        user = self.api.get_user(USER_NAME)
        wips = user.get_wips()
        self.assertIsNotNone(wips)
        for wip in wips:
            for key in WIP_KEYS:
                self.assertTrue(wip.has_key(key))

    def test_user_appreciations(self):
        user = self.api.get_user(USER_NAME)
        appreciations = user.get_appreciations()
        self.assertIsNotNone(appreciations)
        for appreciation in appreciations:
            for key in ['project', 'timestamp']:
                self.assertTrue(appreciation.has_key(key))

    def test_user_collections(self):
        user = self.api.get_user(USER_NAME)
        collections = user.get_collections()
        self.assertIsNotNone(collections)
        for collection in collections:
            for key in COLLECTION_KEYS:
                self.assertTrue(collection.has_key(key))

    def test_exception(self):
        with self.assertRaises(NotFound):
            user = self.api.get_user('asdf1234')
        with self.assertRaises(Forbidden):
            self.api = API('12345')
            users = self.api.user_search('apple')

class TestWIP(BehanceTestCase):

    def test_search(self):
        wips = self.api.wip_search('apple')
        self.assertEqual(len(wips), 12)
        for wip in wips:
            for key in WIP_KEYS:
                self.assertTrue(wip.has_key(key))

    def test_wip(self):
        wip = self.api.get_wip(WIP_ID)
        self.assertIsNotNone(wip)
        for key in WIP_KEYS:
            self.assertTrue(hasattr(wip, key))

    def test_revision(self):
        wip = self.api.get_wip(WIP_ID)
        revision = wip.get_revision(WIP_REVISION_ID)
        for key in ['id', 'description', 'image']:
            self.assertTrue(revision.has_key(key))

    def test_comments(self):
        wip = self.api.get_wip(WIP_ID)
        comments = wip.get_revision_comments(WIP_REVISION_ID)
        for comment in comments:
            for key in ['user', 'comment', 'created_on']:
                self.assertTrue(comment.has_key(key))

    def test_exception(self):
        with self.assertRaises(NotFound):
            wip = self.api.get_wip('asdf1234')
        with self.assertRaises(Forbidden):
            self.api = API('12345')
            wips = self.api.wip_search('apple')

class TestCollection(BehanceTestCase):
    
    def test_search(self):
        collections = self.api.collection_search('apple')
        self.assertGreaterEqual(len(collections), 1)
        for collection in collections:
            for key in COLLECTION_KEYS:
                self.assertTrue(collection.has_key(key))

    def test_collection(self):
        collection = self.api.get_collection(COLLECTION_ID)
        self.assertIsNotNone(collection)
        for key in COLLECTION_KEYS:
            self.assertTrue(hasattr(collection, key))

    def test_collection_projects(self):
        collection = self.api.get_collection(COLLECTION_ID)
        projects = collection.get_projects()
        for project in projects:
            for key in PROJECT_KEYS:
                self.assertTrue(project.has_key(key))

    def test_exception(self):
        with self.assertRaises(NotFound):
            collection = self.api.get_collection('asdf1234')
        with self.assertRaises(Forbidden):
            self.api = API('12345')
            collections = self.api.collection_search('apple')

if __name__ == '__main__':
    unittest.main()

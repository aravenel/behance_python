from project import Project

class API:
    """Base wrapper for the Behance api.
    
    Must be instantiated using your provided auth key."""

    def __init__(self, auth_key):
        self.auth_key = auth_key

    def get_project(self, project_id):
        """Query behance API and return Project object"""
        return Project(project_id, self.auth_key)

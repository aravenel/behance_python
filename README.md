behance_python
==============

A Python wrapper for the Behance API
------------------------------------

####Warning! This wrapper is very much still in development and could change substantially!

Please see [Behance API documentation](http://www.behance.net/dev) to get an API key and more information.

#Installation
TBD. Need to do packaging.
Depends on the excellent Requests library.

#Usage
All wrapper functionality flows from the main API object which must be
instantiated using your Behance-provided API Key.

##API Object Usage
```python
from behance_python import API

behance = API('your_api_key_here')
```

##Project functionality
###Search for projects
```python
projects = behance.project_search('term1', 'term2', filter_key='filter_value')
```

Supports all filters and modifiers as supported by Behance:
- sort
- time
- field
- country
- state
- page
- tags

Data will be returned as list of dictionaries with same keys and data formats
as Behance API.

###Get Single Project Details
```python
proj = behance.get_project(project_id)
```

Returns an instance of the Project object. This object has attributes named
identically to attributes as returned by Behance API. As with the API, 
artwork associated with a project are stored in Project.modules, which is a list
of dictionaries, each dictionary representing one module and its corresponding
metadata.

###Get Project Comments
```python
comments = proj.get_comments()
```
Method of the Project object. Returns list of dictionaries, each dictionary
representing a single comment and its metadata.

##User functionality
###Search for Users
```python
users = behance.user_search('term1', 'term2', filter_key='filter_value')
```
Works just like project_search.

###Get Single User Details
```python
user = behance.get_user(user_id_or_username)
```
Returns User object. This object has attributes named identically to attributes
as returned by Behance API. 


###Get User Projects
```python
user_projects = user.get_projects(filter_key='filter_value')
```
Method of the User object. Can optionally include any filters supported by Behance API.

###Get User Works in Progress
```python
user_wips = user.get_wips(filter_key='filter_value')
```
Method of the User object. Can optionally include any filters supported by Behance API.

###Get User Appreciations
```python
user_appreciations = user.get_appreciations(filter_key='filter_value')
```
Method of the User object. Can optionally include any filters supported by Behance API.

###Get User Collections
```python
user_collections = user.get_collections(filter_key='filter_value')
```
Method of the User object. Can optionally include any filters supported by Behance API.

##Work in Progress Functionality
TBD.

#Exceptions
Unfortunately, they happen. If an exception happens in the calling of the API
(e.g. a timeout), the library will raise the exception from the underlying Requests
library. If the response from the Behance API is anything other than status code
200, it will raise a BehanceException exception with the number of the status
code. Eventually, will move to separate exception types for each error code.

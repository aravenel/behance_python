behance_python
==============

A Python wrapper for the Behance API
------------------------------------

####Warning! This wrapper is very much still in development and could change substantially!

Please see [Behance API documentation](http://www.behance.net/dev) to get an API key and more information.

#Installation
TBD. Need to do packaging.

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
proj.get_comments()
```
Method of the Project object. Returns list of dictionaries, each dictionary
representing a single comment and its metadata.

##User functionality
TBD.

##Work in Progress Functionality
TBD.

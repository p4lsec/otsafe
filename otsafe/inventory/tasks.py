"""
This file holds inventory-related tasks and functions.  It will eventually hold things like database connectors for a local/remote database.  It also includes functions for getting inventory data from the database.  

It also interfaces with other external datasources via querying a REST API. 

These functions can also build a local database from the REST API, and can update the local database from the REST API.  This is useful for testing purposes, and for when the REST API is down.  It is also useful for when the REST API is not available, such as when the system is running in a remote location with no internet access.

 It is the only file that should be allowed to access the database directly.  All other files should access the database via this file.

"""


def get_owner() -> str:
    """
    Returns the owner of a component from the database.  Currently just returns a string, but will eventually return a business entity object. 
    """
    return "Owner's Name Here"

def get_bu() -> str:
    """
    Returns the BU of a component from the database.  Currently just returns a string, but will eventually return a business entity object. 
    """
    return "Business Unit's Name Here"
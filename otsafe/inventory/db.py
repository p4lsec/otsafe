"""
Functions for connecting to any given databases detected in .env file.  Can be multiple databases, but only one is currently supported.  Will eventually support multiple databases.  For now, it just connects to the first database in the list.  Uses psycopg2 for a local or remote Postgres container.  Will eventually support other databases types.
"""

import os
from typing import Any

import psycopg2
from dotenv import load_dotenv

load_dotenv()

def connect_to_db() -> Any:
    """
    Creates the initial connection to the database.  Returns a psycopg2 connection object.
    """

    # Get database connection information from environment variables
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_pasw = os.getenv("DB_PASW")

    # Create connection string
    conn_string = f"host={db_host} port={db_port} dbname={db_name} user={db_user} password={db_pasw}"

    # Create connection object
    try:
        conn = psycopg2.connect(conn_string)
    except Exception as err:
        raise ConnectionError("Unable to connect to database") from err

    return conn

def get_db_cursor(conn: Any) -> Any:
    """
    Creates a cursor object from a psycopg2 connection object.  Returns a psycopg2 cursor object.
    """

    # Create cursor object
    cur = conn.cursor()

    return cur

def close_db_cursor(cur: Any) -> None:
    """
    Closes a psycopg2 cursor object.  Returns None.
    """
    
    cur.close()

def close_db_connection(conn: Any) -> None:
    """
    Closes a psycopg2 connection object.  Returns None.
    """
    
    conn.close()

def get_db_data(cur: Any, query: str) -> Any:
    """
    Executes a query on a psycopg2 cursor object.  Returns the results of the query.
    """
    
    cur.execute(query)
    return cur.fetchall()

def get_db_data_by_id(cur: Any, query: str, id: str) -> Any:
    """
    Executes a query on a psycopg2 cursor object.  Returns the results of the query.
    """
    
    cur.execute(query, (id,))
    return cur.fetchall()

def get_db_data_by_name(cur: Any, query: str, name: str) -> Any:
    """
    Executes a query on a psycopg2 cursor object.  Returns the results of the query.
    """
    
    cur.execute(query, (name,))
    return cur.fetchall()

def get_db_data_by_description(cur: Any, query: str, description: str) -> Any:
    """
    Executes a query on a psycopg2 cursor object.  Returns the results of the query.
    """
    
    cur.execute(query, (description,))
    return cur.fetchall()

def get_db_data_by_owner(cur: Any, query: str, owner: str) -> Any:
    """
    Executes a query on a psycopg2 cursor object.  Returns the results of the query.
    """
    
    cur.execute(query, (owner,))
    return cur.fetchall()

def get_db_data_by_bu(cur: Any, query: str, bu: str) -> Any:
    """
    Executes a query on a psycopg2 cursor object.  Returns the results of the query.
    """
    
    cur.execute(query, (bu,))
    return cur.fetchall()

def get_db_data_by_type(cur: Any, query: str, type: str) -> Any:
    """
    Executes a query on a psycopg2 cursor object.  Returns the results of the query.
    """
    
    cur.execute(query, (type,))
    return cur.fetchall()   

def get_db_data_by_status(cur: Any, query: str, status: str) -> Any:
    """
    Executes a query on a psycopg2 cursor object.  Returns the results of the query.
    """
    
    cur.execute(query, (status,))
    return cur.fetchall()

def get_db_data_by_location(cur: Any, query: str, location: str) -> Any:
    """
    Executes a query on a psycopg2 cursor object.  Returns the results of the query.
    """
    
    cur.execute(query, (location,))
    return cur.fetchall()


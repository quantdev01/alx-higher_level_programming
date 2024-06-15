#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_101_usa along with their associated State objects.

Usage:
    ./102-relationship_cities_states_list.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: The MySQL username.
    mysql_password: The MySQL password.
    database_name: The name of the database to connect to.

Dependencies:
    - SQLAlchemy: This script requires the SQLAlchemy library to interact with the MySQL database.

Note:
    - This script connects to a MySQL server running on localhost at port 3306.
    - It uses only one query to the database and the state relationship to access the State object linked to each City object.
    - Results are sorted in ascending order by cities.id.
    - Results are displayed in the format "<city id>: <city name> -> <state name>".

Example:
    ./102-relationship_cities_states_list.py root password hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Get MySQL username, password, and database name fro
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine to the specified database
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}\
:{mysql_password}@localhost:3306/{database_name}'
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all City objects with their associated State objects
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()

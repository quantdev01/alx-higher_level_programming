#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the databas
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL username, password, database name, and state na
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_to_search = sys.argv[4]

    # Create an engine to the specified database
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}\
:{mysql_password}@localhost:3306/{database_name}'
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the database to get the State object
    to_filter = session.query(State)
    state = to_filter.filter(State.name == state_name_to_search).first()

    # Print the result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()

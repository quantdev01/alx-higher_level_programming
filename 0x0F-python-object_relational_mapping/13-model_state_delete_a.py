#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL username, password, and database
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine to the specified database
    engine = create_engine(f'mysql+mysqldb://{mysql_username}\
:{mysql_password}@localhost:3306/{database_name}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects with a name containing the letter 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%\
')).all()

    # Delete each state object found
    for state in states_to_delete:
        session.delete(state)

    # Commit the transaction to the database
    session.commit()

    # Close the session
    session.close()

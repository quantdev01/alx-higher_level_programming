#!/usr/bin/python3
"""
Creates the State “California” with the City
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Get MySQL username, password, and database name from 
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine to the specified database
    engine = create_engine(f'mysql+mysqldb://{mysql_username}\
:{mysql_password}@localhost:3306/{database_name}')

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State object
    california = State(name="California")

    # Create a new City object
    san_francisco = City(name="San Francisco", state=california)

    # Add the new State and City objects to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the transaction to the database
    session.commit()

    # Close the session
    session.close()

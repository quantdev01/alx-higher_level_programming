#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Get MySQL username, password, and database
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

    # Query the database to get all City objects sorted by id
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    to_filter = session.query(State.name)
    for city in cities:
        state_name = to_filter.filter(State.id == city.state_id).first()[0]
        print(f"{state_name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

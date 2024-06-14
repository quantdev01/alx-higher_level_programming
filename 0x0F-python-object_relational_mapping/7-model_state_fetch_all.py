#!/usr/bin/python3
""" Documenting my python3 """

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

args = sys.argv

ln = len(args)

if ln <= 3:
    print("Insufusant arguments, need 3 args")

username = args[0]
password = args[1]
db_name = args[2]
host = 'localhost'
port = '3306'

database_url = f"mysql+pymysql://{username}:{password}@{host}/{db_name}"
engine = create_engine(database_url)

Session = sessionmaker(bind=engine)

session = Session()

states = session.query(State).order_by(State.id).all()

for state in states:
    print(F"{state.id}: {state.name}")

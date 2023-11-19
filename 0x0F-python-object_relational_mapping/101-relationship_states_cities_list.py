#!/usr/bin/python3
"""Script to list all State objects and corresponding City objects
from the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    # Database connection parameters
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    # Create the tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get all State objects and their corresponding City objects
    states_cities = (session.query(State, City)
                     .join(City, State.id == City.state_id)
                     .order_by(State.id, City.id)
                     .all())

    # Print the results
    current_state_id = None
    for state, city in states_cities:
        if state.id != current_state_id:
            print("{}: {}".format(state.id, state.name))
            current_state_id = state.id
        print("\t{}: {}".format(city.id, city.name))

    # Close the session
    session.close()

#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    enginie = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)
    Base.metadata.create_all(enginie)

    Session = sessionmaker(bind=enginie)
    session = Session()

    for state in session.query(State).order_by(State.id.asc()):
        print("{}: {}".format(state.id, state.name))

    session.close()

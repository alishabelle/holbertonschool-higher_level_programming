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

    states = session.query(State).first()

    if states is not None:
        print("{}: {}".format(states.id, states.name))
    else:
        print('Nothing')

    session.close()

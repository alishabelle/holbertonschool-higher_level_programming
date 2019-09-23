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

    jawn = State(name='Louisiana')
    session.add(jawn)
    session.commit()

    print(jawn.id)
    session.close()

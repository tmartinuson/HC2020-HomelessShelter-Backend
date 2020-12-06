import sys

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

from server.model.base import Base
from server.service.session import Session

DATABASE = 'sqlite:////tmp/foobar.db'

def main():
    engine = create_engine(DATABASE)
    Session.configure(bind=engine)

    try:
        Base.metadata.create_all(engine)
    except OperationalError:
        print('Could not connect to database')
        sys.exit(1)
    else:
        print('Connected to database')


if __name__ == '__main__':
    main()

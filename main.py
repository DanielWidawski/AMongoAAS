import logging

from sqlalchemy import create_engine

from db.deployments_manager.sql_deployments import Base



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)

def get_db_engine():
    engine = create_engine('postgresql://{}:{}@{}/{}'.format('postgres', 'postgres', 'localhost:5432', 'deployments'))
    Base.metadata.create_all(engine)
    return engine

while True:
    try:
        db_engine = get_db_engine().connect()
        if db_engine:
            break
    except Exception as e:
        LOGGER.warning(f"++++ Retrying connection to the db bc of the issue {str(e)}++++")
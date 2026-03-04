from sqlalchemy import create_engine
from sql_deployments import Base

engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format('postgres','postgres','localhost:5432','deployments'))
Base.metadata.create_all(engine)

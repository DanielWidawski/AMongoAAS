from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.deployments_db.sql_deployments import Base, SqlDeployments

engine = create_engine('postgresql://{}:{}@{}/{}'.format('postgres', 'postgres', 'localhost:5432', 'deployments'))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
deployments_db = SqlDeployments()
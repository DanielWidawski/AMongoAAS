# from sqlalchemy import create_engine
# from sqlalchemy.orm import DeclarativeBase, sessionmaker

# class Base(DeclarativeBase):
#     pass

# engine = create_engine('postgresql://{}:{}@{}/{}'.format('postgres', 'postgres', 'localhost:5432', 'deployments'))
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
from datetime import datetime
from uuid import UUID
import uuid

from sqlalchemy import DateTime, String, Enum, create_engine, select, update
import sqlalchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from common.models import Deployment, Status
from db.deployments_db.deployments_db import DeploymentsDb

class Base(DeclarativeBase):
    pass

class Deployments(Base):
    __tablename__ = 'deployments'
    id: Mapped[UUID] = mapped_column(sqlalchemy.UUID,primary_key=True)
    db_name: Mapped[str] = mapped_column(String(30))
    status: Mapped[Enum] = mapped_column(Enum(Status))
    username: Mapped[str] = mapped_column(String(30))
    creation_time: Mapped[datetime] = mapped_column(DateTime)
    
engine = create_engine('postgresql://{}:{}@{}/{}'.format('postgres', 'postgres', 'localhost:5432', 'deployments'))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class SqlDeployments(DeploymentsDb):
    def record_deployment(self, deployment: Deployment):
        with Session() as session:
            row = Deployments(**deployment.model_dump())
            session.add(row)
            session.commit()

    def get_deployment(self, deployment_id: UUID) -> Deployment:
        with Session() as session:
            stmt = select(Deployments).where(Deployments.id == deployment_id)
            result = session.execute(stmt).scalars().one()
            return Deployment(**result.__dict__)

    def update_deployment(self, deployment_id: UUID, db_name: str):
        raise NotImplementedError

    def delete_deployment(self, deployment_id: UUID):
        with Session() as session:
            stmt = update(Deployments).where(Deployments.id == deployment_id).values(status=Status.DELETED)
            session.execute(stmt)
            session.commit()




    
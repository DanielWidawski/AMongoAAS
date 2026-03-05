from datetime import datetime
import enum
from uuid import UUID
import uuid

from sqlalchemy import DateTime, String, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from common.models import Status
from db.deployments_db.deployments_db import DeploymentsDb

class Base(DeclarativeBase):
    pass

class Deployments(Base):
    __tablename__ = 'deployments'
    id: Mapped[UUID] = mapped_column(default=uuid.uuid4(),primary_key=True)
    db_name: Mapped[str] = mapped_column(String(30))
    status: Mapped[Enum] = mapped_column(Enum(Status))
    username: Mapped[str] = mapped_column(String(30))
    creation_time: Mapped[datetime] = mapped_column(DateTime)
    
    
class SqlDeployments(DeploymentsDb):
    
    def record_deployment(self):
        raise NotImplementedError

    def get_deployment(self):
        raise NotImplementedError

    def update_deployment(self):
        raise NotImplementedError

    def delete_deployment(self):
        raise NotImplementedError

    
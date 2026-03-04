
from datetime import datetime
import enum
from uuid import UUID
import uuid


from sqlalchemy import DateTime, String, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column




class Base(DeclarativeBase):
    pass

class Status(enum.Enum):
    CREATED = 'CREATED',
    DELETED = 'DELETED'

class Deployment(Base):
    __tablename__ = 'deployments_db'
    id: Mapped[str] = mapped_column(primary_key=True)
    db_name: Mapped[str] = mapped_column(String(30))
    status: Mapped[Enum] = mapped_column(Enum(Status))
    username: Mapped[str] = mapped_column(String(30))
    creation_time: Mapped[datetime] = mapped_column(DateTime)
    

    



    
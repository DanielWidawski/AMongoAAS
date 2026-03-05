from datetime import datetime
import enum
from uuid import UUID
import uuid

from pydantic import BaseModel, Field

class Status(enum.Enum):
    CREATED = 'CREATED',
    DELETED = 'DELETED'

class Deployments(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    db_name: str
    status: Status = Field(default=Status.CREATED)
    # TODO: add validator
    username: str
    creation_time: datetime
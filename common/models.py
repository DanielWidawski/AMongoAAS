from datetime import datetime
import enum
from uuid import UUID
import uuid

from pydantic import BaseModel, ConfigDict, Field

class Status(enum.Enum):
    CREATED = 'CREATED',
    DELETED = 'DELETED'

class Deployment(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: UUID = Field(default_factory= lambda: uuid.uuid4())
    db_name: str
    status: Status = Field(default=Status.CREATED)
    username: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now())
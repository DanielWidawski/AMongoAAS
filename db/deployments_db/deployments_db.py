from abc import ABC, abstractmethod
from uuid import UUID

from common.models import Deployment


class DeploymentsDb(ABC):
    
    @abstractmethod
    def record_deployment(self, deployment: Deployment):
        ...
    
    @abstractmethod
    def get_deployment(self, deployment_id: UUID) -> Deployment:
        ...
    
    @abstractmethod
    def update_deployment(self, deployment_id: UUID, db_name: str):
        ...
    
    @abstractmethod
    def delete_deployment(self, deployment_id: UUID):
        ...
    
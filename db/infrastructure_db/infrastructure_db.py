from abc import ABC, abstractmethod
from uuid import UUID

from common.models import Deployment


class InfrastructureDb(ABC):
    
    @abstractmethod
    def create_deployment(self, deployment: Deployment):
        ...
    
    @abstractmethod
    def delete_deployment(self, deployment_id: UUID):
        ...
    
    @abstractmethod
    def update_deployment(self, deployment_id: UUID, db_name: str):
        ...
    
    def get_connection_string(self):
        ...
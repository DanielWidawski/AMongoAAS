from abc import ABC, abstractmethod
from uuid import UUID

from common.models import Deployment


class InfrastructureDb(ABC):
    
    @abstractmethod
    def create_deployment(self, deployment: Deployment):
        ...
    
    @abstractmethod
    def delete_deployment(self, db_name: str):
        ...
    
    @abstractmethod
    def update_deployment(self, deployment_id: UUID, db_name: str):
        ...
        
    @abstractmethod
    def get_connection_string(self):
        ...
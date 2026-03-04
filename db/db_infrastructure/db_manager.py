from abc import ABC, abstractmethod


class InfrastructureDb(ABC):
    
    @abstractmethod
    def create_deployment(self):
        ...
    
    @abstractmethod
    def delete_deployment(self, deployment_id):
        ...
    
    @abstractmethod
    def update_deployment(self, new_name: str):
        ...
    
    def get_connection_string(self):
        ...
from abc import ABC, abstractmethod


class DeploymentsDb(ABC):
    
    @abstractmethod
    def record_deployment(self):
        ...
    
    @abstractmethod
    def get_deployment(self):
        ...
    
    @abstractmethod
    def update_deployment(self):
        ...
    
    @abstractmethod
    def delete_deployment(self):
        ...
    
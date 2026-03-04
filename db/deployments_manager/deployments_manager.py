from abc import ABC, abstractmethod
import uuid


class DeploymentsManager(ABC):
    
    @abstractmethod
    def record_deployment(self):
        ...
    
    def id_generator(self):
        return uuid.uuid4().hex
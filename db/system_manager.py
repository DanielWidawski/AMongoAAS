from db.deployments_db.deployments_db import DeploymentsDb
from db.infrastructure_db.infrastructure_db import InfrastructureDb


class SystemManager:
    
    def __init__(self, infrastructure_db: InfrastructureDb, deployments_db: DeploymentsDb):
        self.infrastructure_db: InfrastructureDb = infrastructure_db
        self.deployments_db: DeploymentsDb = deployments_db
    
    def create_deployment(self):
        self.deployments_db.record_deployment()
        self.infrastructure_db.create_deployment()
        
    def get_deployment(self):
        self.deployments_db.get_deployment()
        
    def update_deployment(self):
        self.deployments_db.update_deployment()
        self.infrastructure_db.update_deployment()
        
    def delete_deployment(self):
        self.deployments_db.delete_deployment()
        self.infrastructure_db.delete_deployment()
        
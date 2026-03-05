from uuid import UUID

from common.models import Deployment
from db.deployments_db.deployments_db import DeploymentsDb
from db.infrastructure_db.infrastructure_db import InfrastructureDb


class SystemManager:
    
    def __init__(self, infrastructure_db: InfrastructureDb, deployments_db: DeploymentsDb):
        self.infrastructure_db: InfrastructureDb = infrastructure_db
        self.deployments_db: DeploymentsDb = deployments_db
    
    def create_deployment(self, deployment: Deployment):
        self.deployments_db.record_deployment(deployment)
        self.infrastructure_db.create_deployment(deployment)
        
    def get_deployment(self, deployment_id: UUID) -> Deployment:
        self.deployments_db.get_deployment(deployment_id)
        
    def update_deployment(self, deployment_id: UUID, db_name: str):
        self.deployments_db.update_deployment()
        self.infrastructure_db.update_deployment()
        
    def delete_deployment(self, deployment_id: UUID):
        dep  = self.deployments_db.get_deployment(deployment_id)
        self.deployments_db.delete_deployment(deployment_id)
        self.infrastructure_db.delete_deployment(dep.db_name)
        
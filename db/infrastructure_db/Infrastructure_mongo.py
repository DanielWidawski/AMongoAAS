from uuid import UUID

from common.models import Deployment
from db.infrastructure_db.infrastructure_db import InfrastructureDb


class InfrastructureMongoDB(InfrastructureDb):
    def create_deployment(self, deployment: Deployment):
        raise NotImplementedError

    def delete_deployment(self, deployment_id: UUID):
        raise NotImplementedError

    def update_deployment(self, deployment_id: UUID, db_name: str):
        raise NotImplementedError

    
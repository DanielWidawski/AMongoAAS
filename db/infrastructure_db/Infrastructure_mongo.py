from uuid import UUID

import pymongo

from common.models import Deployment
from db.infrastructure_db.infrastructure_db import InfrastructureDb

client = pymongo.MongoClient("mongodb://nraboy:password1234@localhost:27017/") 

class InfrastructureMongoDB(InfrastructureDb):
    def create_deployment(self, deployment: Deployment):
        client[deployment.db_name].create_collection("init_collection")
    
    def delete_deployment(self, db_name: str):
        client.drop_database(db_name)

    def update_deployment(self, deployment_id: UUID, db_name: str):
        raise NotImplementedError

    def get_connection_string(self):
        raise NotImplementedError


    
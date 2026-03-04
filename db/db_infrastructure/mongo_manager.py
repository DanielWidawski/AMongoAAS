from db.db_infrastructure.db_manager import InfrastructureDb


class InfrastructureMongoDB(InfrastructureDb):
    def __init__(self):
        pass

    def create_deployment(self):
        pass

    def delete_deployment(self, deployment_id):
        raise NotImplementedError

    def update_deployment(self, new_name):
        raise NotImplementedError

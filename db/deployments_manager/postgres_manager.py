from db.deployments_manager.deployments_manager import DeploymentsManager


class PostgresManager(DeploymentsManager):
    
    def record_deployment(self):
        raise NotImplementedError

    
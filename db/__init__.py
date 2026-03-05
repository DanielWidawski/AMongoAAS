from db.infrastructure_db import infrastructure_db
from db.deployments_db.sql_deployments import SqlDeployments
from db.system_manager import SystemManager


system_manager = SystemManager(infrastructure_db, SqlDeployments())

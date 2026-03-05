from db.infrastructure_db import infrastructure_db
from db.deployments_db import deployments_db
from db.system_manager import SystemManager


system_manager = SystemManager(infrastructure_db, deployments_db)

from datetime import datetime

from common.models import Deployment
from db import infrastructure_db
from db import system_manager
from db.deployments_db import deployments_db
from db.deployments_db.sql_deployments import SqlDeployments
from db.system_manager import SystemManager


def main():
    dep = Deployment(db_name="bamba", username="nivi_hamalka")
    system_manager.create_deployment(dep)
    get_dep = system_manager.get_deployment(dep.id)
    system_manager.delete_deployment(dep.id)
    i = 9

if __name__ == "__main__":
    main()
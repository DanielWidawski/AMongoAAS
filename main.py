from datetime import datetime

from common.models import Deployment
from db import infrastructure_db
from db import system_manager
from db.deployments_db import deployments_db
from db.deployments_db.sql_deployments import SqlDeployments
from db.system_manager import SystemManager


def main():
    dep = Deployment(db_name="asd", creation_time=datetime.now(), username="daniel")
    sql = SqlDeployments()
    sql.record_deployment(dep)
    got = sql.get_deployment(dep.id)
    sql.delete_deployment(dep.id)
    i = 9

if __name__ == "__main__":
    main()
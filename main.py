from db import infrastructure_db
from db import system_manager
from db.deployments_db import deployments_db
from db.system_manager import SystemManager


def main():
    sm = system_manager
    sm.create_deployment()

if __name__ == "__main__":
    main()
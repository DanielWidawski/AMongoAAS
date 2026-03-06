from datetime import datetime

from fastapi import FastAPI
import uvicorn

from common.models import Deployment
from db import infrastructure_db
from db import system_manager
from db.deployments_db import deployments_db
from db.deployments_db.sql_deployments import SqlDeployments
from db.system_manager import SystemManager
from routes.deployments import router as deployments_router

app = FastAPI()
app.include_router(deployments_router)

def main():
    # dep1 = Deployment(db_name="1", username="1")
    # system_manager.create_deployment(dep1)
    # dep2 = Deployment(db_name='2', username='1')
    # system_manager.create_deployment(dep2)
    # print(dep1.id)
    # cop = system_manager.get_deployment(dep1.id)
    # system_manager.delete_deployment(dep1.id)
    # system_manager.delete_deployment(dep2.id)
    # i = 0  
    uvicorn.run(app, host='0.0.0.0', port=8080)
    
if __name__ == "__main__":
    main()
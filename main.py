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
    uvicorn.run(app, host='0.0.0.0', port=8080)
    
if __name__ == "__main__":
    main()
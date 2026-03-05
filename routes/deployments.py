from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body, status

from common.models import Deployment, Status
from db import system_manager

router = APIRouter(prefix="/deployments")

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_deployment(deployment: Deployment):
    system_manager.create_deployment(deployment)
    return {"id": deployment.id}

@router.get('/{deployment_id}', status_code=status.HTTP_200_OK)    
def get_deployment(deployment_id: UUID):
    return system_manager.get_deployment(deployment_id)
    
@router.put('/{deployment_id}', status_code=status.HTTP_200_OK)    
def update_deployment(deployment_id: UUID, db_name: Annotated[str, Body()]):
    system_manager.update_deployment(deployment_id, db_name)
    return {"db_name": db_name}
    
@router.delete('/{deplotment_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_deployment(deployment_id: UUID):
    system_manager.delete_deployment(deployment_id)
    
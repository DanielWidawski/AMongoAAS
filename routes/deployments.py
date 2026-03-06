import secrets
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from common.models import Deployment, Status
from db import system_manager

router = APIRouter(prefix="/deployments")

security = HTTPBasic()

def validate_username(deployment_id: UUID, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    current_username_bytes = credentials.username.encode("utf8")
    deployment_username = system_manager.get_deployment(deployment_id).username
    correct_username_bytes = deployment_username.encode("utf-8")
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    if not (is_correct_username):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username",
            headers={"WWW-Authenticate": "Basic"},
        )
    return deployment_id
    


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_deployment(deployment: Deployment):
    system_manager.create_deployment(deployment)
    return {"id": deployment.id}

@router.get('/{deployment_id}', status_code=status.HTTP_200_OK)    
def get_deployment(deployment_id: Annotated[UUID, Depends(validate_username)]):
    return system_manager.get_deployment(deployment_id)
    
@router.put('/{deployment_id}', status_code=status.HTTP_200_OK)    
def update_deployment(deployment_id: Annotated[UUID, Depends(validate_username)], db_name: Annotated[str, Body()]):
    system_manager.update_deployment(deployment_id, db_name)
    return {"db_name": db_name}
    
@router.delete('/{deplotment_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_deployment(deployment_id: Annotated[UUID, Depends(validate_username)]):
    system_manager.delete_deployment(deployment_id)
    
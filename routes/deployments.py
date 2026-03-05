from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body

from common.models import Deployment
from db import system_manager

router = APIRouter("/deployments")


def create_deployment(deployment: Deployment):
    system_manager.create_deployment(deployment)
    
def get_deployment(deployment_id: UUID):
    system_manager.get_deployment(deployment_id)
    
def update_deployment(deployment_id: UUID, db_name: Annotated[str, Body()]):
    system_manager.update_deployment(deployment_id, db_name)
    
def delete_deployment(deployment_id: UUID):
    system_manager.delete_deployment(deployment_id)
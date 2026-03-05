from uuid import UUID

from fastapi import APIRouter

router = APIRouter("/deployments")


def create_deployment():
    .create_deployment()
    
def get_deployment(deployment_id: UUID):
    ...
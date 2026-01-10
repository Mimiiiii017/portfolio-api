from fastapi import APIRouter, HTTPException, Depends
from src.db import projects_collection
from src.auth import verify_api_key

router = APIRouter(
    dependencies=[Depends(verify_api_key)]
)

@router.get("/")
async def get_projects():
    projects = []

    cursor = projects_collection.find({})

    async for project in cursor:
        project["_id"] = str(project["_id"])
        projects.append(project)

    return projects


@router.get("/{slug}")
async def get_project(slug: str):
    project = await projects_collection.find_one({"slug": slug})

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project["_id"] = str(project["_id"])
    return project

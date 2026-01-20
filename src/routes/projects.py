import cloudinary
import cloudinary.uploader
from fastapi import APIRouter, HTTPException, Depends
from src.db import projects_collection
from src.auth import verify_api_key
from typing import List, Dict
import os

# Cloudinary configuration (if necessary for any future interactions)
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

router = APIRouter(
    dependencies=[Depends(verify_api_key)]
)

# Fetch all projects
@router.get("/")
async def get_projects():
    projects = []

    cursor = projects_collection.find({})

    async for project in cursor:
        project["_id"] = str(project["_id"])  # Convert ObjectId to string
        # Add Cloudinary image URL to the project response
        if "image_url" in project:
            project["image_url"] = project["image_url"]
        projects.append(project)

    return projects

# Fetch a specific project by slug
@router.get("/{slug}")
async def get_project(slug: str):
    project = await projects_collection.find_one({"slug": slug})

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project["_id"] = str(project["_id"])  # Convert ObjectId to string
    # Add Cloudinary image URL to the project response
    if "image_url" in project:
        project["image_url"] = project["image_url"]

    return project

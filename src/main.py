from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.projects import router as projects_router
import cloudinary
import cloudinary.uploader
import os

app = FastAPI(title="Portfolio API")

#CORS (allows your frontend to call this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(projects_router, prefix="/projects")

@app.get("/")
def root():
    return {"status": "API is running"}


cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

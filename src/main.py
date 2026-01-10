from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.projects import router as projects_router

app = FastAPI(title="Portfolio API")

# CORS (allow your frontend to call this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later you can restrict this
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(projects_router, prefix="/projects")

@app.get("/")
def root():
    return {"status": "API is running"}

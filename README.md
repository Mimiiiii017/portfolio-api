# Portfolio API

A FastAPI-based backend API that powers my personal portfolio website.  
The API serves project data stored in MongoDB and is secured using an API key.

This repository demonstrates real-world backend practices including:
- Environment-based configuration
- Secure MongoDB connections
- API key protection
- Cloud deployment readiness

---

## Features

- FastAPI backend
- MongoDB Atlas integration
- API key–protected endpoints
- Clean project-based routing
- Ready for deployment on Render

---

## Tech Stack

- **Python**
- **FastAPI**
- **MongoDB Atlas**
- **Motor (async MongoDB driver)**
- **python-dotenv**
- **Uvicorn**

---

## Security

This API uses an API key passed via request headers.

All sensitive values are stored as environment variables:
- `MONGODB_URI`
- `API_KEY`

These are **NOT included in the repository** and must be provided at runtime.
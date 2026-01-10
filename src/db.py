import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
#for future mireya: do not forget these 2 lines as you need them to load env variables from .env file
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise RuntimeError("MONGODB_URI not set")

client = AsyncIOMotorClient(MONGODB_URI)

db = client["Projects"]
projects_collection = db["Projects"]
#FOR FUTURE MIREYA
#Mongo DB is case sensitive. Make sure to match the exact casing of your database and collection names. 

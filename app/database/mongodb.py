from motor.motor_asyncio import AsyncIOMotorClient
from app.config import  DB_NAME
import os

client = None
db = None

async def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
    db = client[DB_NAME]
    print("Connected to MongoDB")

# Export db for use in services
def get_db():
    if db is None:
        raise RuntimeError("Database connection not established")
    return db


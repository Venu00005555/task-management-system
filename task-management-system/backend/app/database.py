import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB connection configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/taskdb")
DB_NAME = os.getenv("DB_NAME", "taskdb")

# Initialize async MongoDB client
client = AsyncIOMotorClient(MONGO_URI)

# Access database
db = client[DB_NAME]

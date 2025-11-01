from bson import ObjectId
from passlib.context import CryptContext

from .database import db

# Password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# -------------------- USER FUNCTIONS -------------------- #

async def get_user_by_email(email: str):
    """Retrieve a user document by email."""
    return await db["users"].find_one({"email": email})


async def create_user(user_data: dict):
    """Create a new user with a hashed password."""
    user_data["hashed_password"] = pwd_context.hash(user_data.pop("password"))
    result = await db["users"].insert_one(user_data)
    return await db["users"].find_one({"_id": result.inserted_id})


async def verify_user(email: str, password: str):
    """Verify user credentials (email and password)."""
    user = await get_user_by_email(email)
    if not user:
        return None

    if not pwd_context.verify(password, user["hashed_password"]):
        return None

    return user

# -------------------- TASK FUNCTIONS -------------------- #

async def create_task(owner_id: ObjectId, task_data: dict):
    """Create a new task for the given user."""
    task_data["owner_id"] = ObjectId(owner_id)
    result = await db["tasks"].insert_one(task_data)
    return await db["tasks"].find_one({"_id": result.inserted_id})


async def get_tasks_for_user(owner_id: ObjectId):
    """Fetch all tasks belonging to a specific user."""
    cursor = db["tasks"].find({"owner_id": ObjectId(owner_id)})
    return await cursor.to_list(length=100)


async def update_task(task_id: ObjectId, owner_id: ObjectId, updates: dict):
    """Update a specific task owned by the user."""
    result = await db["tasks"].update_one(
        {"_id": ObjectId(task_id), "owner_id": ObjectId(owner_id)},
        {"$set": updates}
    )
    return result.modified_count


async def delete_task(task_id: ObjectId, owner_id: ObjectId):
    """Delete a specific task owned by the user."""
    result = await db["tasks"].delete_one(
        {"_id": ObjectId(task_id), "owner_id": ObjectId(owner_id)}
    )
    return result.deleted_count

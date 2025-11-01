from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr


# -------------------- CUSTOM OBJECTID HANDLER -------------------- #
class PyObjectId(ObjectId):
    """Custom validator for MongoDB ObjectId fields in Pydantic models."""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


# -------------------- USER MODELS -------------------- #
class UserCreate(BaseModel):
    """Schema for creating a new user."""
    email: EmailStr
    password: str
    full_name: Optional[str] = None


class UserInDB(BaseModel):
    """Schema representing a user stored in the database."""
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr
    hashed_password: str
    full_name: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}


# -------------------- AUTH TOKEN MODEL -------------------- #
class Token(BaseModel):
    """Schema for JWT authentication token."""
    access_token: str
    token_type: str = "bearer"


# -------------------- TASK MODELS -------------------- #
class TaskCreate(BaseModel):
    """Schema for creating a new task."""
    title: str
    description: Optional[str] = ""
    completed: bool = False


class TaskInDB(TaskCreate):
    """Schema representing a task stored in the database."""
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    owner_id: PyObjectId

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId

from ..auth import get_current_user
from ..models import TaskCreate, TaskInDB
from ..crud import create_task, get_tasks_for_user, update_task, delete_task

router = APIRouter()

@router.post("/", response_model=TaskInDB, status_code=status.HTTP_201_CREATED)
async def create_new_task(
    task: TaskCreate,
    current_user=Depends(get_current_user)
):
    """Create a new task for the authenticated user."""
    new_task = await create_task(current_user["_id"], task.dict())
    return new_task


@router.get("/", response_model=list[TaskInDB])
async def list_tasks(current_user=Depends(get_current_user)):
    """Retrieve all tasks belonging to the authenticated user."""
    return await get_tasks_for_user(current_user["_id"])


@router.put("/{task_id}", response_model=dict)
async def update_existing_task(
    task_id: str,
    updates: dict,
    current_user=Depends(get_current_user)
):
    """Update an existing task for the authenticated user."""
    updated = await update_task(ObjectId(task_id), current_user["_id"], updates)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return {"status": "ok"}


@router.delete("/{task_id}", response_model=dict)
async def delete_existing_task(
    task_id: str,
    current_user=Depends(get_current_user)
):
    """Delete an existing task for the authenticated user."""
    deleted = await delete_task(ObjectId(task_id), current_user["_id"])
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return {"status": "ok"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, tasks
import os

# -------------------- APP INITIALIZATION -------------------- #
app = FastAPI(title="Task Management System - FastAPI")

# -------------------- MIDDLEWARE CONFIGURATION -------------------- #
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (can restrict for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- ROUTERS -------------------- #
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"])

# -------------------- ROOT ROUTE -------------------- #
@app.get("/")
def read_root():
    return {"message": "Task Management System API is running 🚀"}

from fastapi import FastAPI, Header, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

app = FastAPI()

API_KEY = "reqres-free-v1"

# Pydantic v2: обязательно указываем model_config
class UserCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str
    job: str

class UserPatch(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: Optional[str] = None
    job: Optional[str] = None

# Простое хранилище пользователей
users = {}
next_id = 1

def check_api_key(x_api_key: Optional[str]):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")

@app.post("/api/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, x_api_key: Optional[str] = Header(None)):
    check_api_key(x_api_key)
    global next_id
    created_at = datetime.utcnow().isoformat() + "Z"
    user_id = next_id
    next_id += 1
    users[user_id] = {
        "name": user.name,
        "job": user.job,
        "id": str(user_id),
        "createdAt": created_at
    }
    return users[user_id]

@app.put("/api/users/{user_id}")
async def update_user_put(user_id: int, user: UserCreate, x_api_key: Optional[str] = Header(None)):
    check_api_key(x_api_key)
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    updated_at = datetime.utcnow().isoformat() + "Z"
    users[user_id].update({
        "name": user.name,
        "job": user.job,
        "updatedAt": updated_at
    })
    return {
        "name": user.name,
        "job": user.job,
        "updatedAt": updated_at
    }

@app.patch("/api/users/{user_id}")
async def update_user_patch(user_id: int, user: UserPatch, x_api_key: Optional[str] = Header(None)):
    check_api_key(x_api_key)
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    updated_at = datetime.utcnow().isoformat() + "Z"
    if user.name is not None:
        users[user_id]["name"] = user.name
    if user.job is not None:
        users[user_id]["job"] = user.job
    users[user_id]["updatedAt"] = updated_at
    response = {}
    if user.name is not None:
        response["name"] = user.name
    if user.job is not None:
        response["job"] = user.job
    response["updatedAt"] = updated_at
    return response

@app.delete("/api/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, x_api_key: Optional[str] = Header(None)):
    check_api_key(x_api_key)
    users.pop(user_id, None)  # удаляем, если есть, иначе ничего
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)
from fastapi import FastAPI, HTTPException, Query
from typing import List
from pydantic import BaseModel
from data import users


app = FastAPI()


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UserResponse(BaseModel):
    data: User


class UsersListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]


@app.get("/api/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int) -> UserResponse:
    user_dict = users.get(user_id)
    if user_dict is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = User(**user_dict)
    return UserResponse(data=user)


@app.get("/api/users", response_model=UsersListResponse)
def list_users(page: int = Query(1, ge=1)) -> UsersListResponse:
    per_page: int = 3
    total_users: int = len(users)
    total_pages: int = (total_users + per_page - 1) // per_page

    if page > total_pages and total_users > 0:
        return UsersListResponse(
            page=page,
            per_page=per_page,
            total=total_users,
            total_pages=total_pages,
            data=[]
        )

    start: int = (page - 1) * per_page
    end: int = start + per_page

    user_list = [User(**u) for u in list(users.values())[start:end]]

    return UsersListResponse(
        page=page,
        per_page=per_page,
        total=total_users,
        total_pages=total_pages,
        data=user_list
    )


"""
Admin Routes — Knowledge base, user management, dashboard
Issue #7 (徐心铭)
"""
from fastapi import APIRouter

router = APIRouter()


# --- Exercise CRUD ---
@router.get("/exercises")
async def list_exercises():
    """获取知识库动作列表"""
    return {"exercises": []}


@router.post("/exercises")
async def create_exercise():
    """新增动作条目"""
    return {"message": "Create — to be implemented"}


# --- User Management ---
@router.get("/users")
async def list_users():
    """用户列表"""
    return {"users": [], "stats": {"total": 0, "today_active": 0, "new_this_week": 0}}


# --- Dashboard ---
@router.get("/dashboard")
async def dashboard():
    """系统仪表盘"""
    return {
        "total_users": 0,
        "today_active": 0,
        "weekly_corrections": 0,
        "knowledge_entries": 0,
    }
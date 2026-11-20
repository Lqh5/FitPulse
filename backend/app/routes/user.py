"""
User Routes — Profile & stats
Issue #7 (徐心铭)
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/user/profile")
async def get_profile():
    """获取用户信息"""
    # TODO: Implement JWT auth, DB lookup
    return {"message": "User profile — to be implemented by #7"}


@router.patch("/user/profile")
async def update_profile():
    """更新用户信息"""
    # TODO: Implement
    return {"message": "Update profile — to be implemented by #7"}


@router.get("/user/stats")
async def get_stats():
    """获取用户训练统计"""
    # TODO: Implement
    return {"weekly_days": 0, "total_sessions": 0, "total_hours": 0, "total_kcal": 0}
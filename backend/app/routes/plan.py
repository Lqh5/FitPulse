"""
Plan Routes — Training plan generation & management
Issue #7 (徐心铭)
"""
from fastapi import APIRouter

router = APIRouter()


@router.post("/plan/generate")
async def generate_plan():
    """生成训练计划"""
    # TODO: Implement
    return {"message": "Generate plan — to be implemented by #7"}


@router.get("/plan/{plan_id}")
async def get_plan(plan_id: str):
    """获取训练计划详情"""
    # TODO: Implement
    return {"plan_id": plan_id}


@router.patch("/plan/{plan_id}/day/{day_index}/toggle")
async def toggle_day(plan_id: str, day_index: int):
    """标记/取消训练日完成"""
    # TODO: Implement
    return {"plan_id": plan_id, "day_index": day_index}
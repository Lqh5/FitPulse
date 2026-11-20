"""
Correction Routes — Posture analysis via photo upload
Issue #7 (徐心铭) + #9 (林祺皓)
"""
from fastapi import APIRouter

router = APIRouter()


@router.post("/correction")
async def analyze_posture():
    """上传照片 → 姿态分析"""
    # TODO: Implement Claude Vision + RAG comparison
    return {"message": "Posture correction — to be implemented by #7 + #9"}


@router.get("/correction/history")
async def correction_history():
    """纠姿历史记录"""
    # TODO: Implement
    return {"history": []}
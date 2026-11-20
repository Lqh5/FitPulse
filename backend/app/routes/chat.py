"""
Chat Routes — AI Coach conversation (SSE streaming)
Issue #7 (徐心铭) + #9 (林祺皓)
"""
from fastapi import APIRouter

router = APIRouter()


@router.post("/chat")
async def chat():
    """
    AI 对话接口（SSE 流式返回）

    Request: { "message": "...", "session_id": "uuid" }
    Response: Server-Sent Events stream
    """
    # TODO: Implement agent orchestration
    return {"message": "Chat endpoint — to be implemented by #7 + #9"}
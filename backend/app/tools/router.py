"""
Intent Router — Determine which tool to invoke based on user input
Issue #9 (林祺皓)

Priority:
1. Image upload → posture_correction
2. Keyword match → specific tool
3. LLM function-calling fallback
"""
from typing import Optional, Tuple

# Keyword → tool mapping
KEYWORD_ROUTES = {
    "动作": "query_exercise",
    "怎么练": "query_exercise",
    "标准": "query_exercise",
    "计划": "generate_plan",
    "训练计划": "generate_plan",
    "帮我安排": "generate_plan",
    "纠姿": "correct_posture",
    "纠正": "correct_posture",
    "姿势": "correct_posture",
    "进度": "get_progress",
    "统计": "get_progress",
}


def route_intent(message: str, has_image: bool = False) -> Tuple[str, str]:
    """
    Route user intent to the appropriate tool.

    Returns: (tool_name, routing_method)
        routing_method: "image", "keyword", or "llm_fallback"
    """
    # Priority 1: Image → posture correction
    if has_image:
        return "correct_posture", "image"

    # Priority 2: Keyword match
    for keyword, tool in KEYWORD_ROUTES.items():
        if keyword in message:
            return tool, "keyword"

    # Priority 3: LLM function-calling fallback
    return "llm_fallback", "llm_fallback"


def get_tool_for_intent(tool_name: str, tools: dict):
    """Get tool instance by name."""
    return tools.get(tool_name)
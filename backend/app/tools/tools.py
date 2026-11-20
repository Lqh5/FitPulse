"""
LangChain Tool Definitions — Agent tool set
Issue #9 (林祺皓)

Three core tools:
1. query_exercise — RAG-powered exercise lookup
2. generate_plan — Rule engine + LLM plan generation
3. correct_posture — Claude Vision posture analysis
"""
from langchain.tools import tool
from pydantic import BaseModel, Field
from typing import List, Optional


# ============================================================
# Tool 1: query_exercise
# ============================================================
class QueryExerciseInput(BaseModel):
    query: str = Field(description="User's natural language query about an exercise")
    difficulty: Optional[str] = Field(default=None, description="Filter: beginner / intermediate / advanced")
    equipment: Optional[List[str]] = Field(default=None, description="Filter: available equipment list")


@tool("query_exercise", args_schema=QueryExerciseInput)
def query_exercise(query: str, difficulty: Optional[str] = None, equipment: Optional[List[str]] = None) -> str:
    """
    Search the exercise knowledge base via RAG.
    Returns structured exercise card with form cues, breathing, common errors, and source citation.

    TODO: #6 马锦城 — integrate Chroma RAG pipeline
    """
    # Placeholder — will call RAG service
    return f"Exercise query received: {query}"


# ============================================================
# Tool 2: generate_plan
# ============================================================
class GeneratePlanInput(BaseModel):
    goal: str = Field(description="Fitness goal: lose_weight / build_muscle / stay_fit")
    level: str = Field(description="Fitness level: beginner / intermediate / advanced")
    weekly_days: int = Field(description="Training days per week, 1-7")
    equipment: List[str] = Field(description="Available equipment list")


@tool("generate_plan", args_schema=GeneratePlanInput)
def generate_plan(goal: str, level: str, weekly_days: int, equipment: List[str]) -> str:
    """
    Generate a structured weekly training plan.
    Uses rule engine for split programming, RAG for exercise selection, LLM for polish.

    TODO: #9 林祺皓 — implement rule engine + LLM integration
    """
    # Placeholder
    return f"Plan generation — {goal}, {level}, {weekly_days}d/week, equipment: {equipment}"


# ============================================================
# Tool 3: correct_posture
# ============================================================
class CorrectPostureInput(BaseModel):
    photo_url: str = Field(description="URL of the uploaded exercise photo")
    exercise_name: Optional[str] = Field(default=None, description="Name of the exercise being performed")


@tool("correct_posture", args_schema=CorrectPostureInput)
def correct_posture(photo_url: str, exercise_name: Optional[str] = None) -> str:
    """
    Analyze exercise posture from a photo using Claude Vision.
    Compares against RAG knowledge base and returns structured correction report.

    TODO: #9 林祺皓 — implement Claude Vision + RAG comparison
    """
    # Placeholder
    return f"Posture correction — photo: {photo_url}, exercise: {exercise_name}"


# ============================================================
# Tool 4: get_progress (query tool)
# ============================================================
class GetProgressInput(BaseModel):
    days: int = Field(default=7, description="Number of days to look back")


@tool("get_progress", args_schema=GetProgressInput)
def get_progress(days: int = 7) -> str:
    """
    Get user's recent training progress stats.

    TODO: #7 徐心铭 — implement DB query
    """
    return f"Progress for last {days} days"


# --- Tool registry ---
ALL_TOOLS = [query_exercise, generate_plan, correct_posture, get_progress]

# Tool to RAG dependency mapping
TOOL_RAG_DEPS = {
    "query_exercise": ["standard_action"],
    "generate_plan": ["standard_action", "muscle_activation"],
    "correct_posture": ["standard_action", "error_harm"],
    "get_progress": [],
}
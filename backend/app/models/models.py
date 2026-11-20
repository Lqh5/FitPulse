"""
FitPulse SQLAlchemy ORM Models
Implements the 13-table schema defined in schema.sql
"""
import uuid
from datetime import datetime
from sqlalchemy import (
    Column, String, Integer, Text, Boolean, Date, DateTime,
    Enum, JSON, ForeignKey, UniqueConstraint, Index, create_engine
)
from sqlalchemy.dialects.mysql import CHAR, TINYINT
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


def gen_uuid():
    return str(uuid.uuid4())


# ============================================================
# 1. User
# ============================================================
class User(Base):
    __tablename__ = "users"

    id = Column(CHAR(36), primary_key=True, default=gen_uuid)
    nickname = Column(String(50), nullable=False)
    avatar_url = Column(String(255), default="")
    level = Column(Enum("beginner", "intermediate", "advanced"), default="beginner")
    goal = Column(Enum("lose_weight", "build_muscle", "stay_fit"), default="stay_fit")
    equipment = Column(JSON)
    weekly_days = Column(Integer, default=3)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    training_plans = relationship("TrainingPlan", back_populates="user", cascade="all, delete-orphan")
    posture_corrections = relationship("PostureCorrection", back_populates="user", cascade="all, delete-orphan")
    agent_sessions = relationship("AgentSession", back_populates="user", cascade="all, delete-orphan")
    workout_records = relationship("WorkoutRecord", back_populates="user", cascade="all, delete-orphan")
    feedbacks = relationship("Feedback", back_populates="user", cascade="all, delete-orphan")


# ============================================================
# 2. Exercise
# ============================================================
class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(CHAR(36), primary_key=True, default=gen_uuid)
    name = Column(String(100), nullable=False)
    module = Column(Enum("standard_action", "muscle_activation", "error_harm"), nullable=False)
    target_muscles = Column(JSON)
    difficulty = Column(Enum("beginner", "intermediate", "advanced"), default="beginner")
    equipment_needed = Column(JSON)
    description = Column(Text)
    form_cues = Column(Text)
    breathing = Column(Text)
    common_errors = Column(Text)
    image_urls = Column(JSON)
    video_url = Column(String(255), default="")
    tags = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        Index("idx_exercises_module", "module"),
        Index("idx_exercises_difficulty", "difficulty"),
    )


# ============================================================
# 3. KnowledgeChunk
# ============================================================
class KnowledgeChunk(Base):
    __tablename__ = "knowledge_chunks"

    id = Column(CHAR(36), primary_key=True, default=gen_uuid)
    chunk_id = Column(String(100), nullable=False, unique=True)
    module = Column(Enum("standard_action", "muscle_activation", "error_harm"), nullable=False)
    exercise_id = Column(CHAR(36), ForeignKey("exercises.id", ondelete="SET NULL"))
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    tags = Column(JSON)
    source = Column(String(255), default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        Index("idx_kc_module", "module"),
        Index("idx_kc_chunk_id", "chunk_id"),
    )


# ============================================================
# 4. TrainingPlan
# ============================================================
class TrainingPlan(Base):
    __tablename__ = "training_plans"

    id = Column(CHAR(36), primary_key=True, default=gen_uuid)
    user_id = Column(CHAR(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    week_start = Column(Date, nullable=False)
    status = Column(Enum("active", "completed", "abandoned"), default="active")
    created_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (UniqueConstraint("user_id", "week_start", name="uk_user_week"),)

    user = relationship("User", back_populates="training_plans")
    plan_days = relationship("PlanDay", back_populates="plan", cascade="all, delete-orphan")


# ============================================================
# 5. PlanDay
# ============================================================
class PlanDay(Base):
    __tablename__ = "plan_days"

    id = Column(CHAR(36), primary_key=True, default=gen_uuid)
    plan_id = Column(CHAR(36), ForeignKey("training_plans.id", ondelete="CASCADE"), nullable=False)
    day_index = Column(Integer, nullable=False)
    focus = Column(String(100), default="")
    estimated_minutes = Column(Integer, default=45)
    is_completed = Column(Boolean, default=False)

    __table_args__ = (UniqueConstraint("plan_id", "day_index", name="uk_plan_day"),)

    plan = relationship("TrainingPlan", back_populates="plan_days")
    exercises = relationship("PlanExercise", back_populates="day", cascade="all, delete-orphan")


# ============================================================
# 6. PlanExercise
# ============================================================
class PlanExercise(Base):
    __tablename__ = "plan_exercises"

    id = Column(CHAR(36), primary_key=True, default=gen_uuid)
    day_id = Column(CHAR(36), ForeignKey("plan_days.id", ondelete="CASCADE"), nullable=False)
    exercise_id = Column(CHAR(36), ForeignKey("exercises.id", ondelete="RESTRICT"), nullable=False)
    sets = Column(Integer, default=3)
    reps = Column(Integer, default=12)
    rest_seconds = Column(Integer, default=60)
    sort_order = Column(Integer, default=0)

    day = relationship("PlanDay", back_populates="exercises")


# ============================================================
# 7. PostureCorrection
# ============================================================
class PostureCorrection(Base):
    __tablename__ = "posture_corrections"

    id = Column(CHAR(36), primary_key=True, default=gen_uuid)
    user_id = Column(CHAR(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    photo_url = Column(String(255), nullable=False)
    overall_assessment = Column(Text)
    safety_note = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="posture_corrections")
    issues = relationship("CorrectionIssue", back_populates="correction", cascade="all, delete-orphan")


# ============================================================
# 8. CorrectionIssue
# ============================================================
class CorrectionIssue(Base):
    __tablename__ = "correction_issues"

    id = Column(CHAR(36), primary_key=True, default=gen_uuid)
    correction_id = Column(CHAR(36), ForeignKey("posture_corrections.id", ondelete="CASCADE"), nullable=False)
    body_part = Column(String(50), nullable=False)
    severity = Column(Enum("mild", "moderate", "severe"), default="moderate")
    problem = Column(Text, nullable=False)
    correction = Column(Text, nullable=False)

    correction = relationship("PostureCorrection", back_populates="issues")


# ============================================================
# 9. AgentSession
# ============================================================
class AgentSession(Base):
    __tablename__ = "agent_sessions"

    id = Column(CHAR(36), primary_key=True, default=gen_uuid)
    user_id = Column(CHAR(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    task_type = Column(String(50), default="")
    context = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="agent_sessions")
    messages = relationship("Message", back_populates="session", cascade="all, delete-orphan")


# ============================================================
# 10. Message
# ============================================================
class Message(Base):
    __tablename__ = "messages"

    id = Column(CHAR(36), primary_key=True, default=gen_uuid)
    session_id = Column(CHAR(36), ForeignKey("agent_sessions.id", ondelete="CASCADE"), nullable=False)
    role = Column(Enum("user", "assistant", "system", "tool"), nullable=False)
    content = Column(Text, nullable=False)
    metadata = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

    session = relationship("AgentSession", back_populates="messages")
    tool_calls = relationship("ToolCall", back_populates="message", cascade="all, delete-orphan")


# ============================================================
# 11. ToolCall
# ============================================================
class ToolCall(Base):
    __tablename__ = "tool_calls"

    id = Column(CHAR(36), primary_key=True, default=gen_uuid)
    message_id = Column(CHAR(36), ForeignKey("messages.id", ondelete="CASCADE"), nullable=False)
    tool_name = Column(String(100), nullable=False)
    args = Column(JSON)
    result = Column(JSON)

    message = relationship("Message", back_populates="tool_calls")


# ============================================================
# 12. WorkoutRecord
# ============================================================
class WorkoutRecord(Base):
    __tablename__ = "workout_records"

    id = Column(CHAR(36), primary_key=True, default=gen_uuid)
    user_id = Column(CHAR(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    plan_id = Column(CHAR(36), ForeignKey("training_plans.id", ondelete="SET NULL"))
    completed_at = Column(DateTime, default=datetime.utcnow)
    duration_minutes = Column(Integer, default=0)
    difficulty_rating = Column(TINYINT, default=3)
    notes = Column(Text)

    user = relationship("User", back_populates="workout_records")


# ============================================================
# 13. Feedback
# ============================================================
class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(CHAR(36), primary_key=True, default=gen_uuid)
    user_id = Column(CHAR(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    category = Column(String(50), default="")
    status = Column(Enum("pending", "processing", "resolved"), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="feedbacks")


# ============================================================
# Database helper
# ============================================================
def init_db(database_url: str):
    """Create all tables."""
    engine = create_engine(database_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal
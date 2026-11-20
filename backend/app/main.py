"""
FitPulse Backend — FastAPI Application Entry Point
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes import chat, plan, correction, user, admin


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup / shutdown events."""
    yield


app = FastAPI(
    title="FitPulse API",
    description="AI-powered virtual fitness coach",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Register Routers ---
app.include_router(chat.router, prefix="/api/v1", tags=["Chat"])
app.include_router(plan.router, prefix="/api/v1", tags=["Plan"])
app.include_router(correction.router, prefix="/api/v1", tags=["Correction"])
app.include_router(user.router, prefix="/api/v1", tags=["User"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["Admin"])


@app.get("/")
def root():
    return {"service": "FitPulse API", "version": "0.1.0"}


@app.get("/health")
def health():
    return {"status": "ok"}
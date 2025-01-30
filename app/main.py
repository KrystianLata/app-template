from fastapi import FastAPI
from app.api.v1.router import router as api_v1_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, version="1.0.0", description="FastAPI project template"
)

# Include routers
app.include_router(api_v1_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI template"}

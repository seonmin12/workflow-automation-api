from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, engine
from app.models import work_request
from app.routers.work_request_router import router as work_request_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="WorkFlow Automation API",
    description="FastAPI based internal workflow request automation system.",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(work_request_router)


@app.get("/", tags=["Health"])
def read_root() -> dict[str, str]:
    return {
        "service": "WorkFlow Automation API",
        "status": "running",
    }

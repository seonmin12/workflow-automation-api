from fastapi import FastAPI

app = FastAPI(
    title="WorkFlow Automation API",
    description="FastAPI based internal workflow request automation system.",
    version="0.1.0",
)


@app.get("/", tags=["Health"])
def read_root() -> dict[str, str]:
    return {
        "service": "WorkFlow Automation API",
        "status": "running",
    }

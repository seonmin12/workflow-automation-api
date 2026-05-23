from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class Department(str, Enum):
    MARKETING = "MARKETING"
    LOGISTICS = "LOGISTICS"
    CS = "CS"
    FINANCE = "FINANCE"
    HR = "HR"


class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    URGENT = "URGENT"


class RequestStatus(str, Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"


class WorkRequestCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    requester: str = Field(..., min_length=1, max_length=100)
    department: Department
    priority: Priority


class WorkRequestStatusUpdate(BaseModel):
    status: RequestStatus


class WorkRequestResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    requester: str
    department: Department
    priority: Priority
    status: RequestStatus
    created_at: datetime
    updated_at: datetime

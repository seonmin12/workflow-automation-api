from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.work_request_schema import (
    Department,
    RequestStatus,
    WorkRequestCreate,
    WorkRequestResponse,
    WorkRequestStatusUpdate,
)
from app.services import work_request_service

router = APIRouter(prefix="/api/requests", tags=["Work Requests"])


@router.post(
    "",
    response_model=WorkRequestResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_work_request(
    request: WorkRequestCreate,
    db: Session = Depends(get_db),
) -> WorkRequestResponse:
    return work_request_service.create_request(db, request)


@router.get("", response_model=list[WorkRequestResponse])
def get_work_requests(
    department: Department | None = None,
    status: RequestStatus | None = None,
    db: Session = Depends(get_db),
) -> list[WorkRequestResponse]:
    return work_request_service.get_requests(db, department, status)


@router.get("/{request_id}", response_model=WorkRequestResponse)
def get_work_request(
    request_id: int,
    db: Session = Depends(get_db),
) -> WorkRequestResponse:
    return work_request_service.get_request(db, request_id)


@router.patch("/{request_id}/status", response_model=WorkRequestResponse)
def update_work_request_status(
    request_id: int,
    request: WorkRequestStatusUpdate,
    db: Session = Depends(get_db),
) -> WorkRequestResponse:
    return work_request_service.update_status(db, request_id, request.status)

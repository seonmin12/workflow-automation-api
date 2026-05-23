from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.work_request import WorkRequest
from app.repositories import work_request_repository
from app.schemas.work_request_schema import (
    Department,
    RequestStatus,
    WorkRequestCreate,
    WorkRequestUpdate,
)

ALLOWED_STATUS_TRANSITIONS = {
    RequestStatus.PENDING: {RequestStatus.IN_PROGRESS, RequestStatus.REJECTED},
    RequestStatus.IN_PROGRESS: {RequestStatus.COMPLETED, RequestStatus.REJECTED},
    RequestStatus.COMPLETED: set(),
    RequestStatus.REJECTED: set(),
}


def create_request(db: Session, request: WorkRequestCreate) -> WorkRequest:
    return work_request_repository.create_work_request(db, request)


def get_requests(
    db: Session,
    department: Department | None = None,
    status_filter: RequestStatus | None = None,
) -> list[WorkRequest]:
    return work_request_repository.find_work_requests(db, department, status_filter)


def get_request(db: Session, request_id: int) -> WorkRequest:
    work_request = work_request_repository.find_work_request_by_id(db, request_id)
    if work_request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Work request not found.",
        )
    return work_request


def update_status(
    db: Session,
    request_id: int,
    new_status: RequestStatus,
) -> WorkRequest:
    work_request = get_request(db, request_id)
    current_status = RequestStatus(work_request.status)

    if current_status == new_status:
        return work_request

    allowed_next_statuses = ALLOWED_STATUS_TRANSITIONS[current_status]
    if new_status not in allowed_next_statuses:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                f"Invalid status transition: {current_status.value} "
                f"to {new_status.value}."
            ),
        )

    return work_request_repository.update_work_request_status(
        db,
        work_request,
        new_status,
    )


def update_request(
    db: Session,
    request_id: int,
    request: WorkRequestUpdate,
) -> WorkRequest:
    work_request = get_request(db, request_id)
    return work_request_repository.update_work_request(db, work_request, request)


def delete_request(db: Session, request_id: int) -> None:
    work_request = get_request(db, request_id)
    work_request_repository.delete_work_request(db, work_request)

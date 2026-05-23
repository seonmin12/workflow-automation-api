from sqlalchemy.orm import Session

from app.models.work_request import WorkRequest
from app.schemas.work_request_schema import (
    Department,
    RequestStatus,
    WorkRequestCreate,
)


def create_work_request(db: Session, request: WorkRequestCreate) -> WorkRequest:
    work_request = WorkRequest(
        title=request.title,
        description=request.description,
        requester=request.requester,
        department=request.department.value,
        priority=request.priority.value,
        status=RequestStatus.PENDING.value,
    )
    db.add(work_request)
    db.commit()
    db.refresh(work_request)
    return work_request


def find_work_requests(
    db: Session,
    department: Department | None = None,
    status: RequestStatus | None = None,
) -> list[WorkRequest]:
    query = db.query(WorkRequest)

    if department is not None:
        query = query.filter(WorkRequest.department == department.value)

    if status is not None:
        query = query.filter(WorkRequest.status == status.value)

    return query.order_by(WorkRequest.id.desc()).all()


def find_work_request_by_id(db: Session, request_id: int) -> WorkRequest | None:
    return db.query(WorkRequest).filter(WorkRequest.id == request_id).first()


def update_work_request_status(
    db: Session,
    work_request: WorkRequest,
    status: RequestStatus,
) -> WorkRequest:
    work_request.status = status.value
    db.commit()
    db.refresh(work_request)
    return work_request

# WorkFlow Automation API

FastAPI 기반 사내 업무 요청 자동화 API입니다.  
마케팅/운영 조직에서 반복적으로 발생하는 업무 요청을 등록하고, 담당 부서와 처리 상태에 따라 조회 및 관리할 수 있도록 설계했습니다.
본 프로젝트는 Python 백엔드 프레임워크인 FastAPI의 구조를 이해하고, RESTful API 설계, MySQL 연동, Swagger 문서화, 계층 분리 구조를 학습하기 위해 진행한 미니 프로젝트입니다.

## Overview

메신저, 문서, 구두 요청으로 분산되기 쉬운 반복 업무 요청을 하나의 API 흐름으로 구조화한 내부 운영 시스템 컨셉의 프로젝트입니다.

- 업무 요청 등록
- 업무 요청 목록 및 상세 조회
- 부서별 조회
- 상태별 조회
- 요청 상태 변경
- 업무 요청 수정 및 삭제
- Swagger 기반 API 문서화
- 간단한 내부 업무 요청 관리 화면
- MySQL 연동

## Tech Stack

- Python
- FastAPI
- MySQL
- SQLAlchemy
- Pydantic
- Swagger UI

## Project Structure

```text
workflow-automation-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   └── work_request.py
│   ├── schemas/
│   │   └── work_request_schema.py
│   ├── repositories/
│   │   └── work_request_repository.py
│   ├── services/
│   │   └── work_request_service.py
│   └── routers/
│       ├── dashboard_router.py
│       └── work_request_router.py
├── sql/
│   └── schema.sql
├── requirements.txt
├── .env.example
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
```

`.env.example`을 참고해 `.env` 파일을 설정합니다.

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=workflow_db
```

MySQL 데이터베이스를 생성합니다.

```sql
CREATE DATABASE workflow_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

서버를 실행합니다.

```bash
uvicorn app.main:app --reload
```

- API Health Check: `http://localhost:8000/`
- Swagger UI: `http://localhost:8000/docs`
- Dashboard: `http://localhost:8000/dashboard`

Swagger 문서는 서버만 실행되면 확인할 수 있습니다.  
업무 요청 등록/조회 API를 실제로 호출하려면 MySQL 실행, DB 생성, `.env` 비밀번호 설정이 필요합니다.

## API

### 업무 요청 등록

```http
POST /api/requests
```

```json
{
  "title": "광고 성과 리포트 자동 생성 요청",
  "description": "매주 월요일 반복되는 광고 성과 리포트 작성을 자동화하고 싶습니다.",
  "requester": "marketing_team",
  "department": "MARKETING",
  "priority": "HIGH"
}
```

### 업무 요청 목록 조회

```http
GET /api/requests
```

### 업무 요청 상세 조회

```http
GET /api/requests/{request_id}
```

### 업무 요청 수정

```http
PUT /api/requests/{request_id}
```

```json
{
  "title": "광고 성과 리포트 자동 생성 요청 수정",
  "description": "매주 월요일 반복되는 리포트 작성 업무를 자동화합니다.",
  "requester": "marketing_team",
  "department": "MARKETING",
  "priority": "URGENT"
}
```

### 부서/상태 필터링

```http
GET /api/requests?department=MARKETING&status=PENDING
```

### 상태 변경

```http
PATCH /api/requests/{request_id}/status
```

```json
{
  "status": "IN_PROGRESS"
}
```

### 업무 요청 삭제

```http
DELETE /api/requests/{request_id}
```

## Domain Rules

### Department

- `MARKETING`
- `LOGISTICS`
- `CS`
- `FINANCE`
- `HR`

### Priority

- `LOW`
- `MEDIUM`
- `HIGH`
- `URGENT`

### Status

- `PENDING`: 요청 접수
- `IN_PROGRESS`: 처리 중
- `COMPLETED`: 완료
- `REJECTED`: 반려

상태 변경은 다음 흐름을 기준으로 검증합니다.

```text
PENDING -> IN_PROGRESS
PENDING -> REJECTED
IN_PROGRESS -> COMPLETED
IN_PROGRESS -> REJECTED
```

## Key Design Points

1. 요청 상태 Enum 관리  
   `PENDING`, `IN_PROGRESS`, `COMPLETED`, `REJECTED` 상태를 기준으로 업무 처리 흐름을 제어했습니다.

2. 계층 분리 구조 적용  
   Router-Service-Repository 구조로 API 요청 처리, 비즈니스 로직, DB 접근 책임을 분리했습니다.

3. Swagger 기반 API 문서화  
   FastAPI 자동 문서화를 활용해 API 테스트와 협업 가능성을 확보했습니다.

4. 간단한 Dashboard 화면 제공  
   현업 담당자가 업무 요청 등록, 목록 조회, 부서/상태 필터링, 상태 변경 흐름을 한 화면에서 확인할 수 있도록 구성했습니다.

## Portfolio Summary

### Problem

마케팅/운영 조직에서 반복적으로 발생하는 업무 요청이 메신저, 문서, 구두 요청 등으로 분산되면 요청 상태 추적과 담당 부서별 관리가 어려워질 수 있다고 판단했습니다.

### Solution

FastAPI 기반 업무 요청 자동화 API를 설계하여 요청 등록, 수정, 삭제, 상태 변경, 부서/상태별 조회 기능을 구현했습니다. 요청 상태를 Enum으로 관리하고, Pydantic Schema를 활용해 요청/응답 모델을 분리했습니다.

### Outcome

분산된 업무 요청을 하나의 API 흐름으로 구조화하고, Swagger 문서화를 통해 API 테스트와 협업 가능성을 높였습니다. 이를 통해 FastAPI 기반 백엔드 구조와 Python 기반 업무 자동화 시스템의 기본 흐름을 이해했습니다.

## AI Usage

- AI 도구는 코드 초안 생성과 오류 해결에 활용했습니다.
- API 구조, 데이터 모델, 상태값, 예외 케이스는 직접 설계하고 검토했습니다.
- 생성된 코드를 실행 및 수정하며 FastAPI 백엔드 구조를 학습했습니다.

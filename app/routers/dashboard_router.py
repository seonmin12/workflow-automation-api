from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["Dashboard"])


@router.get("/dashboard", response_class=HTMLResponse)
def read_dashboard() -> str:
    return """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Workflow Automation Dashboard</title>
  <style>
    :root {
      color-scheme: light;
      --bg: #f6f7f9;
      --surface: #ffffff;
      --surface-soft: #eef3f8;
      --border: #d8dee8;
      --text: #1e2633;
      --muted: #667085;
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --success: #13845f;
      --warning: #a15c07;
      --danger: #b42318;
      --radius: 8px;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      min-height: 100vh;
      background: var(--bg);
      color: var(--text);
      font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.5;
    }

    button,
    input,
    select,
    textarea {
      font: inherit;
    }

    button {
      cursor: pointer;
    }

    .topbar {
      border-bottom: 1px solid var(--border);
      background: var(--surface);
    }

    .topbar-inner,
    .page {
      width: calc(100% - 48px);
      margin: 0 auto;
    }

    .topbar-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      min-height: 68px;
      gap: 16px;
    }

    .brand {
      display: flex;
      flex-direction: column;
      gap: 2px;
      min-width: 0;
    }

    .brand strong {
      font-size: 20px;
      font-weight: 750;
    }

    .brand span {
      color: var(--muted);
      font-size: 13px;
    }

    .nav-link {
      color: var(--primary);
      font-weight: 700;
      text-decoration: none;
      white-space: nowrap;
    }

    .page {
      display: grid;
      grid-template-columns: 320px minmax(0, 1fr);
      gap: 18px;
      padding: 24px 0;
    }

    .panel {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
    }

    .panel-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 16px 18px;
      border-bottom: 1px solid var(--border);
    }

    h1,
    h2 {
      margin: 0;
      font-size: 17px;
      line-height: 1.25;
    }

    .form {
      display: grid;
      gap: 14px;
      padding: 18px;
    }

    .field {
      display: grid;
      gap: 6px;
    }

    .field label {
      color: var(--muted);
      font-size: 13px;
      font-weight: 700;
    }

    .field input,
    .field select,
    .field textarea {
      width: 100%;
      border: 1px solid var(--border);
      border-radius: 6px;
      background: #fff;
      color: var(--text);
      min-height: 42px;
      padding: 9px 10px;
      outline: none;
    }

    .field textarea {
      min-height: 118px;
      resize: vertical;
    }

    .field input:focus,
    .field select:focus,
    .field textarea:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.14);
    }

    .row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }

    .button {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      min-height: 42px;
      border: 1px solid transparent;
      border-radius: 6px;
      padding: 0 14px;
      background: var(--primary);
      color: #fff;
      font-weight: 800;
    }

    .button:hover {
      background: var(--primary-dark);
    }

    .button.secondary {
      background: #fff;
      border-color: var(--border);
      color: var(--text);
    }

    .button.secondary:hover {
      background: var(--surface-soft);
    }

    .content {
      display: grid;
      gap: 14px;
      min-width: 0;
    }

    .filters {
      display: flex;
      align-items: end;
      gap: 10px;
      padding: 14px 18px;
      flex-wrap: wrap;
    }

    .filters .field {
      width: 180px;
    }

    .table-wrap {
      overflow-x: visible;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      table-layout: fixed;
      min-width: 0;
    }

    th,
    td {
      padding: 11px 12px;
      border-top: 1px solid var(--border);
      text-align: left;
      vertical-align: top;
      font-size: 14px;
    }

    th {
      background: var(--surface-soft);
      color: var(--muted);
      font-size: 12px;
      text-transform: uppercase;
    }

    .title-cell {
      font-weight: 750;
      word-break: keep-all;
      overflow-wrap: break-word;
    }

    .description {
      margin-top: 4px;
      color: var(--muted);
      font-size: 13px;
      word-break: keep-all;
      overflow-wrap: break-word;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      min-height: 24px;
      border-radius: 999px;
      padding: 0 9px;
      background: var(--surface-soft);
      color: var(--text);
      font-size: 12px;
      font-weight: 800;
      white-space: nowrap;
    }

    .badge.PENDING {
      color: var(--warning);
      background: #fff3df;
    }

    .badge.IN_PROGRESS {
      color: var(--primary-dark);
      background: #e8f0ff;
    }

    .badge.COMPLETED {
      color: var(--success);
      background: #e8f7f1;
    }

    .badge.REJECTED {
      color: var(--danger);
      background: #fff0ee;
    }

    .status-select {
      width: 100%;
      min-width: 0;
      min-height: 36px;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 6px 8px;
    }

    .delete-button {
      width: 100%;
      min-height: 36px;
      border: 1px solid #fecaca;
      border-radius: 6px;
      background: #fff;
      color: var(--danger);
      padding: 0 10px;
      font-weight: 800;
    }

    .delete-button:hover {
      background: #fff0ee;
    }

    .empty,
    .message {
      padding: 18px;
      color: var(--muted);
    }

    .message {
      display: none;
      border-top: 1px solid var(--border);
    }

    .message.show {
      display: block;
    }

    .message.error {
      color: var(--danger);
    }

    .message.success {
      color: var(--success);
    }

    @media (max-width: 900px) {
      .page {
        grid-template-columns: 1fr;
      }

      .topbar-inner,
      .page {
        width: min(100% - 24px, 1440px);
      }

      .table-wrap {
        overflow-x: auto;
      }

      table {
        min-width: 920px;
      }
    }

    @media (max-width: 560px) {
      .topbar-inner {
        align-items: flex-start;
        flex-direction: column;
        padding: 14px 0;
      }

      .row {
        grid-template-columns: 1fr;
      }

      .filters .field {
        width: 100%;
      }
    }
  </style>
</head>
<body>
  <header class="topbar">
    <div class="topbar-inner">
      <div class="brand">
        <strong>Workflow Automation API</strong>
        <span>Internal automation request management</span>
      </div>
      <a class="nav-link" href="/docs">Swagger Docs</a>
    </div>
  </header>

  <main class="page">
    <section class="panel" aria-labelledby="create-title">
      <div class="panel-header">
        <h1 id="create-title">Create Automation Request</h1>
      </div>
      <form class="form" id="request-form">
        <div class="field">
          <label for="title">Title</label>
          <input id="title" name="title" required maxlength="255"
            value="광고 성과 리포트 자동 생성 요청">
        </div>
        <div class="field">
          <label for="description">Description</label>
          <textarea id="description" name="description" required>매주 월요일 반복되는 광고 성과 리포트 작성을 자동화하고 싶습니다.</textarea>
        </div>
        <div class="field">
          <label for="requester">Requester</label>
          <input id="requester" name="requester" required maxlength="100"
            value="marketing_team">
        </div>
        <div class="row">
          <div class="field">
            <label for="department">Department</label>
            <select id="department" name="department">
              <option>MARKETING</option>
              <option>LOGISTICS</option>
              <option>CS</option>
              <option>FINANCE</option>
              <option>HR</option>
            </select>
          </div>
          <div class="field">
            <label for="priority">Priority</label>
            <select id="priority" name="priority">
              <option>HIGH</option>
              <option>URGENT</option>
              <option>MEDIUM</option>
              <option>LOW</option>
            </select>
          </div>
        </div>
        <button class="button" type="submit">Create</button>
      </form>
      <div class="message" id="form-message"></div>
    </section>

    <section class="content">
      <section class="panel" aria-labelledby="list-title">
        <div class="panel-header">
          <h2 id="list-title">Automation Request List</h2>
          <button class="button secondary" id="refresh-button" type="button">Refresh</button>
        </div>
        <div class="filters">
          <div class="field">
            <label for="filter-department">Department</label>
            <select id="filter-department">
              <option value="">ALL</option>
              <option>MARKETING</option>
              <option>LOGISTICS</option>
              <option>CS</option>
              <option>FINANCE</option>
              <option>HR</option>
            </select>
          </div>
          <div class="field">
            <label for="filter-status">Status</label>
            <select id="filter-status">
              <option value="">ALL</option>
              <option>PENDING</option>
              <option>IN_PROGRESS</option>
              <option>COMPLETED</option>
              <option>REJECTED</option>
            </select>
          </div>
        </div>
        <div class="table-wrap">
          <table>
            <colgroup>
              <col style="width: 4%">
              <col style="width: 31%">
              <col style="width: 13%">
              <col style="width: 14%">
              <col style="width: 10%">
              <col style="width: 12%">
              <col style="width: 11%">
              <col style="width: 5%">
            </colgroup>
            <thead>
              <tr>
                <th>ID</th>
                <th>Request</th>
                <th>Requester</th>
                <th>Department</th>
                <th>Priority</th>
                <th>Status</th>
                <th>Change Status</th>
                <th>Delete</th>
              </tr>
            </thead>
            <tbody id="request-table"></tbody>
          </table>
        </div>
        <div class="empty" id="empty-state">No requests found.</div>
        <div class="message" id="list-message"></div>
      </section>
    </section>
  </main>

  <script>
    const requestForm = document.querySelector("#request-form");
    const requestTable = document.querySelector("#request-table");
    const emptyState = document.querySelector("#empty-state");
    const formMessage = document.querySelector("#form-message");
    const listMessage = document.querySelector("#list-message");
    const refreshButton = document.querySelector("#refresh-button");
    const filterDepartment = document.querySelector("#filter-department");
    const filterStatus = document.querySelector("#filter-status");

    const statuses = ["PENDING", "IN_PROGRESS", "COMPLETED", "REJECTED"];

    function showMessage(element, text, type) {
      element.textContent = text;
      element.className = `message show ${type}`;
    }

    function clearMessage(element) {
      element.textContent = "";
      element.className = "message";
    }

    function escapeHtml(value) {
      return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
    }

    function buildQuery() {
      const params = new URLSearchParams();
      if (filterDepartment.value) {
        params.append("department", filterDepartment.value);
      }
      if (filterStatus.value) {
        params.append("status", filterStatus.value);
      }
      const query = params.toString();
      return query ? `?${query}` : "";
    }

    function renderRequests(requests) {
      requestTable.innerHTML = requests.map((item) => {
        const options = statuses.map((status) => `
          <option value="${status}" ${status === item.status ? "selected" : ""}>
            ${status}
          </option>
        `).join("");

        return `
          <tr>
            <td>${item.id}</td>
            <td class="title-cell">
              ${escapeHtml(item.title)}
              <div class="description">${escapeHtml(item.description)}</div>
            </td>
            <td>${escapeHtml(item.requester)}</td>
            <td><span class="badge">${item.department}</span></td>
            <td><span class="badge">${item.priority}</span></td>
            <td><span class="badge ${item.status}">${item.status}</span></td>
            <td>
              <select class="status-select" data-id="${item.id}" aria-label="Change status">
                ${options}
              </select>
            </td>
            <td>
              <button class="delete-button" type="button" data-id="${item.id}">
                Delete
              </button>
            </td>
          </tr>
        `;
      }).join("");

      emptyState.style.display = requests.length ? "none" : "block";
    }

    async function fetchJson(url, options = {}) {
      const response = await fetch(url, {
        headers: {
          "Content-Type": "application/json",
          ...(options.headers || {}),
        },
        ...options,
      });

      if (!response.ok) {
        const errorBody = await response.json().catch(() => ({}));
        throw new Error(errorBody.detail || `Request failed: ${response.status}`);
      }

      if (response.status === 204) {
        return null;
      }

      return response.json();
    }

    async function loadRequests() {
      clearMessage(listMessage);
      try {
        const requests = await fetchJson(`/api/requests${buildQuery()}`);
        renderRequests(requests);
      } catch (error) {
        renderRequests([]);
        showMessage(listMessage, error.message, "error");
      }
    }

    requestForm.addEventListener("submit", async (event) => {
      event.preventDefault();
      clearMessage(formMessage);

      const formData = new FormData(requestForm);
      const payload = Object.fromEntries(formData.entries());

      try {
        await fetchJson("/api/requests", {
          method: "POST",
          body: JSON.stringify(payload),
        });
        showMessage(formMessage, "Request created.", "success");
        await loadRequests();
      } catch (error) {
        showMessage(formMessage, error.message, "error");
      }
    });

    requestTable.addEventListener("change", async (event) => {
      if (!event.target.matches(".status-select")) {
        return;
      }

      const requestId = event.target.dataset.id;
      const status = event.target.value;

      try {
        await fetchJson(`/api/requests/${requestId}/status`, {
          method: "PATCH",
          body: JSON.stringify({ status }),
        });
        await loadRequests();
      } catch (error) {
        showMessage(listMessage, error.message, "error");
        await loadRequests();
      }
    });

    requestTable.addEventListener("click", async (event) => {
      if (!event.target.matches(".delete-button")) {
        return;
      }

      const requestId = event.target.dataset.id;

      try {
        await fetchJson(`/api/requests/${requestId}`, {
          method: "DELETE",
        });
        await loadRequests();
      } catch (error) {
        showMessage(listMessage, error.message, "error");
      }
    });

    refreshButton.addEventListener("click", loadRequests);
    filterDepartment.addEventListener("change", loadRequests);
    filterStatus.addEventListener("change", loadRequests);

    loadRequests();
  </script>
</body>
</html>
"""

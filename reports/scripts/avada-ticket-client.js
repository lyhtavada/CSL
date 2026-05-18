/**
 * Avada Ticket API Client
 * Docs: /Users/avada/Downloads/external-api.md
 * Base URL: https://avada-ts-a9cb0.web.app/api/external
 */

const BASE_URL = 'https://avada-ts-a9cb0.web.app/api/external';
const API_KEY = 'avd_b6597a0df66cbacba036989a549096cc4a8676af23b8cce70bd13b4ca62ef7ea';

const headers = {
  'Content-Type': 'application/json',
  'X-API-Key': API_KEY,
};

async function request(path, options = {}) {
  const res = await fetch(`${BASE_URL}${path}`, { headers, ...options });
  const json = await res.json();
  if (!json.success) throw new Error(`[${res.status}] ${json.error?.message}`);
  return json.data;
}

// --- Tickets ---

/** Lấy tất cả ticket theo ngày, filter theo app nếu cần
 * @param {string} startDate ISO string
 * @param {string} endDate   ISO string
 * @param {string} [appName] e.g. "Chatty", "JOY Loyalty"
 */
async function getTicketsByDate(startDate, endDate, appName) {
  const params = new URLSearchParams({ startDate, endDate });
  if (appName) params.set('appName', appName);
  return request(`/tickets/by-date?${params}`);
}

/** Lấy tất cả open ticket theo tsStatus (admin view, auto-paginate)
 * @param {string} tsStatus  e.g. "pending", "doing", "dev_fixing"
 * @param {number} [maxItems] default 200
 */
async function getTicketsByStatus(tsStatus, maxItems = 200) {
  const tickets = [];
  let cursor = null;
  do {
    const params = new URLSearchParams({ tsStatus, limit: 20 });
    if (cursor) params.set('cursor', cursor);
    const data = await request(`/tickets/admin?${params}`);
    tickets.push(...data.tickets);
    cursor = data.hasMore ? data.nextCursor : null;
  } while (cursor && tickets.length < maxItems);
  return { tickets, total: tickets.length };
}

/** Lấy tất cả open ticket ở một tsStatus (by-status endpoint)
 * @param {string} tsStatus
 */
async function getOpenTicketsByStatus(tsStatus, limit = 100) {
  return request(`/tickets/by-status?${new URLSearchParams({ tsStatus, limit })}`);
}

/** Lấy chi tiết một ticket */
async function getTicket(id) {
  return request(`/tickets/${id}`);
}

/** Tìm ticket theo Crisp chat link */
async function getTicketByChat(chatLink) {
  return request(`/tickets/by-chat?${new URLSearchParams({ chatLink })}`);
}

// --- Members ---

/** Lấy danh sách tất cả members */
async function getMembers(limit = 100) {
  return request(`/members?${new URLSearchParams({ limit })}`);
}

// --- Export ---

module.exports = {
  getTicketsByDate,
  getTicketsByStatus,
  getOpenTicketsByStatus,
  getTicket,
  getTicketByChat,
  getMembers,
};

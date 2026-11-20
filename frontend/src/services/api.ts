/**
 * API Service — Shared API client for all pages
 * Issue #8 (张智轩) + #11 (李江炜)
 */

const API_BASE = import.meta.env.VITE_API_BASE_URL || "";

async function request<T = any>(
  path: string,
  options: RequestInit = {}
): Promise<T> {
  const url = `${API_BASE}/api/v1${path}`;
  const res = await fetch(url, {
    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
    ...options,
  });

  if (!res.ok) {
    throw new Error(`API Error: ${res.status} ${res.statusText}`);
  }

  return res.json();
}

// --- Chat ---
export async function sendChatMessage(
  message: string,
  sessionId: string
): Promise<Response> {
  const url = `${API_BASE}/api/v1/chat`;
  return fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, session_id: sessionId }),
  });
}

// --- Plan ---
export async function generatePlan() {
  return request("/plan/generate", { method: "POST" });
}

export async function getPlan(planId: string) {
  return request(`/plan/${planId}`);
}

export async function toggleDay(planId: string, dayIndex: number) {
  return request(`/plan/${planId}/day/${dayIndex}/toggle`, { method: "PATCH" });
}

// --- Correction ---
export async function analyzePosture(formData: FormData): Promise<Response> {
  const url = `${API_BASE}/api/v1/correction`;
  return fetch(url, { method: "POST", body: formData });
}

export async function correctionHistory() {
  return request("/correction/history");
}

// --- User ---
export async function getProfile() {
  return request("/user/profile");
}

export async function updateProfile(data: Record<string, unknown>) {
  return request("/user/profile", {
    method: "PATCH",
    body: JSON.stringify(data),
  });
}

export async function getUserStats() {
  return request("/user/stats");
}

// --- Admin ---
export async function listExercises() {
  return request("/admin/exercises");
}

export async function listUsers() {
  return request("/admin/users");
}

export async function getDashboard() {
  return request("/admin/dashboard");
}
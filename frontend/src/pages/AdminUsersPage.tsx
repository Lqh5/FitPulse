/**
 * Admin User Management Page — 后台页面 2
 * Issue #11 (李江炜)
 */
export default function AdminUsersPage() {
  return (
    <div className="page-container">
      <header className="bg-gray-900 text-white px-4 py-3 flex items-center gap-3 sticky top-0 z-10">
        <a href="/" className="text-white">&larr;</a>
        <h1 className="font-semibold">User Management</h1>
      </header>

      {/* Stats bar */}
      <div className="grid grid-cols-3 gap-3 p-4 bg-gray-50">
        {[
          { label: "Total Users", value: "0", color: "text-blue-500" },
          { label: "Today Active", value: "0", color: "text-green-500" },
          { label: "New This Week", value: "0", color: "text-brand-500" },
        ].map((s) => (
          <div key={s.label} className="text-center bg-white rounded-lg p-3 shadow-sm">
            <p className={`text-xl font-bold ${s.color}`}>{s.value}</p>
            <p className="text-xs text-gray-400">{s.label}</p>
          </div>
        ))}
      </div>

      <div className="p-4">
        <p className="text-center text-gray-400 mt-10">
          User list will appear here.
          <br />
          TODO: #11 李江炜 — implement user management UI
        </p>
      </div>
    </div>
  );
}
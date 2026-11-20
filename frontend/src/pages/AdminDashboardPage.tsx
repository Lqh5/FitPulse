/**
 * Admin Dashboard Page — 后台页面 3
 * Issue #11 (李江炜)
 */
export default function AdminDashboardPage() {
  return (
    <div className="page-container">
      <header className="bg-gray-900 text-white px-4 py-3 flex items-center gap-3 sticky top-0 z-10">
        <a href="/" className="text-white">&larr;</a>
        <h1 className="font-semibold">System Dashboard</h1>
      </header>

      <div className="p-4">
        {/* Dashboard stats */}
        <div className="grid grid-cols-4 gap-3 mb-6">
          {[
            { label: "Users", value: "0", color: "text-blue-500" },
            { label: "Active", value: "0", color: "text-green-500" },
            { label: "Corrections", value: "0", color: "text-brand-500" },
            { label: "Knowledge", value: "0", color: "text-purple-500" },
          ].map((s) => (
            <div key={s.label} className="text-center bg-white rounded-lg p-3 shadow-sm">
              <p className={`text-xl font-bold ${s.color}`}>{s.value}</p>
              <p className="text-xs text-gray-400">{s.label}</p>
            </div>
          ))}
        </div>

        <p className="text-center text-gray-400 mt-20">
          Dashboard charts will appear here.
          <br />
          TODO: #11 李江炜 — implement dashboard UI
        </p>
      </div>
    </div>
  );
}
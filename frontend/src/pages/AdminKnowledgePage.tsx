/**
 * Admin Knowledge Base Page — 后台页面 1
 * Issue #11 (李江炜)
 */
export default function AdminKnowledgePage() {
  return (
    <div className="page-container">
      <header className="bg-gray-900 text-white px-4 py-3 flex items-center gap-3 sticky top-0 z-10">
        <a href="/" className="text-white">&larr;</a>
        <h1 className="font-semibold">Knowledge Base</h1>
        <button className="ml-auto bg-brand-500 text-white rounded-lg px-3 py-1 text-sm">
          + Add Entry
        </button>
      </header>

      <div className="p-4">
        <p className="text-center text-gray-400 mt-20">
          Knowledge base entries will appear here.
          <br />
          TODO: #11 李江炜 — implement management UI
        </p>
      </div>
    </div>
  );
}
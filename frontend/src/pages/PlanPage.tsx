/**
 * Training Plan Page — 用户端页面 2
 * Issue #8 (张智轩)
 */
export default function PlanPage() {
  return (
    <div className="page-container">
      <header className="bg-brand-500 text-white px-4 py-3 sticky top-0 z-10">
        <h1 className="font-semibold">Training Plan</h1>
      </header>

      <div className="p-4">
        {/* Week selector */}
        <div className="flex gap-2 mb-4">
          {["Last Week", "This Week", "Next Week"].map((w) => (
            <button
              key={w}
              className={`px-4 py-1 rounded-full text-sm ${
                w === "This Week"
                  ? "bg-brand-500 text-white"
                  : "bg-gray-100 text-gray-600"
              }`}
            >
              {w}
            </button>
          ))}
        </div>

        {/* Placeholder days */}
        <div className="text-center text-gray-400 mt-20">
          <p className="text-4xl mb-4">📋</p>
          <p className="font-medium text-gray-600">No training plan yet</p>
          <p className="text-sm mt-2">
            Go to Coach tab and say "Generate a plan" to get started!
          </p>
        </div>
      </div>
    </div>
  );
}
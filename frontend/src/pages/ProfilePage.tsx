/**
 * Profile Page — 用户端页面 4
 * Issue #8 (张智轩)
 */
export default function ProfilePage() {
  return (
    <div className="page-container">
      {/* Profile header card */}
      <div className="bg-gradient-to-br from-brand-500 to-brand-600 text-white px-4 pt-6 pb-8">
        <div className="flex items-center gap-4 mb-4">
          <div className="w-16 h-16 rounded-full bg-white/20 flex items-center justify-center text-2xl">
            👤
          </div>
          <div>
            <h1 className="font-semibold text-lg">Fitness Newbie</h1>
            <p className="text-sm text-white/70">Beginner · Stay Fit</p>
          </div>
        </div>
        <button className="bg-white/20 text-white rounded-full px-4 py-1 text-sm">
          Edit Profile
        </button>
      </div>

      {/* Stats grid */}
      <div className="grid grid-cols-4 gap-3 p-4 -mt-4">
        {[
          { label: "Weekly", value: "0" },
          { label: "Sessions", value: "0" },
          { label: "Hours", value: "0" },
          { label: "Kcal", value: "0" },
        ].map((s) => (
          <div
            key={s.label}
            className="bg-white rounded-xl p-3 text-center shadow-sm"
          >
            <p className="text-lg font-bold text-brand-500">{s.value}</p>
            <p className="text-xs text-gray-400">{s.label}</p>
          </div>
        ))}
      </div>

      {/* Menu items */}
      <div className="px-4 space-y-1">
        {[
          { icon: "📋", label: "Correction History" },
          { icon: "⚙️", label: "Settings" },
          { icon: "ℹ️", label: "About FitPulse" },
        ].map((item) => (
          <div
            key={item.label}
            className="flex items-center gap-3 p-4 bg-white rounded-lg cursor-pointer hover:bg-gray-50"
          >
            <span className="text-xl">{item.icon}</span>
            <span className="text-sm">{item.label}</span>
            <span className="ml-auto text-gray-300">›</span>
          </div>
        ))}
      </div>
    </div>
  );
}
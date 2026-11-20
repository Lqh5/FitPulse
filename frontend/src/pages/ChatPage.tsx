/**
 * AI Coach Chat Page — 用户端页面 1
 * Issue #8 (张智轩)
 *
 * Features:
 * - AI 虚拟教练头像 + "在线" 徽章
 * - 对话气泡（用户橙色右对齐 / Agent 白色左对齐 + 知识卡片）
 * - 三个快捷操作按钮（查动作/生成计划/姿势纠正）
 * - 输入框 + 相机按钮 + 发送按钮
 */
export default function ChatPage() {
  return (
    <div className="page-container flex flex-col">
      {/* Header */}
      <header className="bg-brand-500 text-white px-4 py-3 flex items-center gap-3 sticky top-0 z-10">
        <div className="relative">
          <div className="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center text-xl">
            🤖
          </div>
          <span className="absolute -bottom-1 -right-1 w-3 h-3 bg-green-400 rounded-full border-2 border-brand-500" />
        </div>
        <div>
          <h1 className="font-semibold text-sm">AI Virtual Trainer</h1>
          <p className="text-xs text-white/70">Online</p>
        </div>
      </header>

      {/* Messages area */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {/* Placeholder — TODO: #8 张智轩 implement chat UI */}
        <div className="text-center text-gray-400 mt-20">
          <p className="text-4xl mb-4">💪</p>
          <p className="font-medium text-gray-600">AI Virtual Coach</p>
          <p className="text-sm mt-2">
            Ask me about exercises, get a training plan, or upload a photo for posture check!
          </p>
        </div>
      </div>

      {/* Quick actions */}
      <div className="flex gap-2 px-4 py-2 overflow-x-auto">
        <button className="btn-primary text-sm whitespace-nowrap">🔍 Look up exercise</button>
        <button className="btn-primary text-sm whitespace-nowrap">📋 Generate plan</button>
        <button className="btn-primary text-sm whitespace-nowrap">📷 Posture correction</button>
      </div>

      {/* Input bar */}
      <div className="p-4 border-t border-gray-100 flex items-center gap-2">
        <button className="text-gray-400 text-xl">📷</button>
        <input
          type="text"
          placeholder="Ask your AI coach..."
          className="flex-1 bg-gray-100 rounded-full px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500"
        />
        <button className="bg-brand-500 text-white rounded-full w-9 h-9 flex items-center justify-center text-sm">
          ➤
        </button>
      </div>
    </div>
  );
}
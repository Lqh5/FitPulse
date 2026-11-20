"""
Agent Orchestration Service
Issue #9 (林祺皓) + #5 (罗堉楠)

Orchestrates:
- Intent routing
- System prompt assembly (Issue #5)
- RAG context injection
- Tool dispatch
- Response streaming (SSE)

TODO: #5 罗堉楠 — design system prompt templates
TODO: #9 林祺皓 — implement LangChain agent loop + SSE streaming
"""


class AgentOrchestrator:
    """
    Core agent orchestration engine.

    Coordinates:
    - Claude LLM (via langchain-anthropic)
    - RAG retrieval (via RAGService)
    - Tool dispatch (via tools/)
    """

    def __init__(self):
        self.system_prompt = self._build_system_prompt()

    def _build_system_prompt(self) -> str:
        """
        Build the system prompt from templates.

        TODO: #5 罗堉楠 — design & iterate on prompt templates
        """
        return (
            "你是 FitPulse AI 虚拟健身教练，一个专业的居家健身指导助手。\n\n"
            "## 你的能力\n"
            "1. 查询健身动作的标准要领、目标肌群、呼吸节奏、常见错误\n"
            "2. 根据用户水平/目标/器械生成结构化的周训练计划\n"
            "3. 分析用户上传的动作照片，指出姿势偏差并提供纠正建议\n\n"
            "## 安全边界\n"
            "- 如果用户描述疼痛或不适，立即建议停止训练并咨询医生\n"
            "- 不提供医疗诊断或治疗建议\n"
            "- 对高危动作（如大重量深蹲、硬拉）强调安全注意事项\n\n"
            "## 输出格式\n"
            "- 动作查询 → 结构化卡片：动作名称 + 要领 + 呼吸 + 常见错误 + 出处\n"
            "- 训练计划 → 表格形式：每天的训练部位 + 动作 + 组数×次数 + 休息时间\n"
            "- 姿势纠正 → 问题列表：部位 + 严重程度 + 问题描述 + 纠正方法 + 安全提示"
        )

    async def process_message(self, message: str, session_id: str, has_image: bool = False):
        """
        Process a user message and yield SSE events.

        TODO: #9 林祺皓 — implement full agent loop
        """
        yield {"type": "thinking", "content": "Agent is thinking..."}
        yield {"type": "token", "content": "This is a placeholder response."}
        yield {"type": "done"}


# Singleton
agent = AgentOrchestrator()
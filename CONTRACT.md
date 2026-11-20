# FitPulse — AI 虚拟健身教练 · 协作契约

> 本文档是团队协作的唯一真相源（Single Source of Truth）。
> 所有接口、数据格式、文件归属、依赖关系均在此定义。
> 修改本文档需提 PR 并经队长（罗炜 @power819）Review 合并。

---

## 一、项目概述

FitPulse 是一款 AI 驱动的"口袋私教"移动 Web 应用，面向高校学生居家健身场景。
核心功能：AI 对话查动作 → 生成训练计划 → 拍照纠姿。

技术栈：React 18 + TypeScript + TailwindCSS (前端) / FastAPI + LangChain + Claude API (后端) / MySQL + Chroma + MinIO (存储)

---

## 二、仓库结构

```
fitpulse-app/
├── frontend/           # React 18 SPA（张智轩 #8、李江炜 #11）
│   ├── src/
│   │   ├── components/ # 可复用组件
│   │   ├── pages/      # 7 个页面
│   │   ├── hooks/      # 自定义 Hook
│   │   ├── services/   # API 调用封装
│   │   └── styles/     # Tailwind 主题
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.js
├── backend/            # FastAPI 后端（徐心铭 #7、林祺皓 #9、罗堉楠 #5、马锦城 #6）
│   ├── app/
│   │   ├── main.py     # FastAPI 入口
│   │   ├── config.py   # 配置（环境变量读取）
│   │   ├── models/     # SQLAlchemy 数据模型
│   │   ├── routes/     # API 路由（chat / plan / correction / user）
│   │   ├── services/   # 业务逻辑层
│   │   └── tools/      # LangChain Agent 工具定义
│   ├── requirements.txt
│   └── Dockerfile
├── FitPulse-KnowledgeBase/  # 领域知识库（林复彬 #3、陈辉腾 #4）
│   ├── exercises/       # 标准动作（≥50 条）
│   ├── error-posture/    # 常见错误姿势
│   ├── muscle-activation/ # 肌肉激活
│   └── manifest.json    # 条目清单
├── scripts/             # 工具脚本（马锦城 #6）
│   └── init_knowledge_base.py  # 知识库初始化（嵌入 → Chroma）
├── docs/                # 设计文档（已完成）
├── tests/               # 测试（连向薇 #10）
│   ├── test_api/        # API 测试
│   ├── test_rag/        # RAG 管线测试
│   └── test_e2e/        # 端到端测试
├── docker-compose.yml   # 一键启动（罗炜 #1）
├── .env.example         # 环境变量模板（罗炜 #1）
├── CONTRACT.md          # 本文档
└── CONTRIBUTING.md      # 协作指南
```

---

## 三、数据模型（13 张表）

### 核心实体

```python
# users — 用户
class User:
    id: UUID                  # 主键
    nickname: str(50)         # 昵称
    avatar_url: str(255)      # 头像
    level: Enum               # beginner / intermediate / advanced
    goal: Enum                # lose_weight / build_muscle / stay_fit
    equipment: JSON           # ["dumbbell", "yoga_mat", ...]
    weekly_days: int          # 每周训练天数
    created_at: datetime

# exercises — 标准动作库
class Exercise:
    id: UUID
    name: str(100)            # 动作名称
    module: Enum              # standard_action / muscle_activation / error_harm
    target_muscles: JSON      # ["胸大肌", "肱三头肌"]
    difficulty: Enum          # beginner / intermediate / advanced
    equipment_needed: JSON    # 所需器材
    description: text         # 动作描述
    form_cues: text           # 动作要点
    breathing: text           # 呼吸节奏
    common_errors: text       # 常见错误
    image_urls: JSON          # 示范图片
    video_url: str(255)       # 示范视频
    tags: JSON                # 标签

# training_plans — 训练计划
class TrainingPlan:
    id: UUID
    user_id: FK → users
    week_start: date
    status: Enum              # active / completed / abandoned
    created_at: datetime

# plan_days — 训练日
class PlanDay:
    id: UUID
    plan_id: FK → training_plans
    day_index: int            # 1-7（周一至周日）
    focus: str(100)           # "胸+三头"
    estimated_minutes: int

# plan_exercises — 日训练动作
class PlanExercise:
    id: UUID
    day_id: FK → plan_days
    exercise_id: FK → exercises
    sets: int
    reps: int
    rest_seconds: int
    order: int                # 排序

# posture_corrections — 姿势纠正
class PostureCorrection:
    id: UUID
    user_id: FK → users
    photo_url: str(255)
    overall_assessment: text
    safety_note: text
    created_at: datetime

# correction_issues — 纠正项
class CorrectionIssue:
    id: UUID
    correction_id: FK → posture_corrections
    body_part: str(50)
    severity: Enum            # mild / moderate / severe
    problem: text
    correction: text

# agent_sessions — Agent 会话
class AgentSession:
    id: UUID
    user_id: FK → users
    task_type: str(50)        # exercise_lookup / plan_generate / posture_correct
    context: JSON             # 会话上下文
    created_at: datetime

# messages — 对话消息
class Message:
    id: UUID
    session_id: FK → agent_sessions
    role: Enum                # user / assistant / system / tool
    content: text
    metadata: JSON
    created_at: datetime

# tool_calls — 工具调用日志
class ToolCall:
    id: UUID
    message_id: FK → messages
    tool_name: str(100)
    args: JSON
    result: JSON

# workout_records — 训练记录
class WorkoutRecord:
    id: UUID
    user_id: FK → users
    plan_id: FK → training_plans
    completed_at: datetime
    duration_minutes: int
    difficulty_rating: int    # 1-5
    notes: text

# feedbacks — 用户反馈
class Feedback:
    id: UUID
    user_id: FK → users
    content: text
    category: str(50)
    status: Enum              # pending / processing / resolved
    created_at: datetime
```

---

## 四、API 接口契约（10 个核心接口）

### 基础 URL: `/api/v1`

| 方法 | 路径 | 说明 | 归属 |
|------|------|------|------|
| POST | `/api/v1/chat` | AI 对话（SSE 流式） | #7 + #9 |
| POST | `/api/v1/plan/generate` | 生成训练计划 | #7 + #9 |
| GET | `/api/v1/plan/{plan_id}` | 获取训练计划详情 | #7 |
| PATCH | `/api/v1/plan/{plan_id}/day/{day_index}/toggle` | 标记/取消完成 | #7 |
| POST | `/api/v1/correction` | 上传照片 → 姿态分析 | #7 + #9 |
| GET | `/api/v1/correction/history` | 纠姿历史 | #7 |
| GET | `/api/v1/exercises/search?q=` | 搜索动作 | #7 |
| GET | `/api/v1/user/profile` | 用户信息 | #7 |
| PATCH | `/api/v1/user/profile` | 更新用户信息 | #7 |
| GET | `/api/v1/user/stats` | 用户统计数据 | #7 |

### SSE 流格式（chat 接口）

```
data: {"type": "token", "content": "肱二头肌弯举"}

data: {"type": "tool_call", "tool": "query_exercise", "args": {...}}

data: {"type": "tool_result", "result": {...}}

data: {"type": "done"}
```

---

## 五、前端组件契约

### 页面路由

| 路径 | 页面 | 归属 |
|------|------|------|
| `/` | AI 教练对话 | #8 |
| `/plan` | 训练计划 | #8 |
| `/correction` | 姿势纠正 | #8 |
| `/profile` | 个人中心 | #8 |
| `/admin/knowledge` | 知识库管理 | #11 |
| `/admin/users` | 用户管理 | #11 |
| `/admin/dashboard` | 系统仪表盘 | #11 |

### 全局命名空间（类 Bookkeeper 模式）

```typescript
// 所有组件通过 src/services/api.ts 调用后端
import { api } from '@/services/api';

// 全局状态用 React Context
// AuthContext — 用户认证状态
// ChatContext — 对话状态
```

---

## 六、文件归属与依赖图

```
            ┌─────────────────┐
            │  #1 罗炜·架构    │ ← docker-compose.yml, .env.example, CI/CD
            └────────┬────────┘
                     │ 依赖所有人
    ┌────────────────┼────────────────┐
    │                │                │
    ▼                ▼                ▼
┌─────────┐   ┌──────────┐   ┌──────────┐
│#3 林复彬│   │#4 陈辉腾  │   │#2 陈加豪 │
│#4 陈辉腾│   │  知识库   │   │   PM     │
│  知识库  │   │  error+  │   │  验收标准 │
│ standard │   │  muscle  │   └──────────┘
└────┬─────┘   └────┬─────┘
     │              │
     └──────┬───────┘
            ▼
    ┌───────────────┐
    │ #6 马锦城·RAG │ ← Chroma 初始化脚本, 嵌入管线
    └───────┬───────┘
            │
    ┌───────┴───────┐
    │               │
    ▼               ▼
┌────────┐   ┌──────────┐
│#5 罗堉楠│   │#9 林祺皓  │
│ Prompt  │   │ 工具编排  │ ← LangChain tools, intent router
└───┬────┘   └─────┬────┘
    │              │
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │ #7 徐心铭·后端│ ← FastAPI 全接口
    └──────┬───────┘
           │
    ┌──────┴───────┐
    │              │
    ▼              ▼
┌────────┐   ┌──────────┐
│#8 张智轩│   │#11 李江炜│
│ 前端    │   │  UI/后台  │ ← React SPA, Tailwind 主题
│ 用户端  │   │  管理端   │
└───┬────┘   └─────┬────┘
    │              │
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │ #10 连向薇·测试│ ← 全部测试
    └──────────────┘
```

---

## 七、成员分工与 Issue

| Issue | 成员 | 学号 | 角色 | 可交付物 | 截止 |
|-------|------|------|------|----------|------|
| #1 | 罗炜 | 102401317 | 队长·架构 | docker-compose, CI/CD, 最终集成 | Week 13 |
| #2 | 陈加豪 | 102401529 | PM | PRD 补充, 验收标准, 用户故事矩阵 | Week 10 |
| #3 | 林复彬 | 102401527 | 知识库A | ≥50 条标准动作知识条目 | Week 10 |
| #4 | 陈辉腾 | 102401521 | 知识库B | 肌肉激活+常见错误知识条目 | Week 10 |
| #5 | 罗堉楠 | 102401218 | Prompt | 3 个 Agent 提示词模板 | Week 10 |
| #6 | 马锦城 | 102401328 | RAG | Chroma 初始化脚本+RAG 管线 | Week 11 |
| #7 | 徐心铭 | 102401531 | 后端 | FastAPI 全接口实现 | Week 11 |
| #8 | 张智轩 | 102401121 | 前端 | React 用户端 4 页 | Week 12 |
| #9 | 林祺皓 | 102401119 | 编排 | LangChain 工具+意图路由 | Week 11 |
| #10 | 连向薇 | 102401203 | 测试 | 单元+集成+E2E 测试 | Week 13 |
| #11 | 李江炜 | 102401222 | UI/后台 | Tailwind 主题+管理后台3页 | Week 12 |

---

## 八、协作流程

1. **Fork** → 每位成员 Fork `power819/FitPulse` 仓库
2. **Branch** → 从 `main` 创建功能分支：`feat/issue-{N}-{描述}`
3. **Develop** → 在自己的分支上开发
4. **PR** → 完成后提 Pull Request 到 `power819/FitPulse` 的 `main` 分支
5. **Review** → 队长 Review + 合并
6. **Sync** → `git remote add upstream https://github.com/power819/FitPulse.git` → `git pull upstream main`

---

## 九、环境变量（.env）

```bash
# Claude API
ANTHROPIC_API_KEY=sk-ant-xxx

# MySQL
MYSQL_ROOT_PASSWORD=fitpulse2024
MYSQL_DATABASE=fitpulse
MYSQL_USER=fitpulse
MYSQL_PASSWORD=fitpulse2024

# Chroma
CHROMA_HOST=chroma
CHROMA_PORT=8000

# MinIO
MINIO_ROOT_USER=fitpulse
MINIO_ROOT_PASSWORD=fitpulse2024

# JWT
JWT_SECRET_KEY=change-me-in-production
```

---

## 十、启动命令

```bash
# 1. 克隆
git clone https://github.com/power819/FitPulse.git
cd FitPulse

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env，填入 ANTHROPIC_API_KEY

# 3. 一键启动
docker compose up -d

# 4. 初始化知识库
docker compose exec backend python scripts/init_knowledge_base.py

# 5. 访问
# 前端: http://localhost:3000
# API 文档: http://localhost:8000/docs
```

---

*本文档由队长罗炜维护。任何接口变更必须先更新本文档再修改代码。*
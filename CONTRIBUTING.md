# 🤝 FitPulse 团队成员协作指南

## 🏗️ 当前阶段：代码开发（第10周起）

项目骨架已搭建完毕，所有成员通过 **Fork → Branch → PR** 流程协作开发。

📋 **协作契约**：[CONTRACT.md](CONTRACT.md) — 数据模型、API接口、文件归属、依赖关系的唯一真相源。

---

## 队员操作步骤（每人约 5 分钟）

### 第 1 步：Fork 仓库

1. 打开 https://github.com/power819/FitPulse
2. 点击右上角 **Fork** 按钮
3. 保持仓库名 `FitPulse`，点击 **Create fork**

### 第 2 步：克隆你的 Fork

```bash
git clone https://github.com/你的用户名/FitPulse.git
cd FitPulse
git remote add upstream https://github.com/power819/FitPulse.git
```

### 第 3 步：找到你的 Issue，创建分支

每个成员有一个对应的 GitHub Issue，编号 #1 到 #11。

```bash
git checkout -b feat/issue-{N}-{描述}
```

### 第 4 步：开发 → 提交 → 推送到你的 Fork

### 第 5 步：发起 Pull Request

1. 进入你的 Fork 仓库页面
2. 点击 **Contribute** → **Open Pull Request**
3. 标题格式：`[Issue #N] 角色名 - 成果描述`
4. 描述中引用 `Closes #N` 关联 Issue
5. 点击 **Create pull request**

---

## 11 个 Issue · 成员分工

| Issue | 成员 | 学号 | 角色 | 开发文件 |
|-------|------|------|------|----------|
| #1 | 罗炜 | 102401317 | 队长·架构 | `docker-compose.yml`, `.env.example`, CI/CD, 最终集成 |
| #2 | 陈加豪 | 102401529 | PM·需求 | PRD补充, 验收标准, 用户故事矩阵 |
| #3 | 林复彬 | 102401527 | 知识库A | `FitPulse-KnowledgeBase/exercises/` ≥50条标准动作 |
| #4 | 陈辉腾 | 102401521 | 知识库B | `FitPulse-KnowledgeBase/muscle-activation/` + `error-posture/` |
| #5 | 罗堉楠 | 102401218 | Prompt工程 | `backend/app/services/agent.py` 系统提示词 + 3个Agent模板 |
| #6 | 马锦城 | 102401328 | RAG管线 | `backend/app/services/rag.py`, `scripts/init_knowledge_base.py` |
| #7 | 徐心铭 | 102401531 | 后端API | `backend/app/routes/` + `backend/app/models/` 全接口实现 |
| #8 | 张智轩 | 102401121 | 前端用户端 | `frontend/src/pages/ChatPage.tsx` 等4页 |
| #9 | 林祺皓 | 102401119 | 工具编排 | `backend/app/tools/` + `backend/app/services/agent.py` |
| #10 | 连向薇 | 102401203 | 测试 | `tests/` 单元+集成+E2E |
| #11 | 李江炜 | 102401222 | UI/后台 | `frontend/src/pages/Admin*.tsx` + Tailwind主题 + `frontend/src/styles/` |

---

## 协作流程示意

```
power819/FitPulse (主仓库)
    │
    ├── Fork → 你的用户名/FitPulse
    │              │
    │              ├── feat/issue-1-xxx ──PR──→ #1
    │              ├── feat/issue-2-xxx ──PR──→ #2
    │              └── ...
    │
    └── 队长 Review → Merge → 队员 Sync upstream
```

---

## 同步上游

```bash
# 当主仓库有更新时，同步到你的 Fork
git pull upstream main
git push origin main
```

---

## 📸 协作截图取证清单

| 截图内容 | 链接 | 证明力 |
|---|---|---|
| Issues 列表 | https://github.com/power819/FitPulse/issues | ⭐⭐⭐ 显示全部任务分配 |
| PR 列表 | https://github.com/power819/FitPulse/pulls | ⭐⭐⭐ 显示所有人提交的 PR |
| Fork Network | https://github.com/power819/FitPulse/network/members | ⭐⭐⭐ 显示所有队员 Fork |
| Insights → Contributors | https://github.com/power819/FitPulse/graphs/contributors | ⭐⭐ 显示贡献者活跃度 |
| 单个 PR 详情页 | 点击任意 PR | ⭐⭐ 显示讨论记录 |

---

## ⚡ 关键规则

1. **先读 CONTRACT.md** — 任何接口变更必须先改契约再写代码
2. **不要直接 push main** — 一切通过 PR
3. **一个 Issue 一个分支** — 不要在一个分支里塞多个 Issue 的工作
4. **PR 描述写 Closes #N** — 合并时自动关闭对应 Issue
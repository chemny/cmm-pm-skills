# cmm-pm-skills

> 一套**产品经理工作流** skills：把"从市场到落地"的每个阶段做成可调用的命令，每步产出真实可用的交付物，并共享一套统一工作纪律。
> 🌐 English: [`README.en.md`](README.en.md)

> **致谢上游**：本项目基于 [phuryn/pm-skills](https://github.com/phuryn/pm-skills)（MIT）二次开发——在其插件骨架上重构各阶段命令、新增统一工作纪律 `CONVENTIONS.md` 与界面设计(⑤)/技术方案(⑥)等环节。原作者版权见 [`LICENSE`](LICENSE)。

## 适合谁 / Who it's for
- 用 Claude Code / Codex 做产品的**产品经理、创始人、独立开发者**；
- 想要"从想法到 PRD 到原型"一条龙、且**每步有据可依、不被 AI 糊弄**的人。

## 它解决什么 / What it solves
通用 AI 给你一堆漂亮文字，但**浅、爱编、容易跑偏**。这套 skills 把 PM 各阶段做成命令，每步：**继承上游不重造、自己搜证三角验证、不编造、结论交你拍板**——产出能直接用的交付物，而不是空话。

## 核心能力 / Core Capabilities（端到端流水线）
| 阶段 | 命令 | 产出 |
|---|---|---|
| ① 市场分析 | `/market-analysis` | 市场/用户/买单人/竞品/颠覆机会（数据定） |
| ② 需求洞察 | `/insight` | 真需求 + 风险结论 + 一手验证计划 |
| ③ 产品战略 | `/strategy` | 定位/壁垒/商业模式/定价/打法 |
| ④ PRD | `/write-prd` | 完整可开发 PRD（需求+功能+流程+交互+数据+边界） |
| ⑤ 界面设计 | `/wireframe` | Mermaid 流/态 + 可点击 HTML 原型 + 规格 |
| ⑥ 技术方案 | `/tech-design` | 选型/架构/数据/解 spike/冲突检查 |
| ⑦ 用户故事 | `/write-stories` | 故事 + 验收（可追溯） |
| ⑧ 测试 | `/test-scenarios` | 测试用例（happy/边界/错误） |
| ⑩ 上线 | `/plan-launch` 等 | GTM 计划 |
| ⑪ 数据/迭代 | `/analyze-cohorts` 等 | 指标 → 回到 ② |

> 完整说明见 [`PIPELINE.md`](PIPELINE.md)；统一纪律见 [`CONVENTIONS.md`](CONVENTIONS.md)。⑥技术方案实现/⑨研发属工程，不在本套件。

## 平台兼容 / Compatibility
| 平台 | 支持 |
|---|---|
| Claude Code | ✅ 命令 + 技能 |
| Codex CLI | ✅ 技能（`/slash` 命令以自然语言描述触发） |
| 其他（Cursor/Gemini CLI 等） | 技能可用（复制 `skills/` 目录） |

## 安装 / Install（Claude Code）
```bash
claude plugin marketplace add <本仓库地址>
claude plugin install pm-market-research@cmm-pm-skills
claude plugin install pm-product-discovery@cmm-pm-skills
claude plugin install pm-product-strategy@cmm-pm-skills
claude plugin install pm-execution@cmm-pm-skills
# 其余：pm-go-to-market / pm-data-analytics / pm-marketing-growth / pm-ai-shipping / pm-toolkit
```

## 快速开始 / Quick Start
```text
/market-analysis 一句话描述你的产品想法
```
它会**先和你确认核心信息**（产品/人群/市场/盈利），再做数据驱动的市场分析，结尾给风险结论并问你是否进下一步。逐阶段往下走即可。

## 用法示例 / Usage Examples
端到端真实案例见 [`_runs/`](_runs)：
- `_runs/voice-ime/` —— "sayit"（个性化语音输入法）从市场分析到 PRD/原型/技术方案的全过程；
- `_runs/natgeo-video/` —— "英文文章转视频学习工具"的市场分析与需求洞察。

## 工作原理 / How it works
- **命令 = 阶段动作**，继承上游阶段的产出，只做本阶段专属逻辑；
- **统一纪律**写在根 `CONVENTIONS.md`（母版），每个插件内置同步副本，**安装即继承**；
- 每个阶段：先研究/搜证 → 给结论与风险 → **决定权交用户**。

## 仓库结构 / Repository Structure
```
CONVENTIONS.md          统一纪律（母版）
PIPELINE.md             全链路总览
sync_conventions.sh     母版→各插件同步
validate_plugins.py     契约校验
pm-*/                   9 个插件（commands/ + skills/ + 内置 CONVENTIONS 副本）
_design/                方法论蓝图 / 清单
_runs/                  端到端示例
```

## 要求 / 配置 / Requirements
- Claude Code 或 Codex CLI；
- 部分命令需联网搜索（市场/竞品研究）。

## 维护
- 改纪律 → 编辑根 `CONVENTIONS.md` → 跑 `./sync_conventions.sh`；
- 改命令/技能 → 跑 `python3 validate_plugins.py`。

## License
MIT，见 [`LICENSE`](LICENSE)（保留原作者 phuryn 版权 + CMM 修改版权）。

# 总协同蓝图：pm-console / `/cmm-pm`

> 定位：站在 9 个阶段插件之上的"领航员 + 项目台账"。统筹一个产品项目走到哪、下一步敲什么、产出存哪、门过没过。**不执行阶段、不硬调用跨插件命令、零侵入。**

## 为什么需要
协同此前靠"约定 + 手动 + 各命令的继承指令"，没有统一调度；**最大痛点是跨会话状态会丢**——换会话回来没有任何东西记得项目走到哪、上游产出在哪。`pm-console` 用磁盘上的台账补这个洞。

## 形态
- 插件 `pm-console`（与 `pm-*` 命名一致，`sync_conventions.sh` 自动覆盖其 CONVENTIONS 副本）。
- 入口命令 `/cmm-pm <项目名 或 想法 | status | next>`。
- 技能 `pipeline-orchestration`：装流水线图谱、`_state.yaml` 规范、看板格式、守门规则（统筹时自动加载）。

## 状态台账 `_runs/<项目slug>/_state.yaml`
唯一跨会话状态源。字段：`project/title/created/next/open_risks/stages{status,artifact,gate}`。
- `status`: pending | in-progress | done
- `gate`: null | passed | revise | pivot
- **以磁盘为准**：台账缺失/过期时，扫 `_runs/<项目>/` 的 `NN-*.md` 反推并重建（§9 不假装）。

## 阶段→命令→产物 映射
01 市场分析 `/market-analysis` → 01-市场分析.md ｜ 02 需求洞察 `/insight` → 02-需求洞察.md ｜ 03 产品战略 `/strategy` → 03-产品战略.md ｜ 04 PRD `/write-prd` → 04-PRD.md ｜ 05 界面设计 `/wireframe` → 05-界面设计.md(+原型.html) ｜ 06 技术方案 `/tech-design` → 06-技术方案.md ｜ 07 用户故事 `/write-stories` → 07-用户故事.md ｜ 08 测试 `/test-scenarios` → 08-测试.md ｜ 09 研发（外部）｜ 10 上线 `/plan-launch` 等 → 10-上线.md ｜ 11 数据/迭代 `/analyze-cohorts` 等 → 11-数据迭代.md（⑪→②闭环）。

## 三种入口行为
- **新项目**：建 `_runs/<slug>/` + 初始台账 → 看板 → 提示敲 `/market-analysis`。
- **续接/status**：读台账（缺失则反推重建）→ 看板 → 推荐 `next`。
- **推进**：扫新产物 → 守门（摘风险结论让用户拍板：放行/调整/pivot）→ 过门才更新 `next` 与台账。

## 关键边界
- 不硬调用跨插件命令（守 No cross-plugin references）——只用人话建议用户去敲 `/xxx`。
- 守门是硬门：gate 未过不放行下一阶段（CONVENTIONS §0a/§0c，用户是决策者）。
- 零侵入：只读阶段产出 md，从不改它们；阶段命令无需知道协同层存在。

## 连带动作（建完）
跑 `validate_plugins.py`（10 插件全过）、`sync_conventions.sh`（同步到 10 插件）、更新 README/README.en/PIPELINE/marketplace（计数与描述）、版本 marketplace 0.2.0→0.3.0、新插件 2.0.0。

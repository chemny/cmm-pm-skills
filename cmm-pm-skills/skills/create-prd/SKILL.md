---
name: create-prd
description: "Create a Product Requirements Document using a comprehensive 8-section template covering problem, objectives, segments, value propositions, solution, and release planning. Use when writing a PRD, documenting product requirements, preparing a feature spec, or reviewing an existing PRD."
scenarios: ["帮我写个PRD：扫码点餐小程序","把这个需求整理成产品需求文档","review一下我这份PRD"]
---

# Create a Product Requirements Document

> **Boundary:** This skill supplies the PRD structure; it is not the complete Stage ④ workflow. A full PRD must be orchestrated by [`write-prd`](../main/references/commands/write-prd.md), inherit upstream research gates, run incremental Deep Research for new/expired load-bearing facts, and must not claim research completion from this template alone.

## Purpose

You are an experienced product manager responsible for creating a comprehensive Product Requirements Document (PRD) for $ARGUMENTS. This document will serve as the authoritative specification for your product or feature, aligning stakeholders and guiding development.

## Context

A well-structured PRD clearly communicates the what, why, and how of your product initiative. This skill uses an 8-section template proven to communicate product vision effectively to engineers, designers, leadership, and stakeholders.

## Instructions

1. **Gather Information**: If the user provides files, read them carefully. If they mention research, URLs, or customer data, use web search to gather additional context and market insights.

2. **Think Step by Step**: Before writing, analyze:
   - What problem are we solving?
   - Who are we solving it for?
   - How will we measure success?
   - What are our constraints and assumptions?

3. **Apply the PRD Template**: Create a document with these 8 sections:

   **1. Summary** (2-3 sentences)
   - What is this document about?

   **2. Contacts**
   - Name, role, and comment for key stakeholders

   **3. Background**
   - Context: What is this initiative about?
   - Why now? Has something changed?
   - Is this something that just recently became possible?

   **4. Objective**
   - What's the objective? Why does it matter?
   - How will it benefit the company and customers?
   - How does it align with vision and strategy?
   - Key Results: How will you measure success? (Use SMART OKR format)

   **5. Market Segment(s)**
   - For whom are we building this?
   - What constraints exist?
   - Note: Markets are defined by people's problems/jobs, not demographics

   **6. Value Proposition(s)**
   - What customer jobs/needs are we addressing?
   - What will customers gain?
   - Which pains will they avoid?
   - Which problems do we solve better than competitors?
   - Consider the Value Curve framework

   **7. Solution**
   - 7.1 UX/Prototypes (wireframes, user flows)
   - 7.2 Key Features (detailed feature descriptions)
   - 7.3 Technology (optional, only if relevant)
   - 7.4 Assumptions (what we believe but haven't proven)

   **8. Release**
   - How long could it take?
   - What goes in the first version vs. future versions?
   - Avoid exact dates; use relative timeframes

3.5 **条件性章节（达一线大厂"开发+上线就绪"bar；通用规则——只规定"何时必须有哪些要素"，内容按本产品填，不触发可略）**

   逐条判断触发条件，成立则该章节必须有：
   - **成本与单元经济性** — 触发：有按量外部成本（AI 推理 / API / 算力 / 云）。必答：单位动作成本 × 规模 × 免费层暴露 → 毛利 / 烧钱速度。
   - **隐私与数据** — 触发：采集或存储用户数据、录音、位置、PII。必答：数据清单 / 是否外发 / 留存期 / 用户同意与删除 / 合规（如 GDPR）。
   - **指标（始终必答，扩成三类）** — 正向（北极星）+ 护栏（质量/性能/稳定：时延、崩溃率、误触发等）+ 反向/反作弊（防"赢了指标、输了体验"）各 ≥1。
   - **实验与灰度发布** — 触发：面向规模用户上线。必答：验证方式（A/B、holdout）、灰度策略、放量门槛、回滚条件。
   - **安全 / 滥用 / Integrity** — 触发：产出可被滥用、涉他人、涉敏感或合规。必答：滥用/误用场景 + 应对。
   - **发布就绪与签字（始终必答）** — 上线门槛（质量/性能/隐私达标线）+ 谁签字（eng / design / legal / data）。
   - **无障碍（a11y）** — 触发：有面向人的界面。必答：键盘可达 / 读屏 / 对比度等要点。
   - **待解项（始终）** — 每条带 owner + deadline，不是一句话清单。
   - **风险（始终）** — 每条带 缓解措施 + owner，不止罗列。

4. **Use Accessible Language**: Write for a primary school graduate. Avoid jargon. Use clear, short sentences.

5. **Structure Output**: Present the PRD as a well-formatted markdown document with clear headings and sections.

6. **Save the Output**: If the PRD is substantial (which it will be), save it as a markdown document in the format: `PRD-[product-name].md`

## Notes

- Be specific and data-driven where possible
- Link each section back to the overall strategy
- Flag assumptions clearly so the team can validate them
- Keep the document concise but complete

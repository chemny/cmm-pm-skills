#!/usr/bin/env bash
# 通用约定的"母版"在 repo 根的 CONVENTIONS.md（唯一编辑入口）。
# 插件按"单个目录"安装，根目录文件不随插件分发，所以插件需内置一份副本。
# 用法：改完根目录 CONVENTIONS.md 后，跑一次本脚本同步进插件。
set -e
cd "$(dirname "$0")"
count=0
for d in cmm-pm/; do
  cp CONVENTIONS.md "${d}CONVENTIONS.md"
  echo "synced -> ${d}CONVENTIONS.md"
  count=$((count+1))
done
echo "完成：已同步到 $count 个插件。"

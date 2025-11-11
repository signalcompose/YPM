#!/bin/bash
set -e

PRIVATE_REPO="/Users/yamato/Src/proj_YPM/YPM-yamato"
PUBLIC_REPO_URL="https://github.com/signalcompose/YPM.git"
EXPORT_DIR="/tmp/ypm-public-export-$(date +%s)"
EXCLUDE_FILE="$PRIVATE_REPO/.export-exclude"

echo "🔍 Exporting YPM to public repository..."
echo "Private repo: $PRIVATE_REPO"
echo "Public repo: $PUBLIC_REPO_URL"
echo "Export dir: $EXPORT_DIR"
echo "Exclude file: $EXCLUDE_FILE"

# Step 1: Fresh cloneを作成
echo "📦 Cloning private repository..."
git clone "$PRIVATE_REPO" "$EXPORT_DIR"
cd "$EXPORT_DIR"

# Step 2: Developブランチをcheckout
git checkout develop

# Step 3: 除外パスを.export-excludeから読み込み
echo "🧹 Filtering sensitive files from history..."
EXCLUDE_PATHS=()
if [[ -f "$EXCLUDE_FILE" ]]; then
  while IFS= read -r line; do
    # コメント行と空行をスキップ
    [[ "$line" =~ ^#.*$ ]] && continue
    [[ -z "$line" ]] && continue
    # 除外パスを配列に追加
    EXCLUDE_PATHS+=(--path "$line" --invert-paths)
  done < "$EXCLUDE_FILE"

  echo "Excluding ${#EXCLUDE_PATHS[@]}/2 paths from export"
else
  echo "⚠️  Warning: $EXCLUDE_FILE not found, using default exclusions"
  EXCLUDE_PATHS=(
    --path PROJECT_STATUS.md --invert-paths
    --path config.yml --invert-paths
    --path CLAUDE.md --invert-paths
    --path docs/research/ --invert-paths
  )
fi

# git filter-repoを実行
git filter-repo "${EXCLUDE_PATHS[@]}" --force

# Step 4: コミットメッセージから機密情報を削除
echo "✏️  Sanitizing commit messages..."
git filter-repo --message-callback '
import re

# messageをdecodeして文字列として扱う
msg = message.decode("utf-8", errors="ignore")

# プロジェクト名を[project]に置換
projects = ["oshireq", "orbitscore", "picopr", "TabClear", "DUNGIA", "godot-mcp", "YPM-yamato"]
for proj in projects:
    msg = msg.replace(proj, "[project]")

# プロジェクト数を[N]に置換
msg = re.sub(r"\d+プロジェクト", r"[N]プロジェクト", msg)
msg = re.sub(r"\d+ projects", r"[N] projects", msg)

# 時刻情報を削除
msg = re.sub(r"\d+分前", r"[時間]前", msg)
msg = re.sub(r"\d+日前", r"[日数]前", msg)

return msg.encode("utf-8")
' --force

# Step 5: Public repoにpush
echo "🚀 Pushing to public repository..."
git remote add public "$PUBLIC_REPO_URL"
git push public develop:main --force

echo ""
echo "✅ Export completed successfully!"
echo "⚠️  Please verify the public repository manually:"
echo "    https://github.com/signalcompose/YPM"
echo ""
echo "Next steps:"
echo "1. Check commit history: cd $EXPORT_DIR && git log --oneline"
echo "2. Verify no sensitive information: git show"
echo "3. Clean up: rm -rf $EXPORT_DIR"

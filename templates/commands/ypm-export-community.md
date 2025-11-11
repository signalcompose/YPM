# /ypm-export-community - Export Private Repository to Public Community Version

このコマンドは、privateリポジトリからpublicコミュニティ版へexportします。

初回実行時は対話形式でセットアップを行い、2回目以降は自動的にexportを実行します。

## あなたの役割

以下の手順を**厳密に**実行してください：

---

### STEP 1: 現在のディレクトリとブランチを確認

```bash
pwd
git branch --show-current
```

現在のディレクトリを確認し、ユーザーに報告してください。

---

### STEP 2: 設定ファイルの存在チェック

```bash
ls -la .export-config.yml 2>/dev/null || echo "NOT_FOUND"
```

**判定**:
- `.export-config.yml`が**存在する** → **STEP 4へスキップ**
- `.export-config.yml`が**存在しない** → **STEP 3へ進む**

---

### STEP 3: インタラクティブセットアップ（初回のみ）

**AskUserQuestionツール**を使用して、以下の情報を収集してください：

#### Question 1: Repository Configuration

**質問内容**:
```
Private repositoryとPublic repositoryの設定を行います。
```

**選択肢**:
1. **Private repo path**:
   - Label: "Current directory"
   - Description: "Use current directory as private repo ({{current_dir}})"

2. **Private repo path (custom)**:
   - Label: "Custom path"
   - Description: "Specify different path (e.g., for Git worktree main branch)"

3. **Public repo (new)**:
   - Label: "Create new public repository"
   - Description: "Create a new public GitHub repository"

4. **Public repo (existing)**:
   - Label: "Use existing repository"
   - Description: "Use an existing public repository URL"

**収集する情報**:
- Private repo path（カレントディレクトリまたはカスタムパス）
- Public repo URL（新規作成の場合はowner/name、既存の場合はURL）

#### Question 2: Files to Exclude

**質問内容**:
```
Public版から除外するファイルを選択してください。
推奨される除外ファイルがデフォルトで選択されています。
```

**選択肢（multiSelect: true）**:
1. **CLAUDE.md**:
   - Label: "CLAUDE.md"
   - Description: "Personal Claude Code configuration (recommended)"

2. **config.yml**:
   - Label: "config.yml"
   - Description: "Personal configuration with local paths (recommended)"

3. **PROJECT_STATUS.md**:
   - Label: "PROJECT_STATUS.md"
   - Description: "Personal project management data (recommended)"

4. **docs/research/**:
   - Label: "docs/research/"
   - Description: "Internal research documents (recommended)"

5. **Additional files**:
   - Label: "Other files"
   - Description: "Specify additional files in the next step"

**追加除外ファイル**（Otherを選択した場合）:
- ユーザーに追加の除外ファイルをカンマ区切りで入力してもらう

#### Question 3: Commit Message Sanitization

**質問内容**:
```
コミットメッセージから削除したい機密キーワードがあれば指定してください。
（例: プロジェクト名、内部コードネーム等）
```

**選択肢**:
1. **No sanitization**:
   - Label: "Skip"
   - Description: "No sensitive keywords to sanitize"

2. **Add keywords**:
   - Label: "Add keywords"
   - Description: "Specify sensitive keywords to redact"

**収集する情報**:
- 機密キーワードのリスト（カンマ区切り）

---

#### STEP 3-2: .export-config.yml を作成

**Writeツール**を使用して、収集した情報から`.export-config.yml`を生成してください。

**フォーマット**:
```yaml
# Export Configuration for [プロジェクト名]
# Generated: [今日の日付: 2025-11-12]

export:
  # Private repository path (absolute path)
  private_repo: "[Step 3で収集したprivate_repo_path]"

  # Public repository URL
  public_repo_url: "[Step 3で収集したpublic_repo_url]"

  # Files and directories to exclude from export
  exclude_paths:
    - CLAUDE.md           # Personal configuration
    - config.yml          # Personal paths
    - PROJECT_STATUS.md   # Personal project data
    - docs/research/      # Internal research documents
    [追加の除外ファイルがあればここに追加]

  # Commit message sanitization patterns
  sanitize_patterns:
    [機密キーワードがある場合]
    - pattern: "[keyword1|keyword2|keyword3]"
      replace: "[redacted]"
    [機密キーワードがない場合]
    # No sanitization patterns specified
```

**作成後**:
- `.export-config.yml`が作成されたことをユーザーに報告
- 内容を確認してもらう
- **STEP 4へ進む**

---

### STEP 4: Export実行

**.export-config.yml**が存在する場合、以下を実行：

#### STEP 4-1: 設定内容の確認

```bash
yq eval '.export' .export-config.yml
```

設定内容をユーザーに提示してください。

#### STEP 4-2: Export実行の確認

**重要**: エクスポートスクリプトは以下の操作を行います：
- Public repositoryの作成（存在しない場合）
- ブランチ保護設定の適用
- Git履歴の書き換え（機密ファイル除外）
- PRの自動作成
- TruffleHogセキュリティスキャン

ユーザーに以下を確認してください：
```
以下の設定でpublic版へexportします：

- Private repo: [private_repo の値]
- Public repo: [public_repo_url の値]
- 除外ファイル: [exclude_paths のリスト]

このexportを実行しますか？
```

#### STEP 4-3: スクリプト実行

ユーザーが承認した場合のみ、以下を実行：

```bash
~/.claude/scripts/export-to-community.sh
```

**注意**:
- スクリプトがインタラクティブ入力を求めた場合、ユーザーに報告して手動実行を依頼
- `.export-config.yml`が存在すれば、スクリプトはインタラクティブセットアップをスキップするはず

---

### STEP 5: 結果報告

スクリプト実行後：
1. 実行結果を確認
2. PR URLをユーザーに報告
3. TruffleHogセキュリティスキャン結果を報告
4. **PRのマージについては必ずユーザーに確認すること**
5. マージ承認を得た場合のみ、マージを実行

---

## 重要な注意事項

- **PRマージは必ずユーザーの承認を得てから実行**（絶対禁止事項）
- 依存ツール: `git-filter-repo`, `yq`, `gh` (GitHub CLI), `trufflehog`
- GitHub権限が必要（repository作成、branch protection設定）
- 初回セットアップは対話形式で丁寧に進める
- 2回目以降は設定ファイルを読み込んで即座に実行

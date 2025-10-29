# YPM - Open Project in Editor

YPMで管理しているプロジェクトを指定したエディタで開きます。

## サブコマンド

- **(引数なし)**: ignore除外の一覧から選択（デフォルトエディタで開く）
- `<プロジェクト名> [エディタ名]`: プロジェクトを指定エディタで開く
- `all`: ignore含む全プロジェクトから選択
- `ignore-list`: ignore設定済みプロジェクト一覧表示
- `add-ignore`: プロジェクトをignoreに追加
- `remove-ignore`: ignoreから削除
- `--editor [エディタ名]`: デフォルトエディタの設定・表示

## 使用例

```
/ypm-open                    # 通常モード（デフォルトエディタ）
/ypm-open oshireq           # oshireqをデフォルトエディタで開く
/ypm-open oshireq cursor    # oshireqをCursorで開く
/ypm-open all               # 全表示モード
/ypm-open --editor          # 現在のデフォルトエディタを表示
/ypm-open --editor cursor   # デフォルトをCursorに設定
/ypm-open ignore-list       # ignore一覧
/ypm-open add-ignore        # ignoreに追加
/ypm-open remove-ignore     # ignoreから削除
```

**対応エディタ**: `code` (VS Code), `cursor` (Cursor), `zed` (Zed)

---

## 実行手順

### 共通STEP: 引数の確認

引数を確認し、対応するモードに分岐：
- 引数なし → **モード1: 通常モード**
- `<プロジェクト名> [エディタ名]` → **モード1: 通常モード**（直接プロジェクト指定）
- `all` → **モード2: 全表示モード**
- `ignore-list` → **モード3: ignore一覧**
- `add-ignore` → **モード4: ignore追加**
- `remove-ignore` → **モード5: ignore削除**
- `--editor [エディタ名]` → **モード6: エディタ設定**

---

## モード1: 通常モード（引数なし または プロジェクト名指定）

### STEP 1: config.ymlとエディタCLIの確認

#### 1-1. config.ymlからデフォルトエディタを取得

```bash
# config.ymlを読み込み
# editor.default の値を取得（例: code, cursor, zed）
```

#### 1-2. 第2引数がある場合、エディタを上書き

- 第2引数 (`cursor`, `code`, `zed` 等) が指定されている場合、そのエディタを使用
- 第2引数がない場合、config.ymlのデフォルトを使用

#### 1-3. エディタCLIの確認

```bash
which <エディタ名>
```

**結果が空の場合**:
```
❌ <エディタ名> CLI が見つかりません。

<エディタ名>のCLIをインストールしてください。

【VS Code (code)】
1. VS Codeを開く
2. Command Palette (Cmd+Shift+P)
3. "Shell Command: Install 'code' command in PATH" を実行

【Cursor (cursor)】
1. Cursorを開く
2. Command Palette (Cmd+Shift+P)
3. "Shell Command: Install 'cursor' command in PATH" を実行

【Zed (zed)】
1. Zedを開く
2. Command Palette (Cmd+Shift+P)
3. "zed: Install CLI" を実行

インストール後、再度このコマンドを実行してください。
```
→ **処理を中断**

### STEP 2: PROJECT_STATUS.mdとconfig.ymlの読み込み

```bash
# ReadツールでPROJECT_STATUS.mdを読み込み
# Readツールでconfig.ymlを読み込み
```

**PROJECT_STATUS.mdが存在しない場合**:
```
❌ PROJECT_STATUS.md が見つかりません。

先に /ypm-update を実行してプロジェクトをスキャンしてください。
```
→ **処理を中断**

### STEP 3: プロジェクト一覧の抽出と除外

#### 3-1. PROJECT_STATUS.mdから抽出

1. **アクティブプロジェクト**（`## 🔥 アクティブプロジェクト` セクション）
2. **開発中プロジェクト**（`## 🚧 開発中` セクション）
3. **休止中プロジェクト**（`## 💤 休止中` セクション）

**抽出ルール**:
- `### プロジェクト名` の行からプロジェクト名を取得
- `- **概要**: ...` から簡単な説明を取得
- `- **実装進捗**: XX%` から進捗を取得
- `- **ドキュメント**: [...]` からプロジェクトパスを抽出
  - 例: `[CLAUDE.md](/Users/yamato/Src/proj_max_mcp/MaxMCP/CLAUDE.md)`
  - → プロジェクトパス: `/Users/yamato/Src/proj_max_mcp/MaxMCP`

#### 3-2. Git worktreeの除外

以下の条件に**いずれか**該当するプロジェクトは除外：
- プロジェクト名が `-main` で終わる
- プロジェクト名が `-develop` で終わる
- 概要に「worktree」が含まれる

#### 3-3. ignore_in_openの除外（通常モードのみ）

config.ymlの`monitor.ignore_in_open`リストに含まれるプロジェクトを除外。

### STEP 4: 番号付き一覧表示

```
## 利用可能なプロジェクト（12個）

### 🔥 アクティブ（1週間以内に更新）
1. Slack_MCP - Slack-Claude Bridge MCP（v1.0.0リリース準備中、95%）
2. CVI - Claude Voice Integration（v2.0.0リリース済み、100%）
3. MaxMCP - Max/MSP用ネイティブMCPサーバー（実装中、35%）
4. MaxMSP-MCP-Server-multipatch - Max/MSP MCPサーバー研究版（80%）
5. picopr - メールマガジン自動化システム（15%）
6. redmine-mcp-server - Redmine REST API MCPサーバー（100%）
7. InstrVo - 楽器演奏を歌声に変換（MVP開発、70%）
8. Claude-code - Claude Code活用ガイド
9. git-dotfiles-manager - プライベート設定ファイル管理（90%）
10. TabClear - P2Pタブ管理・共有システム（設計段階、5%）
11. oshireq - 推し活リクエスト（本番稼働中）

### 🚧 開発中（1ヶ月以内に更新）
12. DUNGIA - ダンジョンタイムアタックゲーム（設計中、0%）
13. my_first_turnip - 自動取引PDCAシステム（実験段階、30%）
14. orbitscore - ライブコーディングDSL（オーディオ実装、20%）

※ 非表示: 2個（全て表示: /ypm-open all）

番号またはプロジェクト名を入力してください:
```

### STEP 5: ユーザー入力処理

**入力パターン**:

#### 5-1. 番号入力（例: `3`）
- 該当番号のプロジェクトを選択 → STEP 6へ

#### 5-2. プロジェクト名入力（例: `max`）
- 大文字小文字を区別せず部分一致検索
- **1件マッチ**: そのプロジェクトを選択 → STEP 6へ
- **複数マッチ**:
  ```
  複数のプロジェクトがマッチしました：

  1. MaxMCP
  2. MaxMSP-MCP-Server-multipatch

  番号を入力してください:
  ```
  → 再度番号入力を待つ → STEP 6へ

- **0件マッチ**:
  ```
  ❌ プロジェクト "xxx" が見つかりませんでした。

  正確なプロジェクト名または番号を指定してください。
  ```
  → **処理を中断**

### STEP 6: エディタでプロジェクトを開く

**重要**: 環境変数をクリアしてエディタを起動します。これにより、各プロジェクトの`.node-version`等が正しく読み込まれます。

```bash
env -u NODENV_VERSION -u NODENV_DIR -u RBENV_VERSION -u PYENV_VERSION <エディタ名> /path/to/project
```

**クリアする環境変数**:
- `NODENV_VERSION` - Node.jsバージョン（nodenv）
- `NODENV_DIR` - nodenvディレクトリ
- `RBENV_VERSION` - Rubyバージョン（rbenv）
- `PYENV_VERSION` - Pythonバージョン（pyenv）

**成功時のメッセージ**:
```
✅ <エディタ表示名>で "MaxMCP" を開きました。

プロジェクトパス: /Users/yamato/Src/proj_max_mcp/MaxMCP
エディタ: <エディタ表示名> (<エディタ名>)

※ 環境変数（NODENV_VERSION等）をクリアした状態で起動しました。
各プロジェクトの設定ファイル（.node-version等）が正しく読み込まれます。
```

**エディタ表示名の対応**:
- `code` → "VS Code"
- `cursor` → "Cursor"
- `zed` → "Zed"

**失敗時のメッセージ**:
```
❌ <エディタ表示名>の起動に失敗しました。

エラー: <エラーメッセージ>

手動で以下のコマンドを実行してください：
env -u NODENV_VERSION -u NODENV_DIR -u RBENV_VERSION -u PYENV_VERSION <エディタ名> /Users/yamato/Src/proj_max_mcp/MaxMCP
```

---

## モード2: 全表示モード（`/ypm-open all`）

### 処理

**STEP 1-2**: モード1と同じ

**STEP 3**: プロジェクト抽出
- worktreeは除外
- **ignore_in_openは除外しない**（これが通常モードとの違い）

**STEP 4**: 番号付き一覧表示（ignore含む）

```
## 利用可能なプロジェクト（全16個）

### 🔥 アクティブ
1-11. （通常モードと同じ）

### 🚧 開発中
12-14. （通常モードと同じ）

### 💤 休止中・その他（ignore設定済み）
15. godot-mcp - Godot Engine向けMCPサーバー（休止中）
16. loto7loto6Generator - ロト番号生成ツール（レガシー、完成済み）

番号またはプロジェクト名を入力してください:
```

**STEP 5-6**: モード1と同じ

---

## モード3: ignore一覧（`/ypm-open ignore-list`）

### 処理

```bash
# config.ymlを読み込み
# monitor.ignore_in_openセクションを抽出
```

**表示**:
```
## Ignore設定済みプロジェクト

1. godot-mcp
2. loto7loto6Generator

削除: /ypm-open remove-ignore
追加: /ypm-open add-ignore
```

**ignore_in_openが空の場合**:
```
✅ 現在ignoreに設定されているプロジェクトはありません。

追加: /ypm-open add-ignore
```

---

## モード4: ignore追加（`/ypm-open add-ignore`）

### STEP 1-3: モード1と同じ（通常モード）

### STEP 4: プロジェクト一覧表示

```
## ignoreに追加するプロジェクトを選択

現在表示中のプロジェクト（12個）:
1. Slack_MCP
2. CVI
3. MaxMCP
...
14. orbitscore

番号またはプロジェクト名を入力してください:
```

### STEP 5: プロジェクト選択（モード1と同じ）

### STEP 6: config.ymlに追加

選択されたプロジェクト名を`monitor.ignore_in_open`リストに追加。

```yaml
monitor:
  ignore_in_open:
    - godot-mcp
    - loto7loto6Generator
    - orbitscore  # 追加
```

**成功メッセージ**:
```
✅ "orbitscore" をignoreに追加しました。

config.ymlを更新:
  monitor.ignore_in_open:
    - godot-mcp
    - loto7loto6Generator
    - orbitscore

次回から /ypm-open では表示されません。
全て表示: /ypm-open all
```

---

## モード5: ignore削除（`/ypm-open remove-ignore`）

### STEP 1: config.yml読み込み

```bash
# config.ymlを読み込み
# monitor.ignore_in_openセクションを抽出
```

**ignore_in_openが空の場合**:
```
✅ 現在ignoreに設定されているプロジェクトはありません。

追加: /ypm-open add-ignore
```
→ **処理を中断**

### STEP 2: ignore一覧表示

```
## ignoreから削除するプロジェクトを選択

1. godot-mcp
2. loto7loto6Generator
3. orbitscore

番号またはプロジェクト名を入力してください:
```

### STEP 3: プロジェクト選択

番号または名前で選択（モード1のSTEP 5と同じロジック）

### STEP 4: config.ymlから削除

選択されたプロジェクト名を`monitor.ignore_in_open`リストから削除。

```yaml
monitor:
  ignore_in_open:
    - godot-mcp
    - loto7loto6Generator
    # orbitscoreを削除
```

**成功メッセージ**:
```
✅ "orbitscore" をignoreから削除しました。

config.ymlを更新:
  monitor.ignore_in_open:
    - godot-mcp
    - loto7loto6Generator

次回から /ypm-open で表示されます。
```

---

## モード6: エディタ設定（`/ypm-open --editor [エディタ名]`）

### STEP 1: 引数の確認

#### 引数がない場合（`/ypm-open --editor`）

現在のデフォルトエディタを表示します。

```bash
# config.ymlを読み込み
# editor.default の値を取得
```

**表示メッセージ**:
```
📝 現在のデフォルトエディタ

エディタ: VS Code (code)

変更方法: /ypm-open --editor <エディタ名>
対応エディタ: code (VS Code), cursor (Cursor), zed (Zed)
```

#### 引数がある場合（`/ypm-open --editor cursor`）

デフォルトエディタを変更します。

### STEP 2: エディタ名のバリデーション

指定されたエディタ名が対応しているか確認します。

**対応エディタ**:
- `code` - VS Code
- `cursor` - Cursor
- `zed` - Zed

**対応していない場合**:
```
❌ 未対応のエディタです: "xxx"

対応エディタ:
- code (VS Code)
- cursor (Cursor)
- zed (Zed)

使用例: /ypm-open --editor cursor
```
→ **処理を中断**

### STEP 3: config.ymlの更新

`editor.default`の値を指定されたエディタ名に変更します。

```yaml
# 変更前
editor:
  default: code

# 変更後
editor:
  default: cursor
```

### STEP 4: 成功メッセージ

```
✅ デフォルトエディタを変更しました

変更前: VS Code (code)
変更後: Cursor (cursor)

config.ymlを更新:
  editor.default: cursor

次回から /ypm-open で Cursor が使用されます。
```

---

## 重要な注意事項

### 1. Git worktreeの除外

Git worktree（例: `MaxMCP-main`, `redmine-mcp-server-main`, `InstrVo-develop`）は**全モードで自動的に除外**されます。これらは開発用ではなく確認用のため、選択肢に含めません。

### 2. ignoreとexcludeの違い

- **exclude**: スキャン対象から完全に除外（PROJECT_STATUS.mdにも表示されない）
- **ignore_in_open**: スキャン対象だが、ypm-openでデフォルト非表示（allで表示可能）

### 3. config.ymlの保存

ignore追加・削除時、エディタ設定変更時は、config.ymlファイルを**必ず保存**してください。Writeツールを使用します。

### 4. PROJECT_STATUS.mdの更新

プロジェクト一覧が古い場合、先に `/ypm-update` を実行してください。

### 5. エディタCLIのインストール

各エディタのCLIがインストールされていない場合、プロジェクトを開くことができません。STEP 1でインストール方法を案内します。

---

## エラーハンドリング

| エラー | 対処法 |
|--------|--------|
| エディタCLIがない | インストール手順を表示して中断 |
| 未対応のエディタ | 対応エディタ一覧を表示して中断 |
| PROJECT_STATUS.mdがない | `/ypm-update` の実行を促して中断 |
| config.ymlがない | エラーメッセージを表示して中断 |
| プロジェクトが見つからない | エラーメッセージを表示して中断 |
| 複数マッチ | 候補を番号付きで再表示 |
| エディタ起動失敗 | エラーメッセージと手動コマンドを表示 |

---

## 仕様書

詳細な仕様は以下を参照：
- **[docs/development/ypm-open-spec.md](../../docs/development/ypm-open-spec.md)**

---

**このコマンドを実行した後、必ず成功/失敗メッセージをユーザーに表示してください。**

# グローバルエクスポートシステム

## 概要

グローバルエクスポートシステムは、privateリポジトリからpublicコミュニティ版へのexport機能をグローバルシステムとして実装したものです。YPM、MaxMCP、その他任意のプロジェクトで使用可能です。

## システム構成

### 1. グローバルスクリプト

**ファイル**: `~/.claude/scripts/export-to-community.sh`

汎用的なprivate→public export機能を提供：
- 各プロジェクトの`.export-config.yml`を読み込み
- git-filter-repoでファイル除外＋コミットメッセージサニタイズ
- 自動PR作成
- TruffleHogセキュリティスキャン（自動）
- インタラクティブマージ（オプション）
- 自動クリーンアップ

### 2. グローバルコマンド

**ファイル**: `~/.claude/commands/ypm-export-community.md`

どのプロジェクトからも`/ypm-export-community`で実行可能なClaude Code slash command。

### 3. 設定ファイル

各プロジェクトのルートに`.export-config.yml`を配置：

```yaml
export:
  private_repo: "/path/to/private"
  public_repo_url: "https://github.com/org/public.git"
  exclude_paths:
    - CLAUDE.md
    - docs/research/
  sanitize_patterns:
    - pattern: "sensitive"
      replace: "[redacted]"
```

## インストール手順

### Step 1: グローバルスクリプトのインストール

```bash
# YPMリポジトリからテンプレートをコピー
cp /path/to/YPM/templates/scripts/export-to-community.sh ~/.claude/scripts/
chmod +x ~/.claude/scripts/export-to-community.sh
```

### Step 2: グローバルコマンドのインストール

```bash
# YPMリポジトリからテンプレートをコピー
cp /path/to/YPM/templates/commands/ypm-export-community.md ~/.claude/commands/
```

**注意**: グローバルコマンドを認識させるには、Claude Codeの再起動が必要です。

### Step 3: 依存ツールのインストール

```bash
# yq (YAML parser)
brew install yq

# git-filter-repo (Git history rewriting)
brew install git-filter-repo

# TruffleHog (Security scanner)
brew install trufflehog
```

### Step 4: プロジェクトごとの設定

各プロジェクトで`.export-config.yml`を作成：

```bash
# サンプルからコピー
cp .export-config.yml.example .export-config.yml

# 自分の環境に合わせて編集
vim .export-config.yml
```

**重要**: `.export-config.yml`は個人のパスを含むため、`.gitignore`に追加してください。

## 使い方

### 基本的な使用方法

1. プロジェクトのルートディレクトリに移動
2. Claude Codeで`/ypm-export-community`を実行
3. 設定内容を確認して承認
4. スクリプトが自動実行される

### ワークフロー

```
1. プロジェクトをクローン
   ↓
2. 機密ファイルを除外（git-filter-repo）
   ↓
3. コミットメッセージをサニタイズ
   ↓
4. featureブランチを作成してpush
   ↓
5. PR自動作成
   ↓
6. TruffleHogセキュリティスキャン（自動）
   ↓
7. インタラクティブマージプロンプト
   - "y"選択 → 自動マージ + クリーンアップ
   - "n"選択 → 手動マージの手順を表示
```

## 機能詳細

### Step 7: Security Verification

**TruffleHogセキュリティスキャン**を自動実行：
- Verified Secrets: 0
- Unverified Secrets: 0

**結果**:
- ✅ スキャンパス → インタラクティブマージへ進む
- ❌ スキャン失敗 → 手動マージが必要（プロンプト表示）

**TruffleHog未インストールの場合**:
- 警告メッセージを表示
- インストール手順を表示
- 手動マージの手順を表示

### Step 8: Interactive Merge

セキュリティスキャンが通過した場合のみ、以下のプロンプトが表示されます：

```
Merge PR now? (y/n):
```

**"y"を選択**:
1. 自動的にPRをマージ（`gh pr merge --merge --delete-branch`）
2. 一時ディレクトリを自動クリーンアップ
3. 完了サマリーを表示

**"n"を選択**:
1. 手動マージの手順を表示
2. 一時ディレクトリはそのまま残る（手動クリーンアップが必要）

### Step 9: Cleanup

自動マージを選択した場合のみ実行：
- 元のディレクトリに戻る
- `/tmp/ypm-public-export-XXXXXXXXXX`を削除
- 完了メッセージを表示

## トラブルシューティング

### Q: コマンドが表示されない

**A**: Claude Codeを再起動してください。グローバルコマンドの読み込みには再起動が必要です。

### Q: TruffleHogが見つからない

**A**: 以下でインストール：
```bash
brew install trufflehog
```

### Q: セキュリティスキャンで問題が検出された

**A**:
1. PRをマージせずに手動で確認
2. `/tmp/ypm-public-export-XXXXXXXXXX`で問題箇所を特定
3. `.export-config.yml`の`exclude_paths`や`sanitize_patterns`を修正
4. 再度exportを実行

### Q: マージ後にエラーが発生した

**A**:
- PRは既にマージされているため、手動でクリーンアップ：
  ```bash
  rm -rf /tmp/ypm-public-export-XXXXXXXXXX
  ```

## セキュリティ考慮事項

1. **機密情報の除外**
   - CLAUDE.md（個人設定）
   - config.yml（個人パス）
   - docs/research/（内部ドキュメント）

2. **コミットメッセージのサニタイズ**
   - プロジェクト名 → `[project]`
   - 統計情報 → `[N]`
   - タイムスタンプ → `[time]`

3. **自動検証**
   - TruffleHogによる全履歴スキャン
   - 検証済みシークレット: 0を確認
   - 未検証シークレット: 0を確認

## 他プロジェクトでの使用例

### MaxMCP

```yaml
# MaxMCP/.export-config.yml
export:
  private_repo: "/Users/yamato/Src/proj_MaxMCP/MaxMCP-yamato"
  public_repo_url: "https://github.com/signalcompose/MaxMCP.git"
  exclude_paths:
    - CLAUDE.md
    - config.yml
    - docs/research/
  sanitize_patterns:
    - pattern: "internal-project-name"
      replace: "[project]"
```

### 任意のプロジェクト

1. `.export-config.yml`を作成
2. `/ypm-export-community`を実行
3. 完了

## 今後の改善案

- [ ] ドライランモード（実際のpushなしでテスト）
- [ ] 複数リポジトリの一括export
- [ ] export履歴の管理
- [ ] カスタムセキュリティスキャンルール

## 関連ドキュメント

- [Private-to-Public Strategy](../research/private-to-public-strategy.md)
- [Issue #4](https://github.com/signalcompose/YPM/issues/4) - Auto-merge機能追加
- [Issue #45](https://github.com/signalcompose/YPM/pull/45) - グローバルエクスポートシステム実装

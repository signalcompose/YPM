# /ypm-export-community - Export Private Repository to Public Community Version

このコマンドは、グローバルエクスポートスクリプトを実行して、privateリポジトリからpublicコミュニティ版へexportします。

**YPM v1.3以降**: スクリプトはインタラクティブセットアップに対応しています。
- 初回実行時: 自動的に4ステップのセットアップウィザードが起動
- 2回目以降: `.export-config.yml`が存在すれば即座にexport開始

## あなたの役割

以下の手順を実行してください：

### STEP 1: 現在のディレクトリ確認

```bash
pwd
```

現在のディレクトリがexportしたいプロジェクトのルートディレクトリであることを確認してください。

### STEP 2: スクリプト実行

```bash
~/.claude/scripts/export-to-community.sh
```

**スクリプトの動作**:

#### 初回実行（`.export-config.yml`が存在しない場合）
スクリプトが自動的にインタラクティブセットアップを開始します：
1. **Step 1/4**: Private repositoryパスの確認
2. **Step 2/4**: Public repository URL（新規作成または既存URL）
3. **Step 3/4**: 除外ファイルの設定（推奨値が自動追加）
4. **Step 4/4**: コミットメッセージのサニタイズパターン

セットアップ完了後、`.export-config.yml`が生成され、自動的にexportが開始されます。

#### 2回目以降（`.export-config.yml`が存在する場合）
設定ファイルを読み込み、即座にexportを開始します：
1. Public repoの存在確認
2. ブランチ保護設定の確認・適用
3. Export実行

### STEP 3: 結果報告

スクリプト実行後：
1. 実行結果を確認
2. PR URLをユーザーに報告
3. TruffleHogセキュリティスキャン結果を報告
4. **PRのマージについては必ずユーザーに確認すること**

## 注意事項

- mainブランチで実行する必要があります
- 依存ツール: `git-filter-repo`, `yq`, `gh` (GitHub CLI), `trufflehog`
- GitHub Admin権限が必要です（branch protection設定のため）
- **PRマージは必ずユーザーの承認を得てから実行**

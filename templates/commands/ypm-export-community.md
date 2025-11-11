# /ypm-export-community - Export Private Repository to Public Community Version

このコマンドは、グローバルエクスポートスクリプトを実行して、privateリポジトリからpublicコミュニティ版へexportします。

## あなたの役割

以下の手順を実行してください：

### STEP 1: 事前確認

1. 現在のディレクトリを確認（`pwd`）
2. `.export-config.yml`が存在するか確認
3. 設定ファイルの内容を確認（`yq eval '.export' .export-config.yml`）

### STEP 2: ユーザーに確認

以下の情報をユーザーに提示して、実行の承認を得てください：

```
以下の設定でpublic版へexportします：

- Private repo: [private_repo の値]
- Public repo: [public_repo_url の値]
- 除外ファイル: [exclude_paths のリスト]

このexportを実行しますか？

⚠️ 注意: このコマンドはpublic repositoryに force push を実行します。
```

### STEP 3: スクリプト実行

ユーザーが承認した場合のみ、以下を実行：

```bash
~/.claude/scripts/export-to-community.sh
```

### STEP 4: 結果報告

スクリプト実行後：
1. 実行結果を確認
2. 一時ディレクトリのパスを報告
3. ユーザーに手動検証を促す

## 注意事項

- mainブランチで実行する必要があります
- git-filter-repo と yq がインストールされている必要があります
- GitHub Admin権限が必要です（force push実行のため）

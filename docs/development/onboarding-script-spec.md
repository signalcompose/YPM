# オンボーディングスクリプト仕様書

**最終更新**: 2025-10-16

---

## 目次

- [目的](#目的)
- [ユーザージャーニー](#ユーザージャーニー)
- [機能要件](#機能要件)
- [入力仕様](#入力仕様)
- [出力仕様](#出力仕様)
- [エラーハンドリング](#エラーハンドリング)
- [実装要件](#実装要件)

---

## 目的

新規ユーザーがYPMを初めて使用する際に、対話的に必要な情報を収集し、`config.yml`を自動生成するウィザードスクリプト。

### 解決する課題

1. **設定ファイルの手動編集が難しい**
   - YAMLの文法エラー
   - パスの書き方がわからない
   - 設定項目の意味が不明

2. **Claude Codeにとっても不確実**
   - 自然言語での設定は解釈の余地がある
   - バリデーションが困難

3. **再現性の欠如**
   - 誰が設定しても同じ品質を保証できない

### 目標

- ✅ 誰でも迷わずセットアップできる
- ✅ 確実にバリデーションされたconfig.ymlを生成
- ✅ Claude Codeが安心して実行できる

---

## ユーザージャーニー

### 理想的なフロー

```
1. ユーザー: YPMをクローン
   ↓
2. ユーザー: Claude Codeを起動
   ↓
3. Claude Code: "config.ymlが存在しません。オンボーディングスクリプトを実行してセットアップしますか？"
   ↓
4. ユーザー: "はい"
   ↓
5. Claude Code: `python scripts/onboarding.py` 実行
   ↓
6. スクリプト: ウェルカムメッセージ表示
   ↓
7. スクリプト: "監視したいプロジェクトディレクトリのパスを入力してください:"
   ↓
8. ユーザー: "/Users/yamato/Projects"
   ↓
9. スクリプト: パス存在確認 → ディレクトリ構造をスキャン
   ↓
10. スクリプト: "以下のプロジェクト検出パターンを提案します:"
    1. * (直下の全プロジェクト)
    2. work/* (workディレクトリ配下)
    3. カスタムパターンを入力
    ↓
11. ユーザー: "1"
    ↓
12. スクリプト: "アクティブプロジェクトの基準日数を入力してください [7]:"
    ↓
13. ユーザー: (Enterでデフォルト)
    ↓
14. スクリプト: config.yml生成
    ↓
15. スクリプト: "初回のPROJECT_STATUS.mdを生成しますか？ [Y/n]:"
    ↓
16. ユーザー: "Y"
    ↓
17. スクリプト: PROJECT_STATUS.md生成
    ↓
18. スクリプト: 完了レポート表示
    ↓
19. Claude Code: "セットアップが完了しました。監視対象は..."
```

---

## 機能要件

### 必須機能

#### 1. 監視対象ディレクトリの設定

**入力プロンプト**:
```
監視したいプロジェクトディレクトリのパスを入力してください:
（例: /Users/yourname/Projects, ~/workspace）
> 
```

**バリデーション**:
- パスが存在するか確認
- ディレクトリであるか確認
- 読み取り権限があるか確認
- `~`を展開する

**エラーメッセージ**:
- "エラー: ディレクトリが存在しません: {path}"
- "エラー: 読み取り権限がありません: {path}"

#### 2. プロジェクト検出パターンの提案

**ロジック**:
1. 指定されたディレクトリをスキャン
2. 実際のディレクトリ構造を解析
3. パターンを提案

**提案例**:
```
以下のプロジェクト検出パターンを提案します:

ディレクトリ構造:
  /Users/yamato/Projects/
  ├── project1/
  ├── project2/
  └── work/
      ├── client-a/
      └── client-b/

推奨パターン:
  1. * (直下の全プロジェクト: project1, project2, work)
  2. work/* (workディレクトリ配下: client-a, client-b)
  3. */* (2階層: project1/*, project2/*, work/*)
  4. カスタムパターンを入力

選択してください [1]:
> 
```

#### 3. 分類基準の設定

**入力プロンプト**:
```
アクティブプロジェクトの基準日数を入力してください [7]:
（何日以内に更新されたプロジェクトを「アクティブ」とするか）
> 
```

**デフォルト値**: 7日

```
休止中プロジェクトの基準日数を入力してください [30]:
（何日以上更新されていないプロジェクトを「休止中」とするか）
> 
```

**デフォルト値**: 30日

**バリデーション**:
- 正の整数であるか
- active_days < inactive_days であるか

#### 4. config.yml生成

**テンプレート**:
```yaml
# YPM設定ファイル
# 自動生成日時: {timestamp}

monitor:
  directories:
    - {user_input_directory}
  
  exclude:
    - proj_YPM/YPM
  
  patterns:
    - {selected_pattern}

classification:
  active_days: {user_input_active_days}
  inactive_days: {user_input_inactive_days}

progress:
  phase_0: 0-20
  phase_1: 20-30
  phase_2: 30-60
  phase_3: 60-80
  phase_4: 80-100

settings:
  include_non_git: false
  doc_priority:
    - CLAUDE.md
    - README.md
    - docs/INDEX.md
```

#### 5. 初回PROJECT_STATUS.md生成（オプション）

**入力プロンプト**:
```
初回のPROJECT_STATUS.mdを生成しますか？ [Y/n]:
（Claude Codeを使わずに、今すぐプロジェクト情報をスキャンします）
> 
```

**ロジック**:
- Gitリポジトリをスキャン
- 基本情報を収集（ブランチ、最終コミット日時）
- PROJECT_STATUS.mdを生成

**スキップ条件**:
- ユーザーが"n"を選択
- Claude Codeに任せる場合

---

## 入力仕様

### 1. 監視対象ディレクトリ

| 項目 | 値 |
|-----|---|
| 型 | 文字列（パス） |
| 必須 | はい |
| デフォルト | なし |
| 例 | `/Users/yamato/Projects`, `~/workspace` |
| バリデーション | 存在確認、ディレクトリ確認、読み取り権限確認 |

### 2. プロジェクト検出パターン

| 項目 | 値 |
|-----|---|
| 型 | 選択肢または文字列 |
| 必須 | はい |
| デフォルト | 1（直下の全プロジェクト） |
| 例 | `*`, `work/*`, `proj_*/*` |
| バリデーション | Globパターンとして有効か |

### 3. アクティブプロジェクト基準日数

| 項目 | 値 |
|-----|---|
| 型 | 整数 |
| 必須 | いいえ |
| デフォルト | 7 |
| 範囲 | 1-365 |
| バリデーション | 正の整数、inactive_daysより小さい |

### 4. 休止中プロジェクト基準日数

| 項目 | 値 |
|-----|---|
| 型 | 整数 |
| 必須 | いいえ |
| デフォルト | 30 |
| 範囲 | 1-365 |
| バリデーション | 正の整数、active_daysより大きい |

### 5. 初回PROJECT_STATUS.md生成

| 項目 | 値 |
|-----|---|
| 型 | Yes/No |
| 必須 | いいえ |
| デフォルト | Y（生成する） |
| 例 | `Y`, `n`, `yes`, `no` |

---

## 出力仕様

### 1. config.yml

**場所**: `/Users/yamato/Src/proj_YPM/YPM/config.yml`

**フォーマット**: YAML

**内容**: 上記テンプレート参照

### 2. PROJECT_STATUS.md（オプション）

**場所**: `/Users/yamato/Src/proj_YPM/YPM/PROJECT_STATUS.md`

**フォーマット**: Markdown

**セクション**:
- サマリー（総プロジェクト数、アクティブ数等）
- アクティブプロジェクト
- 休止中プロジェクト
- Git非管理プロジェクト

### 3. 標準出力

**完了メッセージ**:
```
✅ セットアップが完了しました！

📁 監視対象ディレクトリ: /Users/yamato/Projects
🔍 検出パターン: *
📊 アクティブ基準: 7日以内
💤 休止中基準: 30日以上

生成されたファイル:
  - config.yml
  - PROJECT_STATUS.md

次のステップ:
  Claude Codeで「プロジェクト状況を更新して」と指示してください。
```

---

## エラーハンドリング

### 1. ディレクトリが存在しない

```
❌ エラー: ディレクトリが存在しません: /invalid/path

もう一度入力してください:
> 
```

### 2. 読み取り権限がない

```
❌ エラー: 読み取り権限がありません: /protected/directory

別のディレクトリを指定してください:
> 
```

### 3. 無効な数値入力

```
❌ エラー: 無効な数値です: abc

正の整数を入力してください [7]:
> 
```

### 4. config.ymlが既に存在

```
⚠️  警告: config.ymlが既に存在します。

上書きしますか？ [y/N]:
> 
```

**デフォルト**: N（上書きしない）

**上書きしない場合**:
```
セットアップを中止しました。
既存のconfig.ymlを使用します。
```

### 5. Gitが利用できない

```
⚠️  警告: Gitコマンドが見つかりません。

PROJECT_STATUS.mdの自動生成をスキップします。
Claude Codeで後ほど生成してください。
```

---

## 実装要件

### 技術スタック

- **言語**: Python 3.8+
- **標準ライブラリ**: `os`, `sys`, `pathlib`, `subprocess`, `yaml`, `datetime`
- **外部依存**: なし（標準ライブラリのみ）

### ファイル構成

```python
# scripts/onboarding.py

import os
import sys
from pathlib import Path
import subprocess
import yaml
from datetime import datetime

def main():
    """メインエントリーポイント"""
    print_welcome()
    
    # 既存config.ymlのチェック
    if config_exists():
        if not confirm_overwrite():
            print("セットアップを中止しました。")
            sys.exit(0)
    
    # 情報収集
    directory = ask_directory()
    pattern = ask_pattern(directory)
    active_days = ask_active_days()
    inactive_days = ask_inactive_days(active_days)
    
    # config.yml生成
    generate_config(directory, pattern, active_days, inactive_days)
    
    # PROJECT_STATUS.md生成（オプション）
    if ask_generate_status():
        generate_project_status(directory, pattern)
    
    # 完了レポート
    print_completion_report(directory, pattern, active_days, inactive_days)

def print_welcome():
    """ウェルカムメッセージ"""
    pass

def config_exists():
    """config.ymlが存在するか確認"""
    pass

def confirm_overwrite():
    """上書き確認"""
    pass

def ask_directory():
    """監視対象ディレクトリを尋ねる"""
    pass

def ask_pattern(directory):
    """プロジェクト検出パターンを尋ねる"""
    pass

def ask_active_days():
    """アクティブ基準日数を尋ねる"""
    pass

def ask_inactive_days(active_days):
    """休止中基準日数を尋ねる"""
    pass

def generate_config(directory, pattern, active_days, inactive_days):
    """config.ymlを生成"""
    pass

def ask_generate_status():
    """PROJECT_STATUS.md生成を尋ねる"""
    pass

def generate_project_status(directory, pattern):
    """PROJECT_STATUS.mdを生成"""
    pass

def print_completion_report(directory, pattern, active_days, inactive_days):
    """完了レポートを表示"""
    pass

if __name__ == "__main__":
    main()
```

### テストケース

1. **正常系**
   - 有効なディレクトリパス
   - デフォルト値での実行
   - カスタムパターンの入力

2. **異常系**
   - 存在しないディレクトリ
   - 読み取り権限がないディレクトリ
   - 無効な数値入力
   - config.yml上書き拒否

3. **エッジケース**
   - `~`を含むパス
   - 相対パス
   - 空のディレクトリ
   - Gitが利用できない環境

---

## 実装スケジュール

1. **骨格実装**（30分）
   - メイン関数
   - 入力関数の骨格

2. **バリデーション実装**（30分）
   - ディレクトリ存在確認
   - 数値検証

3. **config.yml生成**（20分）
   - YAMLテンプレート
   - ファイル書き込み

4. **PROJECT_STATUS.md生成（オプション）**（30分）
   - Git情報収集
   - Markdown生成

5. **エラーハンドリング**（20分）
   - 各種エラーケース

6. **テスト**（30分）
   - 手動テスト
   - エッジケース確認

**合計**: 約2.5時間

---

**このスクリプトにより、YPMは誰でも簡単にセットアップできるツールになります。** 🚀

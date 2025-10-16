# YPM 詳細ガイド（日本語）

> YPM (Your Project Manager) の完全な使い方ガイド

---

## 目次

- [概要](#概要)
- [特徴](#特徴)
- [前提条件](#前提条件)
- [インストール](#インストール)
- [セットアップ](#セットアップ)
- [使い方](#使い方)
- [カスタマイズ](#カスタマイズ)
- [よくある質問](#よくある質問)
- [今後の拡張予定](#今後の拡張予定)

---

## 概要

YPMは、ユーザーが指定したディレクトリ配下の複数プロジェクトの進行状況を自動的に収集・整理し、一覧表示するツールです。

**誰のためのツール？**
- 複数のプロジェクトを同時並行で進めているエンジニア・クリエイター
- 本業以外にもサイドプロジェクトを持つ人
- チームで複数プロジェクトを管理するマネージャー

### こんな課題を解決します

- ✅ プロジェクトが増えすぎて、どれが進行中かわからない
- ✅ 本業以外のプロジェクトの状況を覚えておくのが大変
- ✅ 次に何をすべきか確認するのに時間がかかる
- ✅ 進捗率や優先順位を把握しにくい

---

## 特徴

- **自動収集**: Git履歴とドキュメントから情報を自動収集
- **一元管理**: すべてのプロジェクトを1つのファイルで管理
- **Claude Code連携**: Claude Codeを使って簡単に更新
- **進捗可視化**: 各プロジェクトの進捗率を表示
- **次のタスク明示**: 各プロジェクトで次にやるべきことを表示
- **柔軟な設定**: `config.yml`で監視対象を自由にカスタマイズ

---

## 前提条件

- **Git**: プロジェクト情報の収集に使用します
- **Claude Code**: プロジェクト状況の更新に使用します（推奨）
  - [Claude Code公式サイト](https://claude.com/claude-code)
- **Python 3.8+**: オンボーディングウィザード用

---

## インストール

### 1. リポジトリをクローン

```bash
# YPMをクローン
git clone https://github.com/signalcompose/YPM.git
cd YPM
```

### 2. 依存関係のインストール

```bash
# Python依存関係をインストール
pip3 install -r requirements.txt
```

**必要な依存関係**:
- Python 3.8+
- PyYAML (config.ymlの読み書き用)

---

## セットアップ

### オンボーディングウィザードを使用（推奨）

YPMには対話型の初期設定ウィザードが用意されています。以下のコマンドを実行するだけで、簡単にセットアップできます。

```bash
# オンボーディングウィザードを実行
python3 scripts/onboarding.py
```

ウィザードが以下の情報を対話的に収集します：
1. 監視したいプロジェクトディレクトリのパス
2. プロジェクト検出パターン（自動提案）
3. アクティブ/休止中の分類基準日数

完了すると、`config.yml`が自動生成されます。

### 手動セットアップ（上級者向け）

ウィザードを使用せずに手動でセットアップする場合：

1. `config.example.yml`をコピー

```bash
cp config.example.yml config.yml
```

2. `config.yml`を編集

```yaml
monitor:
  directories:
    - /path/to/your/projects    # あなたのプロジェクトディレクトリに変更

  patterns:
    - "*"             # 直下の全プロジェクト
```

**例（macOS/Linux）**:
```yaml
directories:
  - /Users/yourname/Projects
  - /Users/yourname/Work
```

**例（Windows）**:
```yaml
directories:
  - C:/Users/yourname/Projects
```

### 初回のプロジェクト情報収集

Claude Codeを起動して、以下のように指示：

```
プロジェクト状況を更新して
```

これで `PROJECT_STATUS.md` が生成され、すべてのプロジェクト情報が収集されます。

---

## 使い方

### 1. プロジェクト状況の確認

```bash
cd ~/Src/proj_YPM/YPM
cat PROJECT_STATUS.md
```

すべてのプロジェクトの状況が一覧で確認できます。

### 2. 状況の更新

```bash
cd ~/Src/proj_YPM/YPM
# Claude Codeを起動
```

Claude Codeに以下のように指示：

```
プロジェクト状況を更新して
```

自動的に以下が実行されます：
1. `config.yml`で指定したディレクトリをスキャン
2. 各プロジェクトのGit情報を取得
3. ドキュメント（CLAUDE.md、README.md、docs/INDEX.md）を読み込み
4. `PROJECT_STATUS.md`を更新
5. 変更をコミット

### 3. 次のタスク確認

```
次にやるべきタスクは？
```

各プロジェクトの次のタスクを優先度順に表示します。

---

## ファイル構成

```
YPM/
├── .claude/
│   └── settings.json           # Claude Code権限設定
├── docs/
│   ├── INDEX.md                # ドキュメント索引
│   ├── guide-ja.md             # 日本語詳細ガイド（このファイル）
│   ├── guide-en.md             # 英語詳細ガイド
│   └── development/            # 開発者向けドキュメント
│       ├── architecture.md     # アーキテクチャ設計
│       └── onboarding-script-spec.md  # オンボーディング仕様書
├── scripts/
│   ├── onboarding.py           # 初回セットアップウィザード
│   ├── update_status.py        # プロジェクト状況更新（将来）
│   └── create_project.py       # プロジェクト作成支援（将来）
├── config.yml                  # 設定ファイル（監視対象など）※Git管理外
├── config.example.yml          # 設定テンプレート
├── requirements.txt            # Python依存関係
├── CLAUDE.md                   # Claude Code向け指示書
├── README.md                   # プロジェクト概要（英語）
├── PROJECT_STATUS.md           # プロジェクト状況一覧※Git管理外
├── LICENSE                     # MITライセンス
└── .gitignore                  # Git除外設定
```

---

## プロジェクトのカテゴリ

### 🔥 アクティブプロジェクト
最近1週間以内に更新があったプロジェクト。現在進行中。

### 🎨 設計・計画段階
Phase 0やドキュメント策定中のプロジェクト。実装前。

### 🚧 開発中
実装が進行中だが、最近の更新が1週間以上前のプロジェクト。

### 💤 休止中
1ヶ月以上更新がないプロジェクト。一時停止中。

### 📦 Git非管理
Gitリポジトリでないディレクトリ。進捗追跡対象外。

---

## 進捗率の算出基準

YPMは以下の基準でプロジェクトの進捗率を推測します：

| 進捗 | フェーズ | 状態 |
|------|---------|------|
| 0-20% | Phase 0 | 設計・計画段階 |
| 20-30% | Phase 1 | 開発環境構築 |
| 30-60% | Phase 2-3 | 基本機能実装 |
| 60-80% | Phase 4-5 | テスト・改善 |
| 80-100% | Phase 6+ | 本番稼働・機能拡張 |

**注意**: あくまで推測値です。実態と異なる場合は手動で調整してください。

---

## カスタマイズ

### 監視対象の追加

`config.yml`の`directories`に追加：

```yaml
monitor:
  directories:
    - /Users/yamato/Src
    - /Users/yamato/Work      # 追加
    - /Users/yamato/Projects  # 追加
```

### プロジェクト検出パターンの変更

異なるディレクトリ構造に対応する場合：

```yaml
monitor:
  patterns:
    - "proj_*/*"          # 2階層構造
    - "projects/*"        # 1階層構造
    - "my-apps/*/src"     # 3階層構造
```

### 分類基準の変更

アクティブ/休止の判定日数を変更：

```yaml
classification:
  active_days: 14    # 2週間以内をアクティブに変更
  inactive_days: 60  # 2ヶ月以上を休止に変更
```

---

## 更新頻度

- **推奨**: 週に1回程度
- **最低**: 月に1回

定期的に更新することで、プロジェクトの状況を常に把握できます。

---

## よくある質問

### Q: 新しいプロジェクトを追加したい

**A**: `config.yml`で指定したディレクトリ配下にプロジェクトを作成すれば、次回更新時に自動的に検出されます。

### Q: プロジェクトを除外したい

**A**: `config.yml`の`exclude`に追加してください：

```yaml
monitor:
  exclude:
    - proj_YPM/YPM
    - old_projects/*   # 除外したいパターン
```

### Q: 進捗率が不正確

**A**: `PROJECT_STATUS.md`を直接編集して調整してください。

### Q: 次のタスクが表示されない

**A**: 該当プロジェクトの`CLAUDE.md`や`docs/`に開発計画を記載してください。YPMはそれを読み取って表示します。

### Q: 別のマシンで使いたい

**A**: `config.yml`のディレクトリパスを環境に合わせて変更してください。Gitで管理しているので、簡単に同期できます。

---

## 今後の拡張予定

YPMは現在**Phase 1完成状態**です。Claude Code駆動のアプローチが実運用で有効性を発揮しています。

将来的に検討可能な拡張：

- [ ] プロジェクト作成支援ツール
- [ ] ダッシュボードUI（Webベース）
- [ ] Slack通知連携
- [ ] 優先度の自動算出
- [ ] ガントチャート生成
- [ ] プロジェクト間の依存関係可視化

**Note**: 自動更新スクリプト（cron対応）については、AIによる文脈理解と柔軟なタスク抽出の方が優れているため、現時点では優先度を下げています。

---

## トラブルシューティング

### Q: プロジェクトが検出されない

**A**: 以下を確認：
1. Gitリポジトリか？（`.git/`ディレクトリがあるか）
2. ディレクトリ構造が設定したパターンに一致するか？
3. 除外対象に含まれていないか？

### Q: Claude Codeが設定ファイルを変更しようとする

**A**: `.claude/settings.json`で読み取り専用権限を設定してください。YPM自身のファイルのみ変更可能にします。

---

## 貢献方法

YPMへの貢献を歓迎します！

### バグ報告・機能要望

- [GitHub Issues](https://github.com/signalcompose/YPM/issues)でお知らせください

### プルリクエスト

1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'feat: Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

### 開発ガイドライン

詳細は `CONTRIBUTING.md`（作成予定）を参照してください。

---

## ライセンス

このプロジェクトは [MIT License](../LICENSE) のもとで公開されています。

---

## 作成者

**Hiroshi Yamato / dropcontrol**

- Website: [hiroshiyamato.com](https://hiroshiyamato.com/) | [yamato.dev](https://yamato.dev/)
- X: [@yamato](https://x.com/yamato)
- GitHub: [dropcontrol](https://github.com/dropcontrol)

Powered by Claude Code

---

## 関連ドキュメント

- **[README.md](../README.md)** - プロジェクト概要（英語）
- **[Detailed Guide (English)](guide-en.md)** - 英語詳細ガイド
- **[CLAUDE.md](../CLAUDE.md)** - Claude Code向け指示書
- **[docs/INDEX.md](INDEX.md)** - ドキュメント索引

---

**あなたのプロジェクトを、もっと管理しやすく。** 🚀

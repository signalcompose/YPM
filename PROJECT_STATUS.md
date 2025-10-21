# プロジェクト状況一覧

**最終更新**: 2025-10-21 10:15

---

## 📊 サマリー

- **総プロジェクト数**: 24個
- **アクティブ**: 15個（1週間以内に更新）
- **開発中**: 7個（1ヶ月以内に更新）
- **休止中**: 2個（1ヶ月以上更新なし）

---

## 🔥 アクティブプロジェクト（最近1週間以内に更新）

### Slack_MCP (Slack-Claude Bridge MCP)
- **概要**: SlackとClaude Codeを接続するMCPサーバー - Slackからクエリ送信、Claude経由で回答を取得
- **現在のブランチ**: develop
- **最終更新**: 16 hours ago（docs: add vision support configuration to CLAUDE.md (#13)）
- **Phase**: v1.0.0開発完了、Phase 1移行中
- **実装進捗**: 95%（基本機能完成、Vision対応追加中）
- **次のタスク**:
  - Issue #13: Vision対応設定ドキュメント整備
  - Issue #12: リリース準備（v1.0.0）
  - Issue #11: GitHub公開準備
  - Issue #10: ブランチ保護設定
  - Issue #8: Google Drive MCP統合
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_slack_mcp/Slack_MCP/CLAUDE.md)

### CVI (Claude Voice Integration)
- **概要**: Claude Codeのタスク完了時に音声通知を行うシステム
- **現在のブランチ**: main
- **最終更新**: 15 hours ago（chore: update metadata for v2.0.0 release (#2)）
- **Phase**: Phase 1 完成、v2.0.0リリース済み
- **実装進捗**: 100%（コア機能完成、GitHub公開完了）
- **次のタスク**:
  - Issue #2: v2.0.0リリース完了
  - Issue #1: メタデータ更新
  - 多言語対応の拡張（Phase 2検討）
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_CVI/CVI/CLAUDE.md)

### MaxMCP
- **概要**: Max/MSP用ネイティブC++ MCPサーバー - 自然言語でMaxパッチを制御
- **現在のブランチ**: feature/35-maxmcp-server-implementation
- **最終更新**: 2 days ago（feat(server): implement MCP tools and Max communication (#37)）
- **Phase**: Phase 8 完了（Bootstrap完了、実装開始）
- **実装進捗**: 35%（MCPサーバー基本実装中）
- **次のタスク**:
  - Issue #37: MCPツール実装とMax通信機能
  - Issue #35: MaxMCPサーバー実装（親Issue）
  - Issue #26: テストスイート整備
  - Issue #4: リリース準備
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_max_mcp/MaxMCP/CLAUDE.md)

### MaxMCP-main（Git worktree）
- **概要**: MaxMCP mainブランチのworktree
- **現在のブランチ**: main
- **最終更新**: 2 days ago（docs: establish documentation structure (Phase 3)）
- **Phase**: Bootstrap段階
- **実装進捗**: 0%（プロジェクト構造設定中）
- **次のタスク**: develop → mainマージ時の確認用
- **ドキュメント**: [README.md](/Users/yamato/Src/proj_max_mcp/MaxMCP-main/README.md)

### MaxMSP-MCP-Server-multipatch
- **概要**: Max/MSP MCPサーバー - マルチパッチ対応バージョン（研究用）
- **現在のブランチ**: main
- **最終更新**: 2 days ago（Merge pull request #10 from dropcontrol/develop）
- **Phase**: 実験的研究
- **実装進捗**: 80%（プロトタイプ完成、MaxMCPへ移行中）
- **次のタスク**: MaxMCPプロジェクトへの知見の反映
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_max_mcp/MaxMSP-MCP-Server-multipatch/CLAUDE.md)

### picopr
- **概要**: 小規模チーム向けメールマガジン自動化システム
- **現在のブランチ**: main
- **最終更新**: 5 days ago（feat: implement Auth module with JWT authentication）
- **Phase**: Phase 1（MVP開発）
- **実装進捗**: 15%（Auth module完了）
- **テスト**: 5%（Auth moduleテスト実装）
- **次のタスク**: Newsletter Context（ドメインモデル実装）
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_picopr/picopr/CLAUDE.md)

### redmine-mcp-server
- **概要**: Redmine REST APIをMCP経由で操作可能にするサーバー
- **現在のブランチ**: develop
- **最終更新**: 3 days ago（Merge pull request #19 from signalcompose/docs/enforce-japanese-body-rule）
- **Phase**: v1.0.1リリース済み
- **実装進捗**: 100%（基本機能完成）
- **次のタスク**:
  - Issue #20: ユーザーフィードバックに基づく機能改善
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_redmine_mcp/redmine-mcp-server/CLAUDE.md)

### redmine-mcp-server-main（Git worktree）
- **概要**: redmine-mcp-server mainブランチのworktree
- **現在のブランチ**: main
- **最終更新**: 3 days ago（Release v1.0.1 (#16)）
- **Phase**: v1.0.1リリース完了
- **実装進捗**: 100%
- **次のタスク**: developの変更をマージする際の確認用
- **ドキュメント**: [README.md](/Users/yamato/Src/proj_redmine_mcp/redmine-mcp-server-main/README.md)

### InstrVo
- **概要**: 楽器演奏をリアルタイムに歌声として再生するWebアプリ
- **現在のブランチ**: feature/phase-1-mvp
- **最終更新**: 4 days ago（fix: Resolve TypeScript type checking errors）
- **Phase**: Phase 1（MVP開発、手動テストのみ）
- **実装進捗**: 70%（基本機能実装）
- **次のタスク**: TypeScriptエラー解消、MVP完成
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_InstrVo/InstrVo/CLAUDE.md)

### InstrVo-develop（Git worktree）
- **概要**: InstrVo developブランチのworktree
- **現在のブランチ**: feature/testing-setup
- **最終更新**: 4 days ago（fix: Run svelte-kit sync before ESLint in CI）
- **Phase**: Phase 1（MVP）
- **実装進捗**: 70%
- **次のタスク**: テスト環境の設定
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_InstrVo/InstrVo-develop/CLAUDE.md)

### Claude-code
- **概要**: Signal Compose社内でClaude Codeを活用するための秘伝のタレ
- **現在のブランチ**: main
- **最終更新**: 5 days ago（feat: Claude Code秘伝のタレ初版作成）
- **Phase**: 継続的更新
- **実装進捗**: ドキュメント型プロジェクト
- **次のタスク**: 新しいベストプラクティスの追加
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/Claude-code/CLAUDE.md)

### git-dotfiles-manager
- **概要**: プロジェクト固有のプライベート設定ファイルをGitとシンボリックリンクで管理
- **現在のブランチ**: develop
- **最終更新**: 6 days ago（refactor: Remove obsolete bump-version.sh script (#19)）
- **Phase**: v1.0.0開発中
- **実装進捗**: 90%（リファクタリング完了）
- **次のタスク**: v1.0.0リリース準備
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_git_dotfiles/git-dotfiles-manager/CLAUDE.md)

### TabClear
- **概要**: P2P技術とプライバシーファーストなタブグループ管理・共有システム
- **現在のブランチ**: main
- **最終更新**: 6 days ago（docs: ultra-emphasize absolute principle in README）
- **Phase**: Phase 2（3ヶ月でMVP達成目標）
- **実装進捗**: 5%（設計段階）
- **次のタスク**: 技術選定、アーキテクチャ設計
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_tabclear/TabClear/CLAUDE.md)

### oshireq
- **概要**: USEN 推し活リクエスト - 音楽リクエスト・投票サービス（本番稼働中）
- **現在のブランチ**: integration-claude-and-git-worktree
- **最終更新**: 6 days ago（レビューコメント対応: 危険なGitコマンドのブロックリスト追加）
- **Phase**: 本番稼働中（継続開発）
- **実装進捗**: 本番運用中
- **次のタスク**: Issue #702環境判定ロジック統一、#701 IPアドレス制限機能（GitHubより）
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_usen/oshireq/CLAUDE.md)

### YPM-main（Git worktree）
- **概要**: YPM mainブランチのworktree
- **現在のブランチ**: main
- **最終更新**: 6 days ago（Merge pull request #6 from signalcompose/develop）
- **Phase**: 継続的開発
- **実装進捗**: 100%（基本機能完成）
- **次のタスク**: developからのマージ確認用
- **ドキュメント**: [README.md](/Users/yamato/Src/proj_YPM/YPM-main/README.md)

---

## 🚧 開発中（最近1ヶ月以内に更新）

### DUNGIA
- **概要**: エクストリームダンジョニング - ダンジョンタイムアタックゲーム
- **現在のブランチ**: develop
- **最終更新**: 1 week ago（docs: Enforce standard Git Flow and add global policies (#9)）
- **Phase**: Phase 0（設計・計画段階）
- **実装進捗**: 0%（設計中、Backend TBD: Go/Rust + PostgreSQL/NoSQL）
- **次のタスク**: 技術スタック決定、プロトタイプ開発
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_game_jam/DUNGIA/CLAUDE.md)

### GLOBAL_PDCA_IMPLEMENTATION_v1.3-Final
- **概要**: 人間時間で考える投資PDCAシステムの安全モードテンプレート
- **現在のブランチ**: main
- **最終更新**: 1 week ago（Initial commit）
- **Phase**: テンプレート
- **実装進捗**: 100%（テンプレート完成）
- **次のタスク**: 実装プロジェクトでの活用
- **ドキュメント**: [README.md](/Users/yamato/Src/proj_my_first_turnip/GLOBAL_PDCA_IMPLEMENTATION_v1.3-Final/README.md)

### my_first_turnip
- **概要**: 実験的自動取引PDCAシステム（BTC/ETH）
- **現在のブランチ**: develop
- **最終更新**: 1 week ago（Merge pull request #5 from dropcontrol/feature/4-add-initial-pdca-system）
- **Phase**: Phase 1（実験段階）
- **実装進捗**: 30%（基本PDCA実装）
- **次のタスク**: バックテスト環境構築
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_my_first_turnip/my_first_turnip/CLAUDE.md)

### my_first_turnip-main（Git worktree）
- **概要**: my_first_turnip mainブランチのworktree
- **現在のブランチ**: main
- **最終更新**: 1 week ago（chore: add specs submodule (dropcontrol/GLOBAL_PDCA_IMPLEMENTATION)）
- **Phase**: Phase 1
- **実装進捗**: 30%
- **次のタスク**: developからのマージ確認用
- **ドキュメント**: [README.md](/Users/yamato/Src/proj_my_first_turnip/my_first_turnip-main/README.md)

### orbitscore
- **概要**: オーディオベースのライブコーディングDSL（音楽制作用）
- **現在のブランチ**: 61-audio-playback-testing
- **最終更新**: 1 week ago（docs: CLAUDE.md簡潔化とプロジェクト計画ドキュメント追加）
- **Phase**: オーディオ実装へ移行中（MIDI実装廃止）
- **実装進捗**: 20%（オーディオ再生実装中）
- **次のタスク**: オーディオ再生テスト、タイムストレッチ実装
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_livecoding/orbitscore/CLAUDE.md)

### orbitscore-main（Git worktree）
- **概要**: orbitscore mainブランチのworktree（MIDI実装保存用）
- **現在のブランチ**: main
- **最終更新**: 2 weeks ago（docs: clarify agent initialization and tool confirmation policy）
- **Phase**: 旧MIDI実装（研究参考用）
- **実装進捗**: 100%（廃止、参考実装として保存）
- **次のタスク**: オーディオ実装の参考資料として活用
- **ドキュメント**: [CLAUDE.md](/Users/yamato/Src/proj_livecoding/orbitscore-main/CLAUDE.md)

### almf.github.io
- **概要**: ALMF公式サイト（Jekyll）
- **現在のブランチ**: main
- **最終更新**: 4 weeks ago（Update site opened post to clarify ALMF's official site announcement）
- **Phase**: 運用中
- **実装進捗**: 100%（サイト公開済み）
- **次のタスク**: コンテンツ更新
- **ドキュメント**: [README.md](/Users/yamato/Src/proj_almf/almf.github.io/README.md)

---

## 💤 休止中（1ヶ月以上更新なし）

### godot-mcp
- **概要**: Godot Engine向けMCPサーバー
- **現在のブランチ**: main
- **最終更新**: 7 months ago
- **Phase**: 休止中
- **実装進捗**: 不明
- **次のタスク**: 未定
- **ドキュメント**: [README.md](/Users/yamato/Src/MCPServer/godot-mcp/README.md)

### loto7loto6Generator
- **概要**: ロト7・ロト6番号生成ツール
- **現在のブランチ**: master
- **最終更新**: 6 years ago
- **Phase**: 休止中（レガシー）
- **実装進捗**: 100%（完成済み）
- **次のタスク**: なし
- **ドキュメント**: [README.md](/Users/yamato/Src/proj_loto/loto7loto6Generator/README.md)

---

## 📦 Git非管理

（なし）

---

## 次回確認事項

**注意**: 以下は観測された状況からの確認事項です。実際の計画は各プロジェクトで決定されます。

- **Slack_MCP**: v1.0.0リリース準備、GitHub公開準備の進捗
- **CVI**: v2.0.0リリース完了、Phase 2多言語対応の計画
- **MaxMCP**: MCPサーバー実装進捗（feature/35）
- **picopr**: Newsletter Contextドメインモデル実装
- **InstrVo**: MVP完成状況
- **orbitscore**: オーディオ再生実装進捗
- **DUNGIA**: 技術スタック決定
- **TabClear**: アーキテクチャ設計

**重要**: 「次のタスク」は以下の情報源から取得しています：
- GitHubのIssue（最優先）
- 最新のコミットメッセージ
- プロジェクトのCLAUDE.mdやREADME.md
- 不明な場合は「不明」と記載

---

**管理者メモ**:
- Git worktree（MaxMCP-main、redmine-mcp-server-main、InstrVo-develop、my_first_turnip-main、orbitscore-main、YPM-main）は各プロジェクトの別ブランチ管理用
- 検出されたworktree: 5個（`.git`ファイルで判定）
- CVIがv2.0.0リリース完了（10/21）
- MaxMCPが実装フェーズ35%到達
- picoprがAuth module実装完了、DDD原則でドメインモデル開発中
- Slack_MCPがv1.0.0リリース準備段階、Vision対応追加中

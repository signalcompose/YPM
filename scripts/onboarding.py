#!/usr/bin/env python3
"""
YPM オンボーディングスクリプト

新規ユーザーがYPMを初めて使用する際に、対話的に必要な情報を収集し、
config.ymlを自動生成するウィザードスクリプト。

仕様書: docs/development/onboarding-script-spec.md
"""

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
            print("\n❌ セットアップを中止しました。")
            print("既存のconfig.ymlを使用します。")
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
    print("\n" + "=" * 70)
    print("🚀 YPM (Your Project Manager) - 初期設定ウィザード")
    print("=" * 70)
    print("\nこのウィザードで、YPMがプロジェクトを監視するための設定を行います。")
    print("いくつかの質問に答えていただくだけで、config.ymlが自動生成されます。\n")

def config_exists():
    """config.ymlが存在するか確認"""
    config_path = Path("config.yml")
    return config_path.exists()

def confirm_overwrite():
    """上書き確認"""
    print("\n⚠️  警告: config.ymlが既に存在します。")
    response = input("\n上書きしますか？ [y/N]: ").strip().lower()
    return response in ['y', 'yes']

def ask_directory():
    """監視対象ディレクトリを尋ねる"""
    print("\n" + "-" * 70)
    print("📁 STEP 1: 監視対象ディレクトリの設定")
    print("-" * 70)
    print("\nYPMが監視するプロジェクトディレクトリのパスを入力してください。")
    print("例: /Users/yourname/Projects, ~/workspace\n")
    
    while True:
        path_input = input("監視対象ディレクトリ: ").strip()
        
        if not path_input:
            print("❌ エラー: パスを入力してください。")
            continue
        
        # ~ を展開
        path_expanded = Path(path_input).expanduser()
        
        # 存在確認
        if not path_expanded.exists():
            print(f"❌ エラー: ディレクトリが存在しません: {path_expanded}")
            print("\nもう一度入力してください。")
            continue
        
        # ディレクトリ確認
        if not path_expanded.is_dir():
            print(f"❌ エラー: パスがディレクトリではありません: {path_expanded}")
            print("\nもう一度入力してください。")
            continue
        
        # 読み取り権限確認
        if not os.access(path_expanded, os.R_OK):
            print(f"❌ エラー: 読み取り権限がありません: {path_expanded}")
            print("\n別のディレクトリを指定してください。")
            continue
        
        print(f"\n✅ ディレクトリを確認しました: {path_expanded}")
        return str(path_expanded)

def ask_pattern(directory):
    """プロジェクト検出パターンを尋ねる"""
    print("\n" + "-" * 70)
    print("🔍 STEP 2: プロジェクト検出パターンの設定")
    print("-" * 70)
    print("\nディレクトリ構造を分析しています...\n")
    
    # ディレクトリ構造を表示
    try:
        subdirs = [d.name for d in Path(directory).iterdir() if d.is_dir() and not d.name.startswith('.')]
        subdirs = sorted(subdirs[:10])  # 最初の10個まで
        
        print(f"ディレクトリ構造: {directory}/")
        for subdir in subdirs:
            print(f"  ├── {subdir}/")
            # 2階層目も確認
            subdir_path = Path(directory) / subdir
            try:
                sub_subdirs = [d.name for d in subdir_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
                for sub in sub_subdirs[:3]:
                    print(f"  │   ├── {sub}/")
            except:
                pass
        
        if len(subdirs) > 10:
            print(f"  ... (他 {len(list(Path(directory).iterdir())) - 10}個)")
    except Exception as e:
        print(f"ディレクトリのスキャンに失敗しました: {e}")
    
    print("\n推奨プロジェクト検出パターン:")
    print("  1. * (直下の全プロジェクト)")
    print("  2. work/* (特定のディレクトリ配下)")
    print("  3. proj_*/* (特定の命名規則、2階層)")
    print("  4. カスタムパターンを入力")
    
    while True:
        choice = input("\n選択してください [1]: ").strip()
        
        if not choice:
            choice = "1"
        
        if choice == "1":
            return "*"
        elif choice == "2":
            subdir = input("ディレクトリ名を入力してください (例: work): ").strip()
            if subdir:
                return f"{subdir}/*"
            else:
                print("❌ エラー: ディレクトリ名を入力してください。")
        elif choice == "3":
            prefix = input("プレフィックスを入力してください (例: proj_): ").strip()
            if prefix:
                return f"{prefix}*/*"
            else:
                print("❌ エラー: プレフィックスを入力してください。")
        elif choice == "4":
            pattern = input("カスタムパターンを入力してください: ").strip()
            if pattern:
                return pattern
            else:
                print("❌ エラー: パターンを入力してください。")
        else:
            print("❌ エラー: 1-4の番号を選択してください。")

def ask_active_days():
    """アクティブ基準日数を尋ねる"""
    print("\n" + "-" * 70)
    print("📅 STEP 3: 分類基準の設定")
    print("-" * 70)
    print("\n何日以内に更新されたプロジェクトを「アクティブ」とするか設定します。")
    
    while True:
        response = input("\nアクティブプロジェクトの基準日数 [7]: ").strip()
        
        if not response:
            return 7
        
        try:
            days = int(response)
            if days <= 0:
                print("❌ エラー: 正の整数を入力してください。")
                continue
            if days > 365:
                print("❌ エラー: 365日以下の値を入力してください。")
                continue
            return days
        except ValueError:
            print(f"❌ エラー: 無効な数値です: {response}")
            print("正の整数を入力してください。")

def ask_inactive_days(active_days):
    """休止中基準日数を尋ねる"""
    print("\n何日以上更新されていないプロジェクトを「休止中」とするか設定します。")
    
    while True:
        response = input(f"\n休止中プロジェクトの基準日数 [30]: ").strip()
        
        if not response:
            days = 30
        else:
            try:
                days = int(response)
            except ValueError:
                print(f"❌ エラー: 無効な数値です: {response}")
                print("正の整数を入力してください。")
                continue
        
        if days <= 0:
            print("❌ エラー: 正の整数を入力してください。")
            continue
        if days > 365:
            print("❌ エラー: 365日以下の値を入力してください。")
            continue
        if days <= active_days:
            print(f"❌ エラー: アクティブ基準日数（{active_days}日）より大きい値を入力してください。")
            continue
        
        return days

def generate_config(directory, pattern, active_days, inactive_days):
    """config.ymlを生成"""
    print("\n" + "-" * 70)
    print("⚙️  config.ymlを生成しています...")
    print("-" * 70)
    
    config_data = {
        '# YPM設定ファイル': None,
        '# 自動生成日時': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'monitor': {
            'directories': [directory],
            'exclude': ['proj_YPM/YPM'],
            'patterns': [pattern]
        },
        'classification': {
            'active_days': active_days,
            'inactive_days': inactive_days
        },
        'progress': {
            'phase_0': '0-20',
            'phase_1': '20-30',
            'phase_2': '30-60',
            'phase_3': '60-80',
            'phase_4': '80-100'
        },
        'settings': {
            'include_non_git': False,
            'doc_priority': ['CLAUDE.md', 'README.md', 'docs/INDEX.md']
        }
    }
    
    # コメント付きYAMLを生成
    with open('config.yml', 'w', encoding='utf-8') as f:
        f.write(f"# YPM設定ファイル\n")
        f.write(f"# 自動生成日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        yaml.dump({
            'monitor': config_data['monitor'],
            'classification': config_data['classification'],
            'progress': config_data['progress'],
            'settings': config_data['settings']
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    print("✅ config.ymlを生成しました。")

def ask_generate_status():
    """PROJECT_STATUS.md生成を尋ねる"""
    print("\n" + "-" * 70)
    print("📊 STEP 4: 初回PROJECT_STATUS.mdの生成（オプション）")
    print("-" * 70)
    print("\n初回のPROJECT_STATUS.mdを今すぐ生成することもできます。")
    print("（Claude Codeで後ほど生成することも可能です）")
    
    # Gitが利用可能か確認
    try:
        subprocess.run(['git', '--version'], capture_output=True, check=True)
    except:
        print("\n⚠️  警告: Gitコマンドが見つかりません。")
        print("PROJECT_STATUS.mdの自動生成をスキップします。")
        print("Claude Codeで後ほど生成してください。")
        return False
    
    response = input("\n初回のPROJECT_STATUS.mdを生成しますか？ [Y/n]: ").strip().lower()
    return response != 'n'

def generate_project_status(directory, pattern):
    """PROJECT_STATUS.mdを生成"""
    print("\n" + "-" * 70)
    print("📊 PROJECT_STATUS.mdを生成しています...")
    print("-" * 70)
    print("\nこの処理には時間がかかる場合があります...\n")
    
    # 簡易版のPROJECT_STATUS.mdを生成
    # （完全版はClaude Codeに任せる）
    with open('PROJECT_STATUS.md', 'w', encoding='utf-8') as f:
        f.write("# プロジェクト状況一覧\n\n")
        f.write(f"**最終更新**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write("---\n\n")
        f.write("## 📊 サマリー\n\n")
        f.write("初回生成完了。Claude Codeで「プロジェクト状況を更新して」と指示してください。\n\n")
    
    print("✅ PROJECT_STATUS.md（初期版）を生成しました。")
    print("   詳細な情報はClaude Codeで更新してください。")

def print_completion_report(directory, pattern, active_days, inactive_days):
    """完了レポートを表示"""
    print("\n" + "=" * 70)
    print("✅ セットアップが完了しました！")
    print("=" * 70)
    print("\n📁 監視対象ディレクトリ:", directory)
    print("🔍 検出パターン:", pattern)
    print("📊 アクティブ基準:", f"{active_days}日以内")
    print("💤 休止中基準:", f"{inactive_days}日以上")
    print("\n生成されたファイル:")
    print("  - config.yml")
    if Path("PROJECT_STATUS.md").exists():
        print("  - PROJECT_STATUS.md（初期版）")
    print("\n" + "-" * 70)
    print("🎉 次のステップ:")
    print("-" * 70)
    print("\nClaude Codeで以下のように指示してください：")
    print('  「プロジェクト状況を更新して」')
    print("\nこれで、すべてのプロジェクト情報が収集されます。\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ セットアップが中断されました。")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

# 演習3：KINTONEのログイン突破

## 課題内容
**ID**、**PASSWORD**を環境変数（.env）ファイルに格納・取得。
KINTONEにWEBスクレイピングでログインし**ポータル**画面を表示させる。

## テーマ
- 環境変数
  - 「.envファイル」作成
  - ID・PASSWORDを格納
  - ID・PASSWORDを取得
- WEBスクレイピング
  - URLへアクセス
  - XPATHの取得
  - ログイン情報入力
  - ボタンクリック


## 作成手順・ヒント
- python-dotenv
  - 「.env」ファイル読み込むためのライブラリ
  - 「pip install python-dotenv」にてライブラリインストール
  - 使用方法：https://qiita.com/harukikaneko/items/b004048f8d1eca44cba9
- selenium
  - WEB自動化ライブラリ（別途Chromeドライバーなど必要）
  - 「pip install selenium」にてライブラリインストール
  - Chromeドライバー
    - ダウンロードサイト：https://chromedriver.chromium.org/downloads
    - ダウンロード、解凍し任意の場所に配置



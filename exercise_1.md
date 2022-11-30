# 演習1：ライブラリ一覧の読み込み&Excelへ書き出し

# 課題内容
「requirements.txt」というライブラリの一覧ファイルを読み込みライブラリ名とバージョンが記載されているので、Excelへ転記する。

## サンプル
### ライブラリ一覧サンプル（インプット）
@import "./requirements.txt" {line_begin=0 line_end=5}

### Excelへ出力した際のサンプル（アウトプット）
@import "./img/exercise_1/output_sample.png"

## 作成手順・ヒント
- テキストファイルの読み込み
  - ライブラリ名とバージョンに分割（split関数）
  - バージョンの後ろに改行コード「\n」が挿入されているので、置換（削除）が必要（replace関数）
- 読み込んだテキストファイルを辞書形式へ成形
- Pandas(※1)を利用し、Excelへ書き出し
  - 辞書形式に格納したものをデータフレーム(※2)へ格納
  - 注意：Excelへ出力時にPnadasのライブラリ内部で「openpyxl(※1)」というライブラリを使用しているため、事前にインストールが必要

※1：Pandasは3rd partyライブラリ
※2：データフレームとは、Pandasで扱う2次元配列のこと（Pandasで扱う1次元配列は「Series」という）
※3：openpyxlは3rd partyライブラリ

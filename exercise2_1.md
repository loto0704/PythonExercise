# 演習2：requestsモジュールを利用した、APIへアクセス

## 課題内容
requestsモジュールを利用し、「Google Books※1」が用意しているのAPI（Google Books API※2）アクセスし書籍情報を取得。
書籍情報の取得方法は、ISBNで検索する。


## テーマ
- ISBN番号取得
  - APIで使用可能なのは「10桁文字列」or「13桁整数」
- APIアクセス用にURLを生成
- APIへアクセスし、ステータスコードが200以外の場合は終了
- APIへアクセスし返ってきたJsonデータを解析
- 定数


## 出力項目（詳細はサンプルを参照）
> 1行目：検索したURL
> 2行目：書籍タイトル
> n+2行目：著者
> n+3行目：ISBN-10
> n+4行目：ISBN-13


## サンプル
### ISBN-10
#### インプット
> 429711111X

#### アウトプット
> URL：https://www.googleapis.com/books/v1/volumes?q=isbn:9784297111113
> タイトル：Python実践入門
> 著者1人目：陶山嶺
> 429711111X
> 9784297111113

### ISBN-13
#### インプット
> 9784297111113
#### アウトプット
> URL：https://www.googleapis.com/books/v1/volumes?q=isbn:9784297111113
> タイトル：Python実践入門
> 著者1人目：陶山嶺
> 429711111X
> 9784297111113


## 作成手順・ヒント
- 事前準備
  - APIアクセスするため「requests」モジュールをインストール
     - ```pip install requests```
- アクセスするURLを生成
  - ベースURL「https://www.googleapis.com/books/v1/volumes」
- 生成したURLにアクセス
  - 問題なければ、書籍情報が返ってくる
- 書籍情報を解析・出力
  - タイトル
  - 著者
  - ISBN-10
  - ISBN-13


※1：Google Books（https://books.google.co.jp/）
※2：GoogleBooksAPI（https://www.googleapis.com/books/v1/volumes）
※3:GoogleBooksAPIドキュメント（https://developers.google.com/books）

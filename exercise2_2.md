# 演習2-2：演習2-1をベースにCSVファイルのデータをまとめて検索

## 課題内容
### 演習1
requestsモジュールを利用し、「Google Books※1」が用意しているのAPI（Google Books API※2）アクセスし書籍情報を取得。
書籍情報の取得方法は、ISBNで検索する。

### 演習2
演習1をベースに「exercise2_sample_data.csv」（サンプルデータ）をまとめて検索を行う。

## テーマ
- ISBNをCSVより1つずつ取り出す(解答ではPandasモジュールを使用しているが、CSVモジュールでも可)
- ISBNを演習1同様にAPIを使用し書籍を検索する

## サンプル
### CSVファイルインポート（まとめて検索）
#### インプット
> ./exercise_2_sample_data.csv

#### アウトプット
>【1冊目】
https://www.googleapis.com/books/v1/volumes?q=isbn:9784822292270
タイトル：独学プログラマー
著者1人目：コーリー・アルソフ
4822292274
9784822292270

>【2冊目】
https://www.googleapis.com/books/v1/volumes?q=isbn:9784297111113
タイトル：Python実践入門
著者1人目：陶山嶺
429711111X
9784297111113



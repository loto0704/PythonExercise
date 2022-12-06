import json
import sys

import requests


BASE_URL = "https://www.googleapis.com/books/v1/volumes"


def create_url(search_isbn):
    request_url = f"{BASE_URL}?q=isbn:{search_isbn}"
    print(f"URL：{request_url}")
    return request_url


def api_request(search_url: str) -> str:
    """APIへアクセスし、成功した場合は結果を返す"""
    res = requests.get(search_url)
    if res.status_code == 200:
        return res.text
    else:
        print(f"エラーコード：{res.status_code}")
        print("終了します")
        sys.exit()


def json_process(request_data: str) -> None:
    json_data = json.loads(request_data)  # 文字列を辞書型へ変換
    title = json_data["items"][0]["volumeInfo"]["title"]
    authors = json_data["items"][0]["volumeInfo"]["authors"]
    print(f"タイトル：{title}")
    for i in range(len(authors)):
        print(f"著者{i + 1}人目：{authors[i]}")

    industry_identifiers = json_data["items"][0]["volumeInfo"]["industryIdentifiers"]
    for i in range(len(industry_identifiers)):
        if industry_identifiers[i]["type"] == "ISBN_10":
            isbn_10 = industry_identifiers[i]["identifier"]
            print(isbn_10)
        elif industry_identifiers[i]["type"] == "ISBN_13":
            isbn_13 = industry_identifiers[i]["identifier"]
            print(isbn_13)


def main() -> None:
    isbn = sys.argv[1]  # ISBN-10 or ISBN-13(「-」なし)を読み込み
    request_url = create_url(isbn)
    request_data = api_request(request_url)
    json_process(request_data)


if __name__ == '__main__':
    main()

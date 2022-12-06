import sys
import pandas
import time
from exercise2_1 import create_url, api_request, json_process


def main():
    csv_path = sys.argv[1]
    pd_data = pandas.read_csv(csv_path, encoding='utf-8')

    for i in range(len(pd_data)):
        print(f"【{i+1}冊目】")
        isbn_13 = pd_data["ISBN-13"][i]
        request_url = create_url(isbn_13)
        request_data = api_request(request_url)
        json_process(request_data)
        time.sleep(2)


if __name__ == '__main__':
    main()

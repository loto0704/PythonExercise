from datetime import date
import os
import sys
import pandas


def txt_read() -> dict:
    """テキストファイル「requirements.txt」を読み込み→辞書に格納"""
    requirements_path = sys.argv[1]
    data_dict = {}
    with open(requirements_path, mode='r', encoding='utf-8') as f:
        library_list = f.readlines()
        for i in range(len(library_list)):
            data_dict[i] = {
                "Library_name": library_list[i].split("==")[0],
                "Version": library_list[i].split("==")[1].replace("\n", "")  # 改行コードが含まれているので、置換で削除
            }
    return data_dict


def main():
    library_dict = txt_read()

    # Exportする際のファイル名やフォルダのを決める
    export_file_name = f"libraryList_{date.today()}.xlsx"
    export_folder_path = os.path.expanduser("~/Downloads")
    export_full_path = f"{export_folder_path}/{export_file_name}"

    # 事前に「pip install pandas openpyxl」を実行
    pd_data = pandas.DataFrame.from_dict(library_dict).T  # 辞書→Pandasを利用してデータフレームへ変換（行列が反対なのでピポット）
    pd_data.to_excel(export_full_path, index=False, header=True)


if __name__ == '__main__':
    main()

import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


BASE_URL = "cybozu.com"
# .envファイルの内容を読み込む
load_dotenv()


def env_get() -> dict:
    email = os.environ["LOGIN-EMAIL"]
    pass_wd = os.environ["LOGIN-PASSWORD"]
    sub_domain = os.environ["SUB-DOMAIN"]

    return {"email": email, "pass_wd": pass_wd, "sub_domain": sub_domain}


def scraping():
    """Chrome driverを直接指定"""
    driver_path="./chromedriver.exe"
    # chrome_service = service.Service(executable_path=driver_path)
    # driver = webdriver.Chrome(service=chrome_service)

    """Chrome driverを自動更新"""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    env = env_get()  # 環境変数読み込み
    home_url = f"https:{env['sub_domain']}.{BASE_URL}"

    driver.get(home_url)
    time.sleep(2)

    login_id_xpath = "/html/body/div[4]/div/div[2]/form/div[2]/div[3]/input"
    login_pw_xpath = "/html/body/div[4]/div/div[2]/form/div[2]/div[4]/input"
    login_button_xpath = "/html/body/div[4]/div/div[2]/form/div[4]/div[2]/input"
    driver.find_element(by=By.XPATH, value=login_id_xpath).send_keys(env['email'])
    driver.find_element(by=By.XPATH, value=login_pw_xpath).send_keys(env['pass_wd'])
    driver.find_element(by=By.XPATH, value=login_button_xpath).click()
    time.sleep(2)

    # ポータルへアクセス
    driver.get(f"{home_url}/k/#/portal")
    time.sleep(100)  # 一時停止目的


def main():
    scraping()


if __name__ == '__main__':
    main()

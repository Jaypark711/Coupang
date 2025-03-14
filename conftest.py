# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    # 크롬 옵션 설정
    chrome_options = Options() #쿠팡이 자동화 크롤링 많은 옵션수정이 필요하다.. 
    # 1) User-Agent 변경
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/91.0")
    # 2) SSL 인증서 에러 무시
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")

    # 4) Selenium이 automation된 브라우저임을 숨기는 몇 가지 설정
    #    - (disable-blink-features=AutomationControlled) 제거
    #    - excludeSwitches, useAutomationExtension
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # 혹은 다음 방식으로 Blink 특징을 비활성화할 수도 있으나
    # "AutomationControlled" 자체가 표기되지 않도록 한다.
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # 6) Sandbox나 DevShm 사이즈 문제 우회 (리눅스 환경에서 발생 가능)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")    
   
   
    # 드라이버 객체 생성
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"Referer": "https://www.coupang.com/"}})

    #  대기시간 설정
    driver.implicitly_wait(5)

    yield driver 

    # 테스트가 끝나면 드라이버 종료
    driver.quit()


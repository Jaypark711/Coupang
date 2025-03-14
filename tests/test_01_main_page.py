# tests/test_main_page.py
import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver # noqa
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from tests.pages.main_page import MainPage
from selenium.webdriver.common.by import By

from urllib import parse
#단위테스트 - 쿠팡 테스트 케이스는 접근도 못함.
class TestMainPage:
    @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_open_main_page(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()

            time.sleep(2)

            wait = ws(driver, 10) #최대 10초까지 기다림
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증 

        except NoSuchElementException as e:
            assert False

    #@pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_click_link_text(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()

            time.sleep(2)

            wait = ws(driver, 10) #최대 10초까지 기다림
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증 

            main_page.click_by_LINK_TEXT('로그인')

            assert "login" in driver.current_url
            driver.save_screenshot('메인페이지-로그인-성공.jpg')

            time.sleep(2)
            driver.back()
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증 

            time.sleep(2)
            main_page.click_by_LINK_TEXT('회원가입')
            assert "memberJoinFrm" in driver.current_url
            driver.save_screenshot('메인페이지-회원가입-성공.jpg')

            time.sleep(2)
            driver.back()
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증 

            #비로그인 테스트이므로 마이쿠팡을 클릭시 로그인가야함함
            time.sleep(2)
            main_page.click_by_LINK_TEXT('마이쿠팡')
            assert "login" in driver.current_url
            driver.save_screenshot('메인페이지-장바구니-성공.jpg')

        except NoSuchElementException as e:
            driver.save_screenshot('메인페이지-링크텍스트-실패-노서치.jpg')
            assert False

        except TimeoutException as e:
            driver.save_screenshot('메인페이지-링크텍스트-실패-타임에러.jpg')
            assert False

    @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_search_items(self, driver: WebDriver):
        try:    
            ITEMS_XPATH = "//form//ul/li"
            main_page = MainPage(driver)
            main_page.open()

            time.sleep(2)

            wait = ws(driver, 10) #최대 10초까지 기다림
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증 
        
            time.sleep(2) #2초 왜? 봇인거 안들키기 위해서 
        
            main_page.search_items('노트북')

            ws(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ITEMS_XPATH))
            )

            items = driver.find_elements(By.XPATH, ITEMS_XPATH)
            item_name = parse.quote('노트북')

            assert len(items) > 0
            assert item_name in driver.current_url
            
            driver.save_screenshot('메인페이지-검색-성공.jpg')
        except NoSuchElementException as e:
            driver.save_screenshot('메인페이지-검색-실패-노서치.jpg')
            assert False

        except TimeoutException as e:
            driver.save_screenshot('메인페이지-검색-실패-타임에러.jpg')
            assert False

    

            

        






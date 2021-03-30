from selenium import webdriver
import pytest
import time

driver = webdriver.Chrome()
driver.get("https://erzaf.com")

def test_open_erzafcom():
    driver.implicitly_wait(5)
    heading = driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/nav/div/div[1]/a/span')
    assert heading.text == "Erzaf"


def test_open_article():
    driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/nav/div/div[2]/a[1]').click()
    driver.implicitly_wait(5)
    article_header = driver.find_element_by_xpath('//*[@id="main-content"]/div/h1')
    assert article_header.text == "Articles"
    
def test_search_article():
    driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/input').send_keys('OSINT')
    driver.implicitly_wait(5)
    results = driver.find_elements_by_xpath('//*[@id="main-content"]/div/section/a[1]/div/div[2]/h2')
    assert len(results) > 0
    assert "OSINT" in results[0].text

def test_click_detail_article():
    link = driver.find_elements_by_xpath('//*[@id="main-content"]/div/section/a')
    link[0].click()
    driver.implicitly_wait(5)
    title = driver.find_element_by_xpath('//*[@id="main-content"]/article/header/div[2]/h1')
    assert "OSINT" in title.text
    time.sleep(2)
    driver.close()

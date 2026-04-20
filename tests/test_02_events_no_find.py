from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

if __name__ == "__main__":

    oprions = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=oprions)
    driver.implicitly_wait(10)

    driver.maximize_window()
    driver.get(BASE_URL)
    
    search_img_selector = "//span[@class='search-img']"
    search_img = driver.find_element(By.XPATH, search_img_selector)
    search_img.click()

    search_place = "//input[@placeholder='Search']"
    search_input = driver.find_element(By.XPATH, search_place)
    search_input.send_keys("456")
    search_input.send_keys(Keys.RETURN)
    wait = WebDriverWait(driver, 10)

    events_find_xpath = "//p[contains(text(), 'Знайдено 0 подій')]"
    wait.until(lambda d: d.find_element(By.XPATH, events_find_xpath).is_displayed())
    events_find = driver.find_element(By.XPATH, events_find_xpath)
    assert events_find.is_displayed(), "Знайдено 0 подій"
    print(events_find.text)

    cansel_search_path = "//img[@alt='cancel search']"
    cansel_search = driver.find_element(By.XPATH, cansel_search_path)
    cansel_search.click()

    events_find_xpath = "//p[contains(text(), 'Знайдено 47 подій')]"
    wait.until(lambda d: d.find_element(By.XPATH, events_find_xpath).is_displayed())
    events_find = driver.find_element(By.XPATH, events_find_xpath)
    assert events_find.is_displayed(), "Знайдено 47 подій"

    print(events_find.text)
    driver.quit()
    
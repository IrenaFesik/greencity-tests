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
    
    language_switcher_xpath = "//ul[@aria-label='language switcher']"
    language_switcher = driver.find_element(By.XPATH, language_switcher_xpath)
    language_switcher.click()
    language_en_selector = ".//span[contains(text(), 'En')]"
    language_en_option = language_switcher.find_element(By.XPATH, language_en_selector)
    language_en_option.click()

    button_create_selector = "//button[@class='secondary-global-button m-btn' and contains(text(), 'Create event')]"
    button_create_event = driver.find_element(By.XPATH, button_create_selector)
    button_create_event.click()

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    sign_in_button_xpath = "//button[@class='greenStyle']"
    sign_in_button = driver.find_element(By.XPATH, sign_in_button_xpath)
    assert sign_in_button.is_displayed(), "Sign in button is not displayed"
    email_input.send_keys("test@gmail.com")
    password_input.send_keys("12345678")
    sign_in_button.click()
    wait = WebDriverWait(driver, 10)
    error_message_xpath = "//div[@class='alert-general-error']"
    wait.until(lambda d: d.find_element(By.XPATH, error_message_xpath).is_displayed())
    error_message = driver.find_element(By.XPATH, error_message_xpath)
    assert error_message.is_displayed(), "Bad password"
    wait = WebDriverWait(driver, 10)
    driver.quit()

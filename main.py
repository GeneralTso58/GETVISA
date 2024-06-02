from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import Credentials
import EmailNotificationService
from random import randrange
import time

REFRESH_INTERVAL_RANGE_START_SECOND = 220
REFRESH_INTERVAL_RANGE_END_SECOND = 350

# TEST_REFRESH_INTERVAL_RANGE_START_SECOND = 5
# TEST_REFRESH_INTERVAL_RANGE_END_SECOND = 10

def isInDesiredMonthYear(availableDate: str) -> bool:
    desiredMonthYear = ['June, 2024', 'July, 2024', 'August, 2024', 'September, 2024', 'October, 2024']
    return sum([desired in availableDate for desired in desiredMonthYear]) > 0

def doLogIn(driver):
    emailInput = driver.find_element(by=By.ID, value="user_email")
    passwordInput = driver.find_element(by=By.ID, value="user_password")
    confirmPolicyButton = driver.find_element(by=By.XPATH, value='//*[@id="sign_in_form"]/div[3]/label')
    loginButton = driver.find_element(by=By.NAME, value="commit")

    emailInput.send_keys(Credentials.CONSULATE_LOGIN_USERNAME)
    passwordInput.send_keys(Credentials.CONSULATE_LOGIN_PASSWORD)
    confirmPolicyButton.click()
    loginButton.click()

def checkIsLoginPage(driver) -> bool:
    try:
        driver.find_element(by=By.ID, value="user_email")
        return True
    except:
        return False

def clickPayVisaFee(driver):
    payVisaFeeLink = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/div[2]/div/section/ul/li[1]/div/div/div[2]/p[2]/a')
    url = payVisaFeeLink.get_attribute('href')
    driver.get(url)

def checkEarliestVancAvailability(driver) -> bool:
    earliestVancouverSlot = driver.find_element(by=By.XPATH, value='//*[@id="paymentOptions"]/div[2]/table/tbody/tr[4]/td[2]').text
    return isInDesiredMonthYear(earliestVancouverSlot)

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://ais.usvisa-info.com/en-ca/niv/users/sign_in")

doLogIn(driver)

# only land on this page for the first time
continueButton = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/ul/li/a')
continueButton.click()

try:
    while True:
        clickPayVisaFee(driver)
        sentBackToLoginPage = False
        while not sentBackToLoginPage:
            if checkEarliestVancAvailability(driver):
                EmailNotificationService.sendSuccessEmail()
                exit()
            time.sleep(randrange(REFRESH_INTERVAL_RANGE_START_SECOND, REFRESH_INTERVAL_RANGE_END_SECOND))
            driver.refresh()
            sentBackToLoginPage = checkIsLoginPage(driver)
        doLogIn(driver)
except:
    EmailNotificationService.sendCrashEmail()

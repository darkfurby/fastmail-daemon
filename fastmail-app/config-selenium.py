from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


login = sys.argv[1] 
password = sys.argv[2]

class Email:
    sender = ''
    subject = ''
    number = 0
    time = ''
    content = ''

def driver_return(url):
    #config
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome('../driver/chromedriver', options=options)
    # driver = webdriver.Chrome('../driver/chromedriver')
    driver.get(url)
    return driver

def login_to_website(driver):
    #login to website
    login_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "v16-input")))
    password_element = driver.find_element_by_id("v17-input")
    login_element.send_keys(login)
    password_element.send_keys(password)
    button_confirm_credentials = driver.find_element_by_class_name("v-Button--constructive")
    button_confirm_credentials.click()

def get_emails_and_content(driver):
    #get emails
    emails_objects_array = []
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME , "app-list")))
    email_container_element = driver.find_element_by_class_name('app-list')
    emails_array = email_container_element.find_elements_by_tag_name('a')

    for email in emails_array:
        email.click()
        email_object = Email()
        div_email_elements = email.find_elements_by_tag_name('div')
        for div in div_email_elements:

            if div.get_attribute('class') == "v-MailboxItem-subject u-ellipsis":
                email_object.subject = div.get_attribute('title')
            
            if div.get_attribute('class') == "v-MailboxItem-time":
                email_object.time = div.get_attribute('title')
            
            inside_div = div.find_elements_by_tag_name('span')
            for span in inside_div:
                if span.get_attribute('class') == "v-MailboxItem-name":
                    get_sender = span.find_elements_by_tag_name('span')
                    email_object.sender = get_sender[0].get_attribute('title')

        email.click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH , "//*[contains(@class, 'u-article')]")))
        content = driver.find_element_by_xpath("//*[contains(@class, 'u-article')]")
        cont = content.get_attribute('innerHTML')
        email_object.content = cont
        emails_objects_array.append(email_object)
    return emails_objects_array


def exec():
    driver = driver_return('https://www.fastmail.com/login/')
    login_to_website(driver)
    return get_emails_and_content(driver)


exec()
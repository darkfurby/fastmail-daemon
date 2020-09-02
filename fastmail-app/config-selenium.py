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
    def __init__(self, sender, subject, number, year, month, day, time):
        self.sender = sender
        self.subject = subject
        self.number = number
        self.year = year
        self.month = month
        self.day = day
        self.time = time

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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "v35")))
    email_container_element = driver.find_element_by_id('v35')
    emails_array = email_container_element.find_elements_by_tag_name('a')

    for email in emails_array:
        div_email_element = email.find_elements_by_tag_name('div')
        for email_part in div_email_element:
            # if len( email_part.get_attribute('title') ) > 0:
            #     print(email_part.get_attribute('title'))
            #get sender
            if email_part.get_attribute('class') == "v-MailboxItem-from":
                # mail_from = email_part.find_element_by_class_name("v-MailboxItem-from")
                mail_from = email_part.find_element_by_class_xpath()
                print(mail_from)

            # inside_div_content = email_part.find_elements_by_class_name("v-MailboxItem-from")
            # print(inside_div_content)
            # for inside in inside_div_content:
            #     print('to co mamy inside: ' + inside)
            #     span = inside.find_elements_by_class_name('v-MailboxItem-name')
            #     sender = span.get_attribute('title')
            #     print( sender )


def main():
    driver = driver_return('https://www.fastmail.com/login/')
    login_to_website(driver)
    get_emails_and_content(driver)


if __name__ == "__main__":
    # execute only if run as a script
    main()


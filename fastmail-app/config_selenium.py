from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import importlib
import os
import random
import glob

login = os.environ.get('LOGIN')
password = os.environ.get('PASSWORD')

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
    options.add_argument('--window-size=1920,1080')
    # driver = webdriver.Chrome(executable_path='./driver/chromedriver', options=options)
    driver = webdriver.Chrome(executable_path='../driver/chromedriver', options=options)
    # driver = webdriver.Chrome(options=options)
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
    print("liczba maili ktore zgarnal" + str( len(emails_array) ))

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
                    get_sender = ''
                    attempts = 0
                    while(attempts < 3):
                        try:
                            get_sender = span.find_elements_by_tag_name('span')
                            break
                        except StaleElementException:
                            print("nie widzi elementu")

                    email_object.sender = get_sender[0].get_attribute('title')
                    

        # email.click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH , "//*[contains(@class, 'u-article')]")))
        content = driver.find_element_by_xpath("//*[contains(@class, 'u-article')]")
        cont = content.get_attribute('innerHTML')
        email_object.content = cont
        emails_objects_array.append(email_object)
    return emails_objects_array

def save_emails_as_files(emails_array):
    mailbox_folder = "mailbox"
    if not os.path.exists(mailbox_folder):
        os.makedirs(mailbox_folder)

    for item in emails_array:
        filename = item.sender + "-" + item.subject

        if os.path.isfile("./" + mailbox_folder + "/" + filename):
            extra_number = random.getrandbits(32)
            f = open(mailbox_folder + "/" + filename + "[-" + str(extra_number) + "]", "w")
            f.write(item.content)
            f.close()
        else:
            f = open(mailbox_folder + "/" + filename,"w")
            f.write(item.content)
            f.close()

def clear_mailbox():
    folder = glob.glob('mailbox/*')
    for f in folder:
        os.remove(f)

def sele_exec():
    while True:
        try:
            clear_mailbox()
            driver = driver_return('https://www.fastmail.com/login/')
            login_to_website(driver)
            dawajListe = get_emails_and_content(driver)
            for i in dawajListe:
                print( i.sender + " " +  i.subject + " " + i.time + " " + i.content)
            save_emails_as_files(dawajListe)
            driver.close()
            break
        except:
            print("this run failed, let me try again")



sele_exec()
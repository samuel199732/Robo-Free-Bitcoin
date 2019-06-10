from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pprint import pprint
from time import sleep
from config import config

driver = webdriver.Chrome('./chromedriver')
wait = WebDriverWait(driver, 5)


def login():
    driver.get('https://freebitco.in/?op=home')
    try:
        wait.until(EC.visibility_of_element_located((By.ID, 'push_notification_modal')))
        background = driver.find_element_by_css_selector('body > div.reveal-modal-bg')
        background.click()
    except Exception as e:
        pprint('without modal')

    botao = driver.find_element_by_css_selector(
        'body > div.large-12.fixed > div > nav > section > ul > li.login_menu_button > a')
    botao.click()
    driver.find_element_by_id('login_form_btc_address').send_keys(config.email)
    driver.find_element_by_id('login_form_password').send_keys(config.senha)
    driver.find_element_by_id('login_button').click()
    try:
        wait.until(EC.url_to_be('https://freebitco.in/?op=home'))
    except Exception as e:
        pass


def islogin():
    try:
        login = driver.get_cookie('password')
        return True if not (login is None) else False
    except Exception as e:
        return False


def rollnumber():
    try:
        wait.until(EC.visibility_of_element_located((By.ID, 'push_notification_modal')))
        background = driver.find_element_by_css_selector('body > div.reveal-modal-bg')
        background.click()
    except Exception as e:
        pass

    try:
        wait.until(EC.visibility_of_element_located((By.ID, 'free_play_form_button')))
        if driver.find_element_by_css_selector('div#play_without_captchas_button.play_without_captcha_button.center'):
            driver.execute_script('document.querySelector("#play_without_captchas_button").click()')
            driver.execute_script('document.querySelector("#free_play_form_button").click()')
            num = driver.execute_script('return document.querySelector("#free_play_digits").textContent')
            pprint('Number drawn ' + str(num).replace(' ', ""))
            driver.refresh()
    except Exception as e:
        pprint("I can't play yet")
        sleep(60)


def main():
    while True:
        if not islogin():
            login()
        else:
            rollnumber()


main()

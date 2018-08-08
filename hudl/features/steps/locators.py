from selenium.webdriver.common.by import By

class locator(object):
    top_header         = (By.XPATH, '//*[@id="ssr-webnav"]/div/div[1]/nav[1]'),
    avatar = (By.XPATH, '//*[@id="ssr-webnav"]/div/div[1]/nav[1]/div[4]/div[2]/div[1]/div[1]/div')
    form_login      = (By.XPATH, '/html/body/div[2]/form[1]'),
    form_username   = (By.ID, 'username'),
    form_password   = (By.ID, 'password'),
    button_login   = (By.CSS_SELECTOR, '#logIn'),
    logo          = (By.XPATH, '/html/body/div[2]/form[1]/div[1]'),
    login_error_module     = (By.XPATH, '/html/body/div[2]/form[1]/div[3]/div')

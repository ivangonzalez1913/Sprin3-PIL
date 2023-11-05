'''
Created on 1 nov. 2023

@author: ivang
'''
from selenium.webdriver.common.by import By
class RegistroLocators:
    CONTINUAR_BTN = (By.ID, "continue-email_btn")
    EMAIL_INPUT = (By.ID, "email")
    INGRESAR_BTN = (By.ID, "insert-email_btn")
    NAME_INPUT = (By.ID, "name")
    INGRESAR_NAME_BTN = (By.ID, "insert-name_btn")
    DATOS_BTN = (By.LINK_TEXT, "DATOS PERSONALES")
    DNI_INPUT = (By.ID, "Dni")
    BIRTH_INPUT = (By.ID, "BirthDate")
    PROVINCIA_BTN = (By.ID, "Province")
    PHONE_INPUT = (By.ID, "PhoneNumber")
    GENDER_BTN = (By.ID, "Gender")
    GUARDAR_BTN = (By.XPATH, "/html//div[@id='contentbar-widget']//form[@method='post']//button[@type='button']")
    DATOS_TXT = (By.ID, "swal2-title")
    OK_BTN = (By.XPATH, "/html//div[@role='dialog']/div[@class='swal2-actions']/button[1]")
    DNI_ERROR_TXT = (By.XPATH, "/html//div[@id='contentbar-widget']/div//form[@method='post']/div[2]//label[.='^ Máximo 9 caracteres']")
    EMAIL_ERROR_TXT = (By.XPATH, "//div[@id='insert-email_card']/form//label[.='^ E-mail inválido']")
class LoginPage():
    def __init__(self, driver):
        self.driver = driver
    def get_continuar_btn(self):
        return self.driver.find_element(*RegistroLocators.CONTINUAR_BTN)
    def get_email_input(self):
        return self.driver.find_element(*RegistroLocators.EMAIL_INPUT)
    def get_ingresar_btn(self):
        return self.driver.find_element(*RegistroLocators.INGRESAR_BTN)
    def get_name_input(self):
        return self.driver.find_element(*RegistroLocators.NAME_INPUT)
    def get_ingresar_name_btn(self):
        return self.driver.find_element(*RegistroLocators.INGRESAR_NAME_BTN)
    def get_datos_input(self):
        return self.driver.find_element(*RegistroLocators.DATOS_BTN)
    def get_dni_input(self):
        return self.driver.find_element(*RegistroLocators.DNI_INPUT)
    def get_birth_input(self):
        return self.driver.find_element(*RegistroLocators.BIRTH_INPUT)
    def get_provincia_btn(self):
        return self.driver.find_element(*RegistroLocators.PROVINCIA_BTN)
    def get_phone_input(self):
        return self.driver.find_element(*RegistroLocators.PHONE_INPUT)
    def get_gender_btn(self):
        return self.driver.find_element(*RegistroLocators.GENDER_BTN)
    def get_guardar_btn(self):
        return self.driver.find_element(*RegistroLocators.GUARDAR_BTN)
    def get_datos_txt(self):
        return self.driver.find_element(*RegistroLocators.DATOS_TXT)
    def get_ok_btn(self):
        return self.driver.find_element(*RegistroLocators.OK_BTN)
    def get_dni_error_txt(self):
        return self.driver.find_element(*RegistroLocators.DNI_ERROR_TXT)
    def get_email_error_txt(self):
        return self.driver.find_element(*RegistroLocators.EMAIL_ERROR_TXT)
    
    
    
    
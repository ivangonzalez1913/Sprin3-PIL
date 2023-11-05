'''
Created on 5 nov. 2023

@author: ivang

'''
import unittest
import time
from selenium import webdriver
from Pages import RegistroPage

class TestRegistro(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15) 
        self.driver.maximize_window() 
        self.driver.get("https://www.farmaciageneralpaz.com/login")
    def test_registro_usuario(self):
        driver = self.driver
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        farmacia_login = RegistroPage.LoginPage(self.driver)
        time.sleep(5)
        farmacia_login.get_continuar_btn().click()
        email_incorrecto = "asdasd%&.u"
        farmacia_login.get_email_input().send_keys(email_incorrecto)
        time.sleep(5)
        farmacia_login.get_ingresar_btn().click()
        time.sleep(3)
        email_error_text = farmacia_login.get_email_error_txt().text
        self.assertEqual(email_error_text, "^ E-mail inválido")
        self.driver.save_screenshot("emailinvalido.png")
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
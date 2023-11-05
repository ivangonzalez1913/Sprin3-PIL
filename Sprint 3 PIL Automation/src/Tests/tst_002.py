'''
Created on 5 nov. 2023

@author: ivang
'''
import unittest
import time
from selenium import webdriver
from Functions import Funciones
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
        
        farmacia_login.get_email_input().send_keys(Funciones.funciones_registros.generar_email(self))
        
        time.sleep(3)
        farmacia_login.get_ingresar_btn().click()
        
        time.sleep(5)
        name = "Ivan Gonzalez"
        farmacia_login.get_name_input().send_keys(name)
       
        farmacia_login.get_ingresar_name_btn().click()
        
        farmacia_login.get_datos_input().click()
        
        time.sleep(5)
        dni = 1234567890
        farmacia_login.get_dni_input().send_keys(dni)
        time.sleep(5)
        farmacia_login.get_guardar_btn().click()
        dni_error_text = farmacia_login.get_dni_error_txt().text
        self.assertEqual(dni_error_text, "^ Máximo 9 caracteres")
        self.driver.save_screenshot("dnicaracteres.png")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
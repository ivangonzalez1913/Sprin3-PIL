'''
Created on 30 oct. 2023

@author: ivang
'''
import unittest
import time
import re
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

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
        
        email_aleatorio = Funciones.funciones_registros.generar_email(self)
        formato_valido = re.match(r"^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email_aleatorio)
        farmacia_login.get_email_input().send_keys(email_aleatorio)
        self.assertIsNotNone(formato_valido, "Email invalido")
        self.driver.save_screenshot("emailvalido.png")
        time.sleep(5)
        farmacia_login.get_ingresar_btn().click()
        
        time.sleep(5)
        name = "Ivan Gonzalez"
        farmacia_login.get_name_input().send_keys(name)
        self.assertTrue(isinstance(name, str), "El nombre ingresado no es valido")
        self.driver.save_screenshot("name.png")
       
        farmacia_login.get_ingresar_name_btn().click()
        
        farmacia_login.get_datos_input().click()
        
        time.sleep(5)
        dni = 12345678
        dni_str = str(dni)
        dni_length = len(dni_str)
        farmacia_login.get_dni_input().send_keys(dni)
        self.assertTrue(isinstance(dni, (int,float)), "el numero ingresado no es valido")
        self.assertLess(dni_length, 9, "Maximo de 9 caracteres")
        farmacia_login.get_birth_input().send_keys("11111999")
        
        time.sleep(3)
        phone = 3514569282
        farmacia_login.get_phone_input().send_keys(phone)
        self.assertTrue(isinstance(phone, (int,float)), "Solo se permiten numeros")
        time.sleep(5)
        select_provincia = farmacia_login.get_provincia_btn()
        select_provincia.click()
       
        select_option_provincia = Select(select_provincia)
        select_option_provincia.select_by_index(1)
        time.sleep(5)
        select_genero = farmacia_login.get_gender_btn()
        select_genero.click()
        
        select_option_genero = Select(select_genero)
        select_option_genero.select_by_index(2)
        time.sleep(5)
        self.driver.save_screenshot("datospersonales.png")
        farmacia_login.get_guardar_btn().click()
        time.sleep(3)
        datos_actualizados = farmacia_login.get_datos_txt()
        datos_actualizados_text = datos_actualizados.text
        datos_actualizados_text_esperado = "Datos actualizados"
        datos_actualizados= driver.find_element(By.ID, "swal2-title")
        self.assertIn(datos_actualizados_text_esperado, datos_actualizados_text, f"El texto obtenido '{datos_actualizados_text}' no coincide con el texto esperado '{datos_actualizados_text_esperado}'.")
        time.sleep(5)
        self.driver.save_screenshot("datosactualizados.png")
        farmacia_login.get_ok_btn().click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
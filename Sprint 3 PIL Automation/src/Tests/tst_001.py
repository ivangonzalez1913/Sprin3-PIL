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
        print("Se muestran las opciones de registro")
        farmacia_login.get_continuar_btn().click()
        print("Se redirige a la pantalla para ingresar email")
        email_aleatorio = Funciones.funciones_registros.generar_email(self)
        formato_valido = re.match(r"^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email_aleatorio)
        farmacia_login.get_email_input().send_keys(email_aleatorio)
        self.assertIsNotNone(formato_valido, "Email invalido")
        print("mediante assert, se verifica que el email es valido")
        self.driver.save_screenshot("emailvalido.png")
        time.sleep(5)
        farmacia_login.get_ingresar_btn().click()
        print("se redirige a la pantalla para ingresar nombre")
        time.sleep(5)
        name = "Ivan Gonzalez"
        farmacia_login.get_name_input().send_keys(name)
        self.assertTrue(isinstance(name, str), "El nombre ingresado no es valido")
        self.driver.save_screenshot("name.png")
        print("se verifica mediante assert que el nombre solo contiene letras")
       
        farmacia_login.get_ingresar_name_btn().click()
        
        farmacia_login.get_datos_input().click()
        print("se redirige a la pagina de datos personales")
        time.sleep(5)
        dni = 12345678
        dni_str = str(dni)
        dni_length = len(dni_str)
        farmacia_login.get_dni_input().send_keys(dni)
        self.assertTrue(isinstance(dni, (int,float)), "el numero ingresado no es valido")
        self.assertLess(dni_length, 9, "Maximo de 9 caracteres")
        print("se verifica mediante asserts que el dni ingresado solo contiene numeros y tiene una longitud maxima de 9 caracteres")
        farmacia_login.get_birth_input().send_keys("11111999")
        
        time.sleep(3)
        phone = 3514569282
        farmacia_login.get_phone_input().send_keys(phone)
        self.assertTrue(isinstance(phone, (int,float)), "Solo se permiten numeros")
        print("se verifica mediante asserts que el numero ingresado no contiene letras")
        time.sleep(5)
        select_provincia = farmacia_login.get_provincia_btn()
        select_provincia.click()
        print("se clickea en provincia y se muestran las opciones")
        select_option_provincia = Select(select_provincia)
        select_option_provincia.select_by_index(1)
        print("se selecciona una provincia")
        time.sleep(5)
        select_genero = farmacia_login.get_gender_btn()
        select_genero.click()
        print("se clickea en genero y se muestran las opciones")
        select_option_genero = Select(select_genero)
        select_option_genero.select_by_index(2)
        print("se selecciona una opcion")
        time.sleep(5)
        self.driver.save_screenshot("datospersonales.png")
        farmacia_login.get_guardar_btn().click()
        print("se clickea en el boton para guardar datos")
        time.sleep(3)
        datos_actualizados = farmacia_login.get_datos_txt()
        datos_actualizados_text = datos_actualizados.text
        datos_actualizados_text_esperado = "Datos actualizados"
        datos_actualizados= driver.find_element(By.ID, "swal2-title")
        self.assertIn(datos_actualizados_text_esperado, datos_actualizados_text, f"El texto obtenido '{datos_actualizados_text}' no coincide con el texto esperado '{datos_actualizados_text_esperado}'.")
        print("se verifica mediante asserts que el texto en el cartel es datos actualizados")
        time.sleep(5)
        self.driver.save_screenshot("datosactualizados.png")
        farmacia_login.get_ok_btn().click()
        print("se clickea el boton de ok y se redirige a la pagina mi cuenta")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
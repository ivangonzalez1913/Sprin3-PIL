'''
Created on 31 oct. 2023

@author: ivang
'''
import random
import string
class funciones_registros:
    def generar_email(self):
        dominio="example.com"
        direccion_longitud = random.randint(5,10)
        direccion_aleatoria = "".join(random.choice(string.ascii_lowercase + string.digits)for _ in range(direccion_longitud))
        email_aleatorio = f"{direccion_aleatoria}@{dominio}"
        return email_aleatorio

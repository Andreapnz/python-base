#!/usr/bin/env python3 
"""
Hello World Multi Linguas.

Dependendo da ligua configurada no ambiente o programa exibe a mensagem correspondentes.

Como usar:

Tenha a variável LANG devidamente configurada ex:
    
    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Andréa Correia"
__license__ = "Unlicense"

#Dunder (substitui o __ no final e no fim)


# if __name__ == "__main__":  Define o bloco principal de um script python, todo codigo que a gente coloca em baixo dessa linha dando 4 espaços é o codigo que vai ser executado quando o programa rodar dentro do terminal

import os 


current_language = os.getenv("LANG")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language =="fr_FR":
    msg = "Bonjour Mode!"

print(msg) 





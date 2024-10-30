import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep, time
import signal
import sys
import requests

# Configurações de hardware
GPIO.setmode(GPIO.BOARD)

# Iniciando o leitor RFID
leitorRfid = SimpleMFRC522()

# Função para finalizar o programa
def finalizar_programa(signal, frame):
    print("\nFinalizando o programa...")
    GPIO.cleanup()
    sys.exit(0)

# Captura o sinal de interrupção (CTRL+C)
signal.signal(signal.SIGINT, finalizar_programa)

try:
    while True:
        print("Aguardando leitura da tag...")
        tag_data = leitorRfid.read()
        tag, nada = tag_data
        tag = int(tag)
        print(f"ID do cartão: {tag}")

        sleep(1)

finally:
    GPIO.cleanup()
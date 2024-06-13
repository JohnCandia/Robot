import pyautogui
import webbrowser
import time
import random

# Función para cerrar la ventana del navegador
def close_browser():
    # Simula la combinación de teclas Ctrl + w para cerrar la pestaña del navegador
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2)  # Espera 2 segundos para que la pestaña se cierre completamente

# Bucle que se ejecuta 5 veces
contador = 0
while contador < 5:
    # Abre google.com en el navegador predeterminado
    webbrowser.open("https://www.google.com")

    # Genera un tiempo de espera aleatorio entre 5 y 10 segundos
    tiempo_espera = random.randint(5, 10)
    print(f"Esperando {tiempo_espera} segundos...")
    time.sleep(tiempo_espera)

    # Cierra el navegador
    close_browser()

    contador += 1
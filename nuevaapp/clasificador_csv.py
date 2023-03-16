import os
import shutil
from datetime import datetime
import time
from plyer import notification

# Cambia esta ruta al directorio de descargas en tu computadora
directorio_descargas = r'C:\Users\Usuario\Downloads'

# Cambia esta ruta al directorio donde quieres mover los archivos
directorio_destino = r'C:\Users\Usuario\Desktop\Programación\Proyecto Análisis de Datos Entrenos\Datos de entrenamiento'

def enviar_notificacion(titulo, mensaje):
    notification.notify(
        title=titulo,
        message=mensaje,
        timeout=5,  # Duración de la notificación en segundos
    )

def mover_archivos_csv(directorio_descargas, directorio_destino):
    for archivo in os.listdir(directorio_descargas):
        if archivo.endswith('.csv'):
            fecha_str, ejercicio = archivo[:-4].rsplit('-', 1)
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d')

            carpeta_ejercicio = os.path.join(directorio_destino, ejercicio)
            os.makedirs(carpeta_ejercicio, exist_ok=True)

            ruta_original = os.path.join(directorio_descargas, archivo)
            ruta_destino = os.path.join(carpeta_ejercicio, archivo)

            if os.path.exists(ruta_destino):
                # Opción 1: Sobrescribir
                # shutil.move(ruta_original, ruta_destino)

                # Opción 2: Renombrar archivo entrante
                base, extension = os.path.splitext(ruta_destino)
                i = 1
                while os.path.exists(ruta_destino):
                    ruta_destino = f"{base}-{i}{extension}"
                    i += 1
                shutil.move(ruta_original, ruta_destino)

                # Opción 3: No mover el archivo (comentar las líneas anteriores)

                enviar_notificacion("Archivo duplicado", f"El archivo {archivo} ya existe y ha sido renombrado.")
            else:
                shutil.move(ruta_original, ruta_destino)
                enviar_notificacion("Archivo movido", f"El archivo {archivo} ha sido movido a {ruta_destino}")

if __name__ == "__main__":
    while True:
        try:
            mover_archivos_csv(directorio_descargas, directorio_destino)
        except Exception as e:
            enviar_notificacion("Error", f"Se encontró un error: {str(e)}")
        time.sleep(5)

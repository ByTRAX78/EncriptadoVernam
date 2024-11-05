# Importamos las librerías necesarias
import numpy as np
from collections import Counter

# Función para calcular la entropía de un mensaje
def calcular_entropia(mensaje):
    # Conteo de frecuencia de cada símbolo en el mensaje
    frecuencia = Counter(mensaje)
    # Longitud total del mensaje
    longitud_mensaje = len(mensaje)
    # Calculo de la probabilidad de cada símbolo
    probabilidad = [frec / longitud_mensaje for frec in frecuencia.values()]
    # Cálculo de la entropía usando la fórmula de Shannon
    entropia = -sum([p * np.log2(p) for p in probabilidad])
    return entropia

# Función para realizar el cifrado de Vernam
def cifrado_vernam(mensaje, clave):
    # Convertimos el mensaje y la clave a listas de enteros binarios
    mensaje_binario = [ord(char) for char in mensaje]
    clave_binario = [ord(char) for char in clave]
    # Aplicamos XOR entre el mensaje y la clave
    mensaje_cifrado = [mb ^ kb for mb, kb in zip(mensaje_binario, clave_binario)]
    # Convertimos el mensaje cifrado a caracteres
    mensaje_cifrado_texto = ''.join([chr(c) for c in mensaje_cifrado])
    return mensaje_cifrado_texto

# Función principal para ejecutar la práctica
def ejecutar_practica():
    # Mensaje de ejemplo y clave
    mensaje = "HELLOCRYPTO"
    clave = "XMCKLQPMNZ"  # Debe ser de la misma longitud que el mensaje

    print(f"Mensaje original: {mensaje}")
    print(f"Clave utilizada: {clave}")

    # Calcular entropía del mensaje original
    entropia_mensaje = calcular_entropia(mensaje)
    print(f"Entropía del mensaje original: {entropia_mensaje:.4f}")

    # Cifrar el mensaje usando Vernam
    mensaje_cifrado = cifrado_vernam(mensaje, clave)
    print(f"Mensaje cifrado: {mensaje_cifrado}")

    # Calcular entropía del mensaje cifrado
    entropia_cifrado = calcular_entropia(mensaje_cifrado)
    print(f"Entropía del mensaje cifrado: {entropia_cifrado:.4f}")

# Ejecutamos la práctica
ejecutar_practica()

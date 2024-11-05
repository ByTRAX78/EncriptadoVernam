# Cálculo de Entropía y Cifrado de Vernam

Este proyecto implementa un programa en Python que calcula la entropía de un mensaje de texto y lo cifra utilizando el cifrado de Vernam. Este tipo de cifrado es un método de clave simétrica que utiliza una clave de igual longitud que el mensaje, aplicando una operación XOR entre los valores binarios de ambos.

## Contenido

- **`calcular_entropia(mensaje)`**: Calcula la entropía de un mensaje basado en la frecuencia de los caracteres que lo componen.
- **`cifrado_vernam(mensaje, clave)`**: Cifra un mensaje usando el cifrado de Vernam, basado en una clave de igual longitud que el mensaje.
- **`ejecutar_practica()`**: Función principal que muestra el flujo de la práctica, realizando el cálculo de la entropía y el cifrado.

## Requisitos

Este código requiere las siguientes librerías:

- `numpy`
- `collections.Counter`

Instalación de `numpy`:

```bash
pip install numpy
```

## Descripción de las Funciones

### 1. `calcular_entropia(mensaje)`

Esta función calcula la entropía de un mensaje basado en la fórmula de Shannon, la cual mide el nivel de incertidumbre o aleatoriedad en el mensaje. La entropía se calcula mediante la frecuencia de aparición de cada símbolo en el mensaje.

### 2. `cifrado_vernam(mensaje, clave)`

El cifrado de Vernam es una técnica de clave simétrica en la cual cada símbolo del mensaje se cifra aplicando una operación XOR con el símbolo correspondiente en la clave. La clave debe ser de igual longitud que el mensaje y se convierte en un valor binario para aplicar la operación XOR.

### 3. `ejecutar_practica()`

Función que orquesta la ejecución de la práctica:
- Define un mensaje y una clave.
- Calcula la entropía del mensaje original.
- Cifra el mensaje utilizando el cifrado de Vernam.
- Calcula la entropía del mensaje cifrado.
- Muestra los resultados.

## Ejecución del Código

Para ejecutar el programa, simplemente llama a la función `ejecutar_practica()`. Esto mostrará el mensaje original, la clave utilizada, el mensaje cifrado y las entropías antes y después del cifrado.

```python
ejecutar_practica()
```

## Ejemplo de Salida

A continuación se muestra un ejemplo de salida del programa al ejecutar `ejecutar_practica()`:

```
Mensaje original: HELLOCRYPTO
Clave utilizada: XMCKLQPMNZ
Entropía del mensaje original: 3.0958
Mensaje cifrado:  ◄♦█☼j♪♠§
Entropía del mensaje cifrado: 3.3219
```

En el ejemplo anterior:
- El mensaje original es `HELLOCRYPTO`.
- La clave utilizada es `XMCKLQPMNZ`, de igual longitud que el mensaje.
- La entropía del mensaje original es 3.0958, mientras que la entropía del mensaje cifrado aumenta a 3.3219, lo que indica un mayor nivel de aleatoriedad y seguridad en el mensaje cifrado.

## Contacto

Para cualquier consulta o sugerencia, puedes contactar al desarrollador:

- **Autor original del código**: Lechuga Blanco Fatima Margarita
- **Nombre**: Adrian Martinez Martinez
- **Correo**: martinezmartinezaadrian@gmail.com
- **GitHub**: [ByTRAX78](https://github.com/ByTRAX78)


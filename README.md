# MCOC-Proyecto-0

# Descripción
En este proyecto se demostrará el error que se produce al calcular directamente en la calculadora vs en la funcion float32.

# Función a utilizar
Para esta comaparación utilicé la siguiente función cúbica: *x^3 - 1*

Se entregan los resultados obtenidos en la calculadora y los obtenidos con .float32

# Resultados
Se definió el error como:
*Error = resultado_float - resultado_calculadora/resultado calculadora*

*Output Consola*

```
resultado float 64: [-0.99482226, -0.9998008, -1.0]
resultado calculadora: [-0.999999994822283, -0.9999999998008233, -0.9999999999999866]
Error: [-0.005177731131440427, -0.00019919852370235602, -1.3433698597964574e-14]
```

Como se puede apreciar en el output, el tercer número al ser muy pequeño en python se aproxima a 1.0, esto de por si ya nos dice que hay pérdida de significancia en float. 
Por otro lado, se aprecia que el error es menor a medida que el valor de x va disminuyendo. Esto es así debido a que es una función cúbica y debido al signo negativo de la operación.

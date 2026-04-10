Universidad Veracruzana


Creador de repositorio 
Alfredo Cid García	Matrícula: zs24013120 - zs24013120@estudiantes.uv.mx
# Codigos para la resolución de problemas con metodos numericos

Este repositorio contiene la implementación en Python de 5 métodos numéricos para encontrar raíces aproximadas de ecuaciones no lineales f(x) = 0. 
## Métodos Incluidos
1. **Método de Bisección** (Cerrado)
2. **Método de Falsa Posición** (Cerrado)
3. **Método de Newton-Raphson** (Abierto)
4. **Método de la Secante** (Abierto)
5. **Método de Punto Fijo** (Abierto)

## Características Especiales del Código
* **Cálculo de Error Dual:** Todos los scripts calculan de forma simultánea el **Error Absoluto** y el **Error Relativo Porcentual**, permitiendo detener el algoritmo con la tolerancia que el usuario requiera.
* **Evaluación Dinámica:** Utiliza la función `eval()` acoplada con la librería `math`, permitiendo al usuario ingresar la ecuación algebraicamente directo en la consola (ej. `math.exp(3*x) - 4`).
* **Protección Algorítmica:** Condiciones de seguridad implementadas para evitar bucles infinitos (límite de 100 iteraciones) y manejo de excepciones matemáticas (derivadas horizontales $f'(x) = 0$).
* **Análisis Visual (Gráficas de Convergencia):** Al encontrar la raíz, el programa despliega automáticamente una gráfica utilizando `matplotlib` que ilustra la caída de la magnitud del error a lo largo de las iteraciones.

## ⚙️ Requisitos y Ejecución

Para ejecutar estos scripts necesitas Python 3.x y la librería `matplotlib` para la generación de gráficas.

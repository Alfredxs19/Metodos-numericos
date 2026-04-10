import matplotlib.pyplot as plt
import math
print("Método de Newton-Raphson (con error y gráfica de convergencia)")
ecuacion = input("Ingresa la ecuación f(x): ")
# Para elevar a una potencia usa x**n
derivada = input("Ingresa la derivada f'(x): ")
x = float(input("Ingresa el valor inicial (x0): ")) 
tol = float(input("Ingresa la tolerancia deseada: "))
def f(x_val):
    return eval(ecuacion, {"x": x_val,"math": math})
def df(x_val):
    return eval(derivada, {"x": x_val,"math": math})
print(f"\n{'Iter':^6} | {'x':^10} | {'f(x)':^10} | {'f_der(x)':^10} | {'Err Abs':^10} | {'Err %':^10}")
i = 1 
historial_iteraciones = []
historial_error_abs = []
historial_error_porc = []
while True:
    fx = f(x)
    dfx = df(x)
    if dfx == 0:
        print("-" * 75)
        print("¡Error! La derivada se hizo cero. El método matemático falla aquí.")
        break
    x_nuevo = x - (fx / dfx)
    error_abs = abs(x_nuevo - x)
    if x_nuevo != 0:
        error_porc = abs((x_nuevo - x) / x_nuevo) * 100
    else:
        error_porc = 100
    str_error_abs = f"{error_abs:.6f}"
    str_error_porc = f"{error_porc:.4f}%"
    historial_iteraciones.append(i)
    historial_error_abs.append(error_abs)
    historial_error_porc.append(error_porc)
    print(f"{i:^6} | {x:^10.4f} | {fx:^10.4f} | {dfx:^10.4f} | {str_error_abs:^10} | {str_error_porc:^10}")
    if error_porc < tol:
        print(f"La raíz se encontró en la iteración {i}: {x_nuevo:.6f}")
        break 
    if i >= 100:
        print("Por si el algoritmo no converge")
        break
    x = x_nuevo  
    i += 1
#Parte de la grafica
if len(historial_iteraciones) > 0:
    plt.figure(figsize=(8, 5))
    # Línea azul para el error absoluto
    plt.plot(historial_iteraciones, historial_error_abs, marker='o', color='blue', label='Error Absoluto', linewidth=2)
    # Línea naranja para el error porcentual
    plt.plot(historial_iteraciones, historial_error_porc, marker='s', color='orange', label='Error Porcentual (%)', linewidth=2)
    plt.title("Gráfica de Convergencia: Newton-Raphson")
    plt.xlabel("Número de Iteración")
    plt.ylabel("Magnitud del Error")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    # Mostramos la ventana emergente
    plt.show()
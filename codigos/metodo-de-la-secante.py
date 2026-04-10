import matplotlib.pyplot as plt
import math
print("Método de la Secante (con error y gráfica de convergencia)")
ecuacion = input("Ingresa la ecuación f(x): ")
# Para elevar a una potencia usa x**n
x0 = float(input("Ingresa el primer valor  (x0): ")) 
x1 = float(input("Ingresa el segundo valor (x1): ")) 
tol = float(input("Ingresa la tolerancia deseada: "))
def f(x_val):
    return eval(ecuacion, {"x": x_val,"math": math})
print(f"\n{'Iter':^6} | {'x0':^10} | {'x1':^10} | {'f(x0)':^10} | {'f(x1)':^10} | {'Err Abs':^10} | {'Err %':^10}")
i = 1 
historial_iteraciones = []
historial_error_abs = []
historial_error_porc = []
while True:
    fx0 = f(x0)
    fx1 = f(x1)
    if (fx1 - fx0) == 0:
        print("¡Error! División entre cero. La línea es completamente horizontal.")
        break
    x_nuevo = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
    error_abs = abs(x_nuevo - x1)
    if x_nuevo != 0:
        error_porc = abs((x_nuevo - x1) / x_nuevo) * 100
    else:
        error_porc = 100
    str_error_abs = f"{error_abs:.6f}"
    str_error_porc = f"{error_porc:.4f}%"
    historial_iteraciones.append(i)
    historial_error_abs.append(error_abs)
    historial_error_porc.append(error_porc)
    print(f"{i:^6} | {x0:^10.4f} | {x1:^10.4f} | {fx0:^10.4f} | {fx1:^10.4f} | {str_error_abs:^10} | {str_error_porc:^10}")
    if error_porc < tol:
        print(f"La raíz se encontró en la iteración {i}: {x_nuevo:.6f}")
        break 
    if i >= 100:
        print("Por si el algoritmo no converge (alcanzó 100 iteraciones)")
        break
    x0 = x1  
    x1 = x_nuevo  
    i += 1
#Parte de la grafica
if len(historial_iteraciones) > 0:
    plt.figure(figsize=(8, 5))
    # Línea azul para el error absoluto
    plt.plot(historial_iteraciones, historial_error_abs, marker='o', color='blue', label='Error Absoluto', linewidth=2)
    # Línea naranja para el error porcentual
    plt.plot(historial_iteraciones, historial_error_porc, marker='s', color='orange', label='Error Porcentual (%)', linewidth=2)
    plt.title("Gráfica de Convergencia: Método de la Secante")
    plt.xlabel("Número de Iteración")
    plt.ylabel("Magnitud del Error")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    # Mostramos la ventana
    plt.show()
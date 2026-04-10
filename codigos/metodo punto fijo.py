import matplotlib.pyplot as plt
import math
print("Método de Punto Fijo (con error y gráfica de convergencia)")
ecuacion_g = input("Ingresa la ecuación despejada g(x): ") 
# Para elevar a una potencia usa x**n
x = float(input("Ingresa el valor inicial (x0): ")) 
tol = float(input("Ingresa la tolerancia deseada: "))
def g(x_val):
    return eval(ecuacion_g, {"x": x_val,"math": math})
print(f"\n{'Iter':^6} | {'x':^10} | {'g(x)':^10} | {'Err Abs':^10} | {'Err %':^10}")
i = 1 
historial_iteraciones = []
historial_error_abs = []
historial_error_porc = []
while True:
    gx = g(x)
    x_nuevo = gx
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
    print(f"{i:^6} | {x:^10.4f} | {gx:^10.4f} | {str_error_abs:^10} | {str_error_porc:^10}")
    if error_porc < tol:
        print(f"La raíz (punto fijo) se encontró en la iteración {i}: {x_nuevo:.6f}")
        break 
    if i >= 100:
        print("Por si el algoritmo no converge (diverge o alcanzó 100 iteraciones)")
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
    plt.title("Gráfica de Convergencia: Método de Punto Fijo")
    plt.xlabel("Número de Iteración")
    plt.ylabel("Magnitud del Error")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    # Mostramos la ventana
    plt.show()
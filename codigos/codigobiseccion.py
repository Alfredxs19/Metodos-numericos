import matplotlib.pyplot as plt
import math
print("Método de bisección (con error absoluto y porcentual)")
# El error comenzará a calcularse a partir de la iteración 2
ecuacion = input("Ingresa la ecuación f(x): ")
a = float(input("Ingresa el primer intervalo (a): "))
b = float(input("Ingresa el segundo intervalo (b): "))
tol = float(input("Ingresa la tolerancia deseada: "))
def f(x):
    return eval(ecuacion)
fa = f(a)
fb = f(b)
print("\nPrimer análisis para visualizar cambio de signo:")
print(f"f({a}) = {fa}")
print(f"f({b}) = {fb}") 
if fa * fb > 0:
    print("\nError: No hay cambio de signo entre 'a' y 'b'")
    print("El método matemáticamente no puede continuar")
else:
    print(f"\n{'Iter':^6} | {'a':^10} | {'b':^10} | {'c':^10} | {'f(c)':^10} | {'Err Abs':^10} | {'Err %':^10}")
    i = 1 
    c_anterior = 0
    historial_iteraciones = []
    historial_error_abs = []
    historial_error_porc = []
    while True:
        c = (a + b) / 2
        fc = f(c)
        if i > 1:
            error_abs = abs(a - b)
            if c != 0: 
                error_porc = abs((c - c_anterior) / c) * 100
            else:
                error_porc = 100
            str_error_abs = f"{error_abs:.6f}"
            str_error_porc = f"{error_porc:.4f}%"
            historial_iteraciones.append(i)
            historial_error_abs.append(error_abs)
            historial_error_porc.append(error_porc)
        else:
            error_abs = 100
            error_porc = 100
            str_error_abs = "---"
            str_error_porc = "---"
        print(f"{i:^6} | {a:^10.4f} | {b:^10.4f} | {c:^10.4f} | {fc:^10.4f} | {str_error_abs:^10} | {str_error_porc:^10}")
        if i > 1 and error_porc < tol:
            print("-" * 75)
            print(f"La raíz se encontró en la iteración {i}: {c:.6f}")
            break 
        if i >= 100:
            print("Por si el algoritmo no converge")
            break
        if fa * fc < 0: 
            b = c
        else:
            a = c
            fa = fc   
        c_anterior = c
        i += 1
    # Parte de la grafica
    if len(historial_iteraciones) > 0:
        plt.figure(figsize=(8, 5))
        # Línea azul para el error absoluto
        plt.plot(historial_iteraciones, historial_error_abs, marker='o', color='blue', label='Error Absoluto', linewidth=2)
        # Línea naranja para el error porcentual
        plt.plot(historial_iteraciones, historial_error_porc, marker='s', color='orange', label='Error Porcentual (%)', linewidth=2)
        plt.title("Gráfica de Convergencia: Caída del Error")
        plt.xlabel("Número de Iteración")
        plt.ylabel("Magnitud del Error")
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        # Mostramos la ventana
        plt.show()
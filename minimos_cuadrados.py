#!/usr/bin/env python3
# -------------- variables globales
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from math import sqrt
list_n = []
list_y = []
list_x = []
list_produc = []
list_x__2 = []
list_y__2 = []
n = int(input("dame el numero total de datos: "))

print("\n[+] Programa para sacar maximos cuadrados en laboratorio ")
print("\n[+]uwu")

# ----------- funciones

def y_bucle():
    for i in range(n):

        numero = i+1
        list_n.append(numero)
        y = float(input(f"\n[+]dato numero {numero} de y: "))
        list_y.append(y)
    print(f"y son {list_y}")

def x_bucle():
    x_range = float(input("dame el rango maximo de x: "))

    res_x = float(input("dame la disminucion constante del rango x: "))

    for x in range(n):
        list_x.append(x_range)
        x_range -= res_x

    print(f"[+]rango {list_x}")


# --------------- comprobaciones

x_bucle()
conformidad_x = str(input("estas conforme con el rango acordado: "))

if conformidad_x in ['si','s','yes','y']:
    print("\n [+] Sigamos adelante")
else:
    x_bucle()



y_bucle()

conformidad_y = str(input("estas de acuerdo con los datos que ingresaste: "))

if conformidad_y in ['si','s','yes','y']:
    print("\n [+] Sigamos adelante")
else:
    y_bucle()


# --------------- tablas

tabla = PrettyTable()
tabla.field_names = ["numero", 'x', 'y']

for i, x, y in zip (list_n, list_x, list_y):
    tabla.add_row([i, x, y])
print(tabla)


# --------------------- grafica

plt.scatter(list_x, list_y, s=100, c =list_y, cmap = 'plasma', alpha = 0.7)

plt.title("Primer grafico")
plt.xlabel("angulo")
plt.ylabel("distancia")

plt.colorbar()
plt.show()








# ------------- m y b


for x, y in zip (list_x, list_y):
    produc = x*y
    list_produc.append(produc)

for x in (list_x):
    x_2 = x ** 2
    list_x__2.append(x_2)

for y in (list_y):
    y_2 = y ** 2
    list_y__2.append(y_2)


sum_y__2 = sum(list_y__2)
sum_x__2= sum(list_x__2)
sum_x_y = sum(list_produc)
sum_x = sum(list_x)
sum_y = sum(list_y)

#numerador_m = ((n*sum_x_y)-((sum_x * sum_y)))
#denominador_m = ((n*sum_x__2)-(sum_x**2))
#m = numerador_m / denominador_m

#numerador_b = (sum_y * sum_x__2) - (sum_x * sum_x_y)
#denominador_b = (n * sum_x__2) - (sum_x ** 2)
#b = numerador_b / denominador_b

#print(f"[+]el valor de b es {b}")
#print(f"[+]el valor de m es {m}")

#---------- correlacion lineal

#numerador_corr = (n * sum_x_y)-(sum_x * sum_y)
#denominador_corr = ( (sqrt(n * sum_x__2) - (sum_x * sum_x))   *   (sqrt(n * sum_x__2)-(sum_y * sum_y)) )
#corr_lineal = numerador_corr / denominador_corr
"""#
"""#e_b = sqrt(((sum_x__2)/((n* sum_x__2)-(sum_x * sum_x)) * ((b ** 2) / n - 2))
           #print(e_m)
           #print(e_b)
# Calcular m
numerador_m = (n * sum_x_y) - (sum_x * sum_y)
denominador_m = (n * sum_x__2) - (sum_x ** 2)

if denominador_m != 0:  # AsegÃºrate de que el denominador no sea cero
    m = numerador_m / denominador_m
    print(f"[+] El valor de m es {m}")
else:
    print("Error: El denominador para calcular m es cero.")

# Calcular b
numerador_b = (sum_y * sum_x__2) - (sum_x * sum_x_y)
denominador_b = (n * sum_x__2) - (sum_x ** 2)

if denominador_b != 0:  # AsegÃºrate de que el denominador no sea cero
    b = numerador_b / denominador_b
    print(f"[+] El valor de b es {b}")
else:
    print("Error: El denominador para calcular b es cero.")

# ---------- CorrelaciÃ³n lineal
numerador_corr = (n * sum_x_y) - (sum_x * sum_y)
denominador_corr = sqrt((n * sum_x__2 - sum_x ** 2) * (n * sum_y__2 - sum_y ** 2))

if denominador_corr != 0:  # AsegÃºrate de que el denominador no sea cero
    corr_lineal = numerador_corr / denominador_corr
    print(f"[+] El valor de la correlaciÃ³n lineal es {corr_lineal}")
else:
    print("Error: El denominador para la correlaciÃ³n lineal es cero.")

# --------------- e

# CÃ¡lculo de e_m y e_b
if (n * sum_x__2) - (sum_x ** 2) > 0:  # Verifica que el denominador no sea negativo
    e_m = sqrt((n / (n * sum_x__2 - sum_x ** 2)) * ((b ** 2) / n))
    print(f"DesviaciÃ³n estÃ¡ndar del estimador m: {e_m}")
else:
    print("Error: La expresiÃ³n para e_m es invÃ¡lida.")

if (n * sum_x__2) - (sum_x ** 2) > 0:  # Verifica que el denominador no sea negativo
    e_b = sqrt((sum_x__2 / ((n * sum_x__2) - (sum_x ** 2))) * ((b ** 2) / n))
    print(f"DesviaciÃ³n estÃ¡ndar del estimador b: {e_b}")
else:
    print("Error: La expresiÃ³n para e_b es invÃ¡lida.")

# g = 2*h/t**2

print("***********************************************************************")
print("***********************************************************************")
print("[+]programa para calcular la gravedad 'UWU'")
print("***********************************************************************")
print("***********************************************************************")

list_h = []
list_t = []
list_g = []
list_num_exp = []
num_rep_expe = int(input("Cuantas veces se repetira el experimento: "))
max_h = float(.485)
round(max_h, 3)
for i in range(num_rep_expe):
    max_h -= .015
    round(max_h, 3)
    list_h.append(max_h)
print(f"Lista de alturas: {list_h}")

for i in range(num_rep_expe):
#   h_exp = float(input(f"[{i+1}] De que altura fue lanzada (m): "))
#   list_h.append(h_exp)
    t_exp = float(input(f"[{i+1}] cual fue el tiempo que tardo en caer (s): "))
    list_t.append(t_exp)
    num_exp = i+1
    list_num_exp.append(num_exp)

print(f"Lista del tiempo ingresado: {list_t}")

for h, t, i in zip (list_h, list_t, list_num_exp):
    num_g = 2*h/t**2
    print(f"[{i}] Gravedad calculada: {num_g}")
    list_g.append(num_g)
#print(f"Lista de gravedades calculadas: {list_g}")

print(f"La gravedad en promedio es: {(sum(list_g)/num_rep_expe)}")

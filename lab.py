from prettytable import PrettyTable
import matplotlib.pyplot as plt
from math import sqrt

class Experimento():

    def __init__(self, experimento = None, num_Mediciones = 0, y_list = [], x_list = [], n_list = [] ):
        self.experimento = experimento
        self.y_list = y_list
        self.x_list = x_list
        self.num_Mediciones = num_Mediciones
        self.n_list = n_list

    @staticmethod
    def inicio():
        mensaje = """
        Bienvenido a LabTex, tu ayudante para crear reportes de laboratorio de la UPIICSA.
        Por favor, elige el experimento deseado:

        a) CaÃ­da libre
        b) PÃ©ndulo
        c) MRU
        d) Tiro parabÃ³lico
        """
        return mensaje

    @classmethod
    def tip_Experimento(cls):
        while True:
            experimento = input("Elige el experimento: ").strip().lower()  # Convertimos a minÃºsculas para evitar errores
            if experimento in ["a", "b", "c", "d"]:
                print(f"\nÂ¡Se ha registrado el experimento deseado correctamente!")
                return experimento
            else:
                print("\nEntrada no vÃ¡lida. Por favor, intenta de nuevo.")
    @staticmethod
    def Presentacion_Experimento():
        raise NotImplementedError("No se eligio el experimento correctamente")

    def list_y_x(self):
        num_Mediciones = int(input("Â¿CuÃ¡ntas mediciones en el experimento realizaron?: "))


        def generar_x():
            x_list = []

            n_list = []

            for i in range(num_Mediciones):
                numero =  i + 1
                x = float(input(f"\n[+] Dato nÃºmero {numero} de X: "))
                x_list.append(x)
            return x_list



        def generar_y():
            y_list = []
            y_range = float(input("\nDame el rango minimo de Y: "))
            res_y = float(input("Dame la adicion constante del rango Y: "))
            for _ in range(num_Mediciones):
                y_list.append(y_range)
                y_range += res_y
            return y_list


        while True:
            y_list = generar_y()
            print(f"\nValores de Y: {y_list}")
            conformidad_y = input("Â¿EstÃ¡s de acuerdo con los valores de Y? (s/si/yes): ").strip().lower()
            if conformidad_y in ["s", "si", "yes", "y"]:
                print("\n[+] Valores de Y registrados con Ã©xito.")
                break
            else:
                print("\n[!] Generando nuevos valores para Y...")


        while True:
            x_list = generar_x()
            print(f"\nValores de X: {x_list}")
            conformidad_x = input("Â¿EstÃ¡s de acuerdo con los valores de X? (s/si/yes): ").strip().lower()
            if conformidad_x in ["s", "si", "yes", "y"]:
                print("\n[+] Valores de X registrados con Ã©xito.")
                break
            else:
                print("\n[!] Generando nuevos valores para X...")
        self.x_list = x_list
        self.y_list = y_list
        self.n_list = list(range(1, num_Mediciones + 1))

        return y_list, x_list

    def grafic_table_1(self):
        tabla = PrettyTable()
        tabla.field_names = ["numero", 'x', 'y']

        for i, x, y in zip (self.n_list, self.x_list, self.y_list):
            tabla.add_row([i, x, y])
        print(tabla)

        plt.scatter(self.x_list, self.y_list, s=100, c =self.y_list, cmap = 'plasma', alpha = 0.7)

        plt.title("Primer grafico")
        plt.xlabel("angulo")
        plt.ylabel("distancia")

        plt.colorbar()
        plt.show()

    def m_b_c_l(self):

        list_produc = []
        list_x__2 = []
        list_y__2 = []

        for x, y in zip(self.x_list, self.y_list):
            produc = x * y
            list_produc.append(produc)

        for x in self.x_list:
            x_2 = x ** 2
            list_x__2.append(x_2)

        for y in self.y_list:
            y_2 = y ** 2
            list_y__2.append(y_2)

        sum_y__2 = sum(list_y__2)
        sum_x__2 = sum(list_x__2)
        sum_x_y = sum(list_produc)
        sum_x = sum(self.x_list)
        sum_y = sum(self.y_list)

        numerador_m = (self.num_Mediciones * sum_x_y) - (sum_x * sum_y)
        denominador_m = (self.num_Mediciones * sum_x__2) - (sum_x ** 2)

        if denominador_m != 0:  # AsegÃºrate de que el denominador no sea cero
            m = numerador_m / denominador_m
            print(f"[+] El valor de m es {m}")
        else:
            print("Error: El denominador para calcular m es cero.")

        numerador_b = (sum_y * sum_x__2) - (sum_x * sum_x_y)
        denominador_b = (self.num_Mediciones * sum_x__2) - (sum_x ** 2)

        if denominador_b != 0:  # AsegÃºrate de que el denominador no sea cero
            b = numerador_b / denominador_b
            print(f"[+] El valor de b es {b}")
        else:
            print("Error: El denominador para calcular b es cero.")

        numerador_corr = (self.num_Mediciones * sum_x_y) - (sum_x * sum_y)
        denominador_corr = sqrt((self.num_Mediciones * sum_x__2 - sum_x ** 2) * (self.num_Mediciones * sum_y__2 - sum_y ** 2))

        if denominador_corr != 0:  # AsegÃºrate de que el denominador no sea cero
            corr_lineal = numerador_corr / denominador_corr
            print(f"[+] El valor de la correlaciÃ³n lineal es {corr_lineal}")
        else:
            print("Error: El denominador para la correlaciÃ³n lineal es cero.")

        if (self.num_Mediciones * sum_x__2) - (sum_x ** 2) > 0:  # Verifica que el denominador no sea negativo
            e_m = sqrt((self.num_Mediciones / (self.num_Mediciones * sum_x__2 - sum_x ** 2)) * ((b ** 2) / self.num_Mediciones))
            print(f"DesviaciÃ³n estÃ¡ndar del estimador m: {e_m}")
        else:
            print("Error: La expresiÃ³n para e_m es invÃ¡lida.")

        if (self.num_Mediciones * sum_x__2) - (sum_x ** 2) > 0:  # Verifica que el denominador no sea negativo
            e_b = sqrt((sum_x__2 / ((self.num_Mediciones * sum_x__2) - (sum_x ** 2))) * ((b ** 2) / self.num_Mediciones))
            print(f"DesviaciÃ³n estÃ¡ndar del estimador b: {e_b}")
        else:
            print("Error: La expresiÃ³n para e_b es invÃ¡lida.")


        x2_list = []
        y2_list = []

        x2_list = self.x_list
        y2_list = self.y_list

        xm = []
        ym = []
        for i in range(-1,1):
            xm.append(i)
            ym.append(i)
        plt.plot(xm, ym, label = "segunda grafica", color = "blue")
        plt.title("grafica con correcion de m y b")
        plt.xlabel("Valores de X")
        plt.ylabel("Valores de Y")
        plt.legend()
        plt.grid()
        plt.show()



class Caida_Libre(Experimento):

    def __init__(self, experimento=None, num_Mediciones=0, y_list=[], x_list=[], n_list=[]):
        super().__init__(experimento, num_Mediciones, y_list, x_list, n_list)
        self.gravedad = 9.81
    @staticmethod
    def Presentacion_Experimento():
            print("""
            Â¡Bienvenido al experimento de CaÃ­da Libre!

            En este experimento, dejamos caer una bola desde una determinada altura y medimos el tiempo
            que tarda en llegar al suelo. Usamos estos dos valores para calcular la aceleraciÃ³n debida a
            la gravedad (g), que indica la fuerza con la que los objetos son atraÃ­dos hacia el centro de
            la Tierra.

            FÃ³rmula para calcular la gravedad (g):

            g = (2 * h) / t^2

            Donde:
                h: Altura desde la que se deja caer el objeto (en metros).
                t: Tiempo que tarda el objeto en llegar al suelo (en segundos).

            A continuaciÃ³n, se muestra una representaciÃ³n visual del experimento:

            """)

            # Crear una "caÃ­da libre" con puntos y lÃ­neas (usando caracteres ASCII)
            print("""
                            *
                        .o.
                        .o O o.
                    .o O   O  o.
                .o O   O       O  o.
            ---------------/----------------
                | Altura (h)      | Tiempo (t)|
            """)

            print("""
            En la grÃ¡fica anterior, el objeto (representado por los asteriscos y puntos) se deja caer desde
            una altura determinada y recorre la distancia hacia el suelo con una aceleraciÃ³n constante, que
            es la gravedad (g). Cuanto mÃ¡s alta sea la caÃ­da (h), mayor serÃ¡ el tiempo que tarda en llegar
            al suelo (t), y viceversa.

            Puedes pensar en este experimento como una representaciÃ³n de cÃ³mo la gravedad influye en la velocidad
            con la que caen los objetos.

            """)


    def gravedad():
        list_gravedad = []
        list_tiempo = []
        list_altura = []

        list_tiempo = self.x_list
        list_altura = self.y_list

        for h, t, i in zip (list_altura, list_tiempo, list_gravedad):
            num_g = 2*h/t**2
            print(f"[{i}] Gravedad calculada: {num_g} m/sÂ²")
            list_gravedad.append(num_g)
        print(f"La gravedad en promedio es : {(sum(list_g))/self.num_Mediciones} m/sÂ²")



class Choque_Unidimensional(Experimento):
    pass
end_Experiment = Caida_Libre()
print(end_Experiment.inicio())
end_Experiment.tip_Experimento()
end_Experiment.Presentacion_Experimento
end_Experiment.list_y_x()
end_Experiment.grafic_table_1()
end_Experiment.m_b_c_l()
end_Experiment.gravedad

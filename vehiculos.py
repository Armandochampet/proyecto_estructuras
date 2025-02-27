from Nodo import nodo
class Vehiculo:
    def __init__(self, placa, marca, modelo, year, kilometraje): #usamos year porque la ñ me daba problema
        self.set_placa(placa)
        self.marca = marca
        self.modelo = modelo
        self.set_year(year)
        self.set_kil(kilometraje)
        self.historial_mantenimientos = None

    # Getter y Setter para la placa
    def get_placa(self):
        return self.placa

    def set_placa(self, nueva_placa):
        if isinstance(nueva_placa, str) and len(nueva_placa) > 4:
            self.placa = nueva_placa
        else:
            print("Error: Placa inválida.")


    def get_year(self):
        return self.year

    def set_year(self, new_year):
        if 1900 <= new_year <= 2025:
            self.year = new_year
        else:
            print("Error: Año inválido.")

    def get_kil(self):
        return self.kil

    def set_kil(self, nuevo_km):
        if nuevo_km >= 0:
            self.kil = nuevo_km
        else:
            print("Error: ingrese un valor mayor a 0")

    def agregar_mantenimiento(self, mantenimiento):
        nuevo_nodo = nodo(mantenimiento)
        if self.historial_mantenimientos is None:
            self.historial_mantenimientos = nuevo_nodo
        else:
            actual = self.historial_mantenimientos
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_mantenimientos(self):
        actual = self.historial_mantenimientos
        if not actual:
            print("No hay mantenimientos registrados.")
            return

        print(f"Historial de mantenimientos para {self.placa}:")
        while actual:
            m = actual.dato
            print(f"Fecha: {m.get_fecha()}, Descripción: {m.get_descripcion()}, Costo: {m.get_costo()}")
            actual = actual.siguiente


    def calcular_costo_total(self):
        total = 0
        actual = self.historial_mantenimientos
        while actual:
            total += actual.dato.get_costo()
            actual = actual.siguiente
        return total

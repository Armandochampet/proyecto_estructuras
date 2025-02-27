from Nodo import nodo
class FlotaVehiculos:
    def __init__(self):
        self.inicio = None

    def agregar_vehiculo(self, vehiculo):
        nuevo_nodo = nodo(vehiculo)
        if self.inicio is None:
            self.inicio = nuevo_nodo
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_vehiculo(self, placa):
        actual = self.inicio
        anterior = None

        while actual:
            if actual.dato.get_placa() == placa:
                if anterior is None:
                    self.inicio = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                print(f"Vehículo con placa {placa} eliminado.")
                return
            anterior = actual
            actual = actual.siguiente

        print("Vehículo no encontrado.")

    def buscar_vehiculo(self, placa):
        actual = self.inicio
        while actual:
            if actual.dato.get_placa() == placa:
                v = actual.dato
                print(f"Vehículo encontrado: {v.get_placa()} - {v.marca} {v.modelo}, Año: {v.get_year()}, KM: {v.get_kil()}")
                return v
            actual = actual.siguiente

        print("Vehículo no encontrado.")
        return None

    def listar_vehiculos(self):
        actual = self.inicio
        if not actual:
            print("No hay vehículos registrados.")
            return

        print("Lista de vehículos:")
        while actual:
            v = actual.dato
            print(f"Placa: {v.get_placa()}, Marca: {v.marca}, Modelo: {v.modelo}, Año: {v.get_year()}, KM: {v.get_kil()}")
            actual = actual.siguiente
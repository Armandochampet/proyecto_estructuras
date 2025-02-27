from flota import FlotaVehiculos
from vehiculos import Vehiculo
def main():
    flotilla = FlotaVehiculos()

    while True:
        print("\n bienvenido al menu")
        print("------------------------------------------------------")
        print("1. Agregar un vehículo")
        print("2. Eliminar un vehículo")
        print("3. Buscar un vehículo")
        print("4. Listar todos los vehículos")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_carro(flotilla)
        elif opcion == "2":
            eliminar_carro(flotilla)
        elif opcion == "3":
            buscar_carro(flotilla)
        elif opcion == "4":
            flotilla.listar_vehiculos()
        elif opcion == "5":
            print("gracias por utlizar mi programa de flota")
            break
        else:
            print(" Opción no válida")

def agregar_carro(flotilla):
    placa = input("Ingrese la placa del vehículo: ")
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")

    while True:  # Validamos que el año sea correcto
        try:
            year = int(input("Ingrese el año del vehículo: "))
            if 1900 <= year <= 2025:
                break
            else:
                print(" Año inválido.")
        except ValueError:
            print("Ingrese un número válido")

    while True:
        try:
            kilometraje = int(input("Ingrese el kilometraje del vehículo: "))
            if kilometraje >= 0:
                break
            else:
                print(" El kilometraje no puede ser negativo.")
        except ValueError:
            print("Ingrese un número válido para el kilometraje.")
    vehiculo = Vehiculo(placa, marca, modelo, year, kilometraje)
    flotilla.agregar_vehiculo(vehiculo)
    print("Vehículo agregado con éxito")

def eliminar_carro(flotilla):
    placa = input("Ingrese la placa del vehículo a eliminar: ")
    flotilla.eliminar_vehiculo(placa)

def buscar_carro(flotilla):
    placa = input("Ingrese la placa del vehículo a buscar: ")
    flotilla.buscar_vehiculo(placa)

main()


class Mantenimiento:
    def __init__(self, fecha, descripcion, costo): #se crea para los datos del mantenimiento
        self.fecha = fecha
        self.descripcion = descripcion
        self.set_costo(costo)

    def get_fecha(self): #se pide la fecha
        return self.fecha

    def set_fecha(self, nueva_fecha):#nodifica la fehca
        self.fecha = nueva_fecha

    def get_descripcion(self): #pide descripcion
        return self.descripcion

    def set_descripcion(self, nueva_descripcion): #modifica descripcion
        self.descripcion = nueva_descripcion

    def get_costo(self): #pide costo
        return self.costo

    def set_costo(self, nuevo_costo): #modifica costo
        if nuevo_costo >= 0:
            self.costo = nuevo_costo
        else:
            print("Error: ingrese un valor mayor a 0.")
            self.costo = 0



print("ProgAplicada - Actividad 2")
print("POO Herencia y encapsulamiento... Horwell Murillo V")
print("Cada clase tiene sus pruebas, descomente cada seccion y ejecute para comprobar!")
print("")
print("--------------------------------------------------------------------------------")


#---------------------------------------------------------------------------------------------------
#definicion SuperClase
class MediosTransporte():
    def __init__(self, marca, modelo, color):
        self.marca=marca
        self.modelo=modelo
        self.color=color

        self.encendido=False
        self.acelerando=False
        self.frenando=True
    
    def encender(self):
        self.encendido=True
        print("Motor encendido..")
    
    def apagar(self):
        self.encendido=False
        self.acelerando=False
        print("Motor apagado..")
    
    def acelerar(self):
        self.encendido=True
        self.acelerando=True
        print("Acelerando...")
            
    def desacelerar(self):
        self.acelerando=False
        print("frenando...")
    
    def __str__(self):
        print("SuperClase Transportes Marca {}, modelo {}, color {} Valores: {},{},{} ".format(self.marca, self.modelo, self.color, self.encendido, self.acelerando,self.frenando))
    
    def __del__(self):
        print("Objeto MediosTrasnporte eliminado en memoria..")

#---------------------------------------------------------------------------------------------------
#Test de Super Clase
'''
vehiculo1=MediosTransporte("BMW","CBR","Azul")

vehiculo1.__str__()
vehiculo1.encender()
vehiculo1.acelerar()
vehiculo1.desacelerar()
vehiculo1.apagar()
'''

#---------------------------------------------------------------------------------------------------
#definicion clase hija MediosTerrestres hereda de MediosTransporte
class MediosTerrestres(MediosTransporte):
    def __init__(self, marca, modelo, color, ruedas, capacidad, tipoMarcha):
        super().__init__(marca, modelo, color)

        self.ruedas=ruedas
        self.capacidad=capacidad
        self.tipoMarcha=tipoMarcha

    def puntoMuerto(self):
        print("En punto muerto")
    
    def cargarCombustible(self):
        print("Cargar combustible")
    
    def cambiarMarcha(self):
        print("Cambiando marcha")
    
    def __del__(self):
        print("Objeto transporteTerrestre eliminado de memoria")
    
#---------------------------------------------------------------------------------------------------
#Test de clase terrestre
'''
terrestre1=MediosTerrestres("Volvo", "Scania", "Blanco", 16, "15-Toneladas","CajaManual")
terrestre1.__str__()
terrestre1.encender()
terrestre1.acelerar()
terrestre1.desacelerar()
terrestre1.apagar()
terrestre1.cambiarMarcha()
terrestre1.cargarCombustible()
terrestre1.puntoMuerto()
'''
    
#---------------------------------------------------------------------------------------------------
#definicion clase hija Auto hereda de MediosTransporte y MediosTerrestres
class Auto(MediosTerrestres):
    def __init__(self, marca, modelo, color, ruedas, capacidad, tipoMarcha, capacidadBaul):
        super().__init__(marca, modelo, color, ruedas, capacidad, tipoMarcha) #Esto evita declarar todos los atributos traidos ya de la clase Padre
        self._capacidadBaul=capacidadBaul #Propiedad privada con _guionBajo para darle encapsulamiento
    
    def __str__(self):
        print("Clase Auto Marca {}, modelo {}, color {} ruedas:{}, capacidad: {}, tipo de marcha: {} y capacidadBaul:{}.".format(
            self.marca, 
            self.modelo, 
            self.color, 
            self.ruedas, 
            self.capacidad,
            self.tipoMarcha,
            self._capacidadBaul))

    def cargarBaul(self):
        pass #esto toma el metodo sin necesidd de desarrollarlo

    def vaciarBaul(self):
        print("Baul vacio")
    
    #metodo get para obtener _capacidadBaul
    def getCapacidadBaul(self):
        return self._capacidadBaul

    #Metodo Setter para cambiar _capacidadBaul
    def setCapacidadBaul(self, nuevaCapacidad):
        self._capacidadBaul=nuevaCapacidad
    
    #Metodo Destructor de la clase Auto
    def __del__(self):
        print("Objeto Auto eliminado de memoria.")

#---------------------------------------------------------------------------------------------------
#Test de clase Auto
'''
auto1=Auto("Ferrary","LaFerrary","Rojo",4,"Dos personas","Secuencial","500 kg")

auto1.__str__()
auto1.cambiarMarcha()
print(auto1._capacidadBaul)
auto1.setCapacidadBaul("100 kg") #seteamos capacidad baul
print(auto1.getCapacidadBaul()) #Obtenemos capacidad baul
'''

#---------------------------------------------------------------------------------------------------

#definicion clase hija moto hereda de MediosTransporte y MediosTerrestres
class Moto(MediosTerrestres):
    def __init__(self, marca, modelo, color, ruedas, capacidad, tipoMarcha, cilindrada):
        super().__init__(marca, modelo, color, ruedas, capacidad, tipoMarcha)
        self._cilindrada=cilindrada
    
    #Metodo get para obtener _cilindrada como atributo privado
    #@property
    def getCilindrada(self):
        return self._cilindrada
    
    #Metodo setter para cambiar _cilindrada como atributo privado
    #@_cilindrada.setter
    def setCilindrada(self, nuevaCilindrada):
        self._cilindrada=nuevaCilindrada
    
    def __str__(self):
        print("Clase Moto Marca {}, modelo {}, color {} ruedas:{}, capacidad: {}, tipo de marcha: {} y Cilindrada. {}.".format(
            self.marca, 
            self.modelo, 
            self.color, 
            self.ruedas, 
            self.capacidad,
            self.tipoMarcha,
            self._cilindrada))
    
    def __del__(self):
        print("Objeto Moto eliminado de memoria")
    
#---------------------------------------------------------------------------------------------------
#Test para clase Moto
'''
moto1=Moto("Ducati","Monster","Negro",2,"dos personas","6 velocidades","1.000cc")
moto1.__str__()
print(moto1.getCilindrada())
moto1.setCilindrada("999cc")
print(moto1.getCilindrada())
'''
#---------------------------------------------------------------------------------------------------

        
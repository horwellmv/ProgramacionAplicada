# ProgramacionAplicada
Repo para subir los tps y codigo ejercitado en la catedra de ProgramacionAplicada 2do año de Analisis de sistemas. IFTS 18-02

##Uso de los decoradores @property y @_miAtributo.setter

Fuente:https://ellibrodepython.com/
el decorador @property, que viene por defecto con Python, y puede ser usado para modificar un método para que sea un atributo o propiedad. Es importante que conozcan antes la programación orientada a objetos.

El decorador puede ser usado sobre un método, que hará que actúe como si fuera un atributo.

class Clase:
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        return self.__mi_atributo
Como si de un atributo normal se tratase, podemos acceder a el con el objeto . y nombre.

mi_clase = Clase("valor_atributo")
mi_clase.mi_atributo
# 'valor_atributo'
Muy importante notar que aunque mi_atributo pueda parecer un método, en realidad no lo es, por lo que no puede ser llamado con ().

# mi_clase.mi_atributo() # Error! Es un atributo, no un método
Tal vez te preguntes para que sirve esto, ya que el siguiente código hace exactamente lo mismo sin hacer uso de decoradores.

class Clase:
    def __init__(self, mi_atributo):
        self.mi_atributo = mi_atributo

mi_clase = Clase("valor_atributo")
mi_clase.mi_atributo
# 'valor_atributo'
Bien, la explicación no es sencilla, pero está relacionada con el concepto de encapsulación de la programación orientada a objetos. 
Este concepto nos indica que en determinadas ocasiones es importante ocultar el estado interno de los objetos al exterior, 
para evitar que sean modificados de manera incorrecta. Para la gente que venga del mundo de Java, esto no será nada nuevo, y está muy relacionado 
con los métodos set()y get() que veremos a continuación.

La primera diferencia que vemos entre los códigos anteriores es el uso de __ antes de mi_atributo. 
Cuando nombramos una variable de esta manera, es una forma de decirle a Python que queremos que se “oculte” 
y que no pueda ser accedida como el resto de atributos.

class Clase:
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

mi_clase = Clase("valor_atributo")

# mi_clase.__mi_atributo # Error!
Esto puede ser importante con ciertas variables que no queremos que sean accesibles desde el exterior de una manera no controlada. 
Al definir la propiedad con @property el acceso a ese atributo se realiza a través de una función, siendo por lo tanto un acceso controlado.

class Clase:
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        # El acceso se realiza a través de este "método" y
        # podría contener código extra y no un simple retorno
        return self.__mi_atributo
Otra utilidad podría ser la consulta de un parámetro que requiera de muchos cálculos. 
Se podría tener un atributo que no estuviera directamente almacenado en la clase, sino que precisara de realizar ciertos cálculos.
Para optimizar esto, se podrían hacer los cálculos sólo cuando el atributo es consultado.

Por último, existen varios añadidos al decorador @property como pueden ser el setter. 
Se trata de otro decorador que permite definir un “método” que modifica el contenido del atributo que se esté usando.

class Clase:
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        return self.__mi_atributo

    @mi_atributo.setter
    def mi_atributo(self, valor):
        if valor != "":
            print("Modificando el valor")
            self.__mi_atributo = valor
        else:
            print("Error está vacío")
De esta forma podemos añadir código al setter, haciendo que por ejemplo realice comprobaciones antes de modificar el valor. 
Esto es una cosa que de usar un atributo normal no podríamos hacer, y es muy útil de cara a la encapsulación.

mi_clase = Clase("valor_atributo")
mi_clase.mi_atributo
# 'valor_atributo'

mi_clase.mi_atributo = "nuevo_valor"
mi_clase.mi_atributo
# 'nuevo_valor'

mi_clase.mi_atributo = ""
# Error está vacío
Resulta lógico pensar que si un determinado atributo pertenece a una clase, 
si queremos modificarlo debería de tener la “aprobación” de la clase, para asegurarse que ninguna entidad externa está “haciendo cosas raras”.

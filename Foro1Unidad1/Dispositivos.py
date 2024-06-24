class Device:
    def __init__(self, marca, modelo, numero_serial): #Encapsulación
        self.__numero_serial = numero_serial  #Atributo privado
        self._marca = marca  #Atributo protegido
        self._modelo = modelo  #Atributo protegido
        self._esta_encendido = False  #Atributo protegido
        self.capacidad = "Tengo capacidad de computo"  #Atributo público

    def encender(self):
        self._esta_encendido = True
        print(f"{self._marca} {self._modelo} está ahora ENCENDIDO.")

    def apagar(self):
        self._esta_encendido = False
        print(f"{self._marca} {self._modelo} está ahora APAGADO.")

    def mostrar_info(self): #Abstracción
        raise NotImplementedError("Las subclases deben implementar este método.")  

    def obtener_numero_serial(self):  #Método público para acceder al atributo privado
        return self.__numero_serial

class Laptop(Device):  #Herencia
    def __init__(self, marca, modelo, color, numero_serial):
        super().__init__(marca, modelo, numero_serial)
        self.color = color  #Atributo público

    def mostrar_info(self):  #Polimorfismo
        print(f"Laptop: {self._marca} {self._modelo}, Color: {self.color}, Número Serial: {self.obtener_numero_serial()}, {self.capacidad}")

class Smartphone(Device):  #Herencia
    def __init__(self, marca, modelo, sistema_operativo, numero_serial):
        super().__init__(marca, modelo, numero_serial)
        self.sistema_operativo = sistema_operativo  #Atributo público

    def mostrar_info(self):  #Polimorfismo
        print(f"Smartphone: {self._marca} {self._modelo}, Sistema Operativo: {self.sistema_operativo}, Número Serial: {self.obtener_numero_serial()}, {self.capacidad}")

#Agregar datos a las clases derivadas
laptop = Laptop("Asus", "TufGaming", "Negro", "12345-67890")
smartphone = Smartphone("Samsung", "Galaxy S24", "Android", "09876-54321")

# Usar métodos de las clases
laptop.mostrar_info()
laptop.encender()

smartphone.mostrar_info()
smartphone.encender()

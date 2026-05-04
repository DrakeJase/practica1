class Persona:
    def __init__(self, nombre, edad, altura, peso, ciudad):
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura
        self.__peso = peso
        self.__ciudad = ciudad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad
    
    def get_altura(self):
        return self.__altura
    
    def get_peso(self):
        return self.__peso

    def get_ciudad(self):
        return self.__ciudad

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_altura(self, altura):
        self.__altura = altura

    def set_peso(self, peso):
        self.__peso = peso

    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad


# Metodos 

    def calcular_imc(self):
        return self._peso / (self._altura ** 2)

    def es_mayor_edad(self):
        return self.__edad >= 18

    def info(self):
        return f"Nombre: {self._nombre}, Edad: {self.edad}, Ciudad: {self._ciudad}"
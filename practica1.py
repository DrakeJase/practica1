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
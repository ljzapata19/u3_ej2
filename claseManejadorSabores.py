import csv
from claseSabor import Sabor
class ManejaSabores:
    __sabores = list()
    
    def __init__(self):
        self.__sabores=[]
    
    def agregarSabor(self,unSabor):
        self.__sabores.append(unSabor)
    
    def testManejadorSabores(self):
        archivo = open('sabores.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            self.agregarSabor(Sabor(int(fila[0]), fila[1], fila[2]))
        archivo.close()
    
    def seleccionarSabor(self, cod):
        return self.__sabores[cod-1]
    
    def getSabores(self):
        return self.__sabores
class Sabor:
    __idSabor=0
    __ingredientes=''
    __nombreSabor=''
    
    def __init__(self, ids, ing, nom):
        self.__idSabor = ids
        self.__ingredientes = ing
        self.__nombreSabor = nom
    
    def getIdSabor(self):
        return self.__idSabor
    
    def getNombre(self):
        return self.__nombreSabor
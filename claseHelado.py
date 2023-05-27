class Helado:
    __gramos: int()
    __precio: float()
    __sabores: list()
    
    def __init__(self, gr, pr):
        self.__gramos = gr
        self.__precio = pr
        self.__sabores = []
    
    def getSabores(self):
        return self.__sabores
    
    def getGramos(self):
        return self.__gramos
    
    def getPrecio(self):
        return self.__precio
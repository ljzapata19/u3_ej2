from claseHelado import Helado
import numpy as np

class ManejaHelados:
    __helados = list()

    def __init__(self):
        self.__helados = []

    def agregarHelado(self, unHelado):
        self.__helados.append(unHelado)

    def addHelado(self, listaSabores):
        gramos = int(input('Ingresar gramos: '))
        precio = float(input('Ingresar precio: '))
        unHelado = Helado(gramos, precio)
        i = 0
        cod = int(input('Ingresar codigo del sabor a agregar (finaliza con 0): '))
        while i < 4 and cod != 0:
            if cod-1 < len(listaSabores.getSabores()):
                unHelado.getSabores().append(listaSabores.seleccionarSabor(cod))
                i += 1
                print('Sabor agregado')
            else:
                print('Sabor erroneo. Por favor ingrese nuevamente')
            if i!=4:
                cod=int(input('Ingresar codigo del sabor a agregar (finaliza con 0): '))
            
        self.agregarHelado(unHelado)

    def masPedidos(self):
        cont_sabores={}
        for helado in self.__helados:
             for sabor in helado.getSabores():
                 if sabor.getNombre() in cont_sabores:
                     cont_sabores[sabor.getNombre()] += 1
                 else:
                     cont_sabores[sabor.getNombre()] = 1
        print(cont_sabores)
        sabores_mas_pedidos = sorted(cont_sabores.items(), key=lambda item: item[1], reverse=True)[:5]
        return sabores_mas_pedidos
    
    def gramosPorSabor(self, sabor_bus):
        cont = 0
        for helado in self.__helados:
            for sabor in helado.getSabores():
                if sabor_bus == sabor.getIdSabor():
                    gramos = float(helado.getGramos()) / float(len(helado.getSabores()))
                    cont = cont + gramos
        return cont
    
    
    def SaboresPorTamaño(self, gramos_bus, sabores):
        cont_gramos = np.zeros(len(sabores))
        band = False
        for helado in self.__helados:
            for sabor in helado.getSabores():
                gramos = float(helado.getGramos()) / float(len(helado.getSabores()))
                cont_gramos[sabor.getIdSabor()-1] += gramos
        
        for i in range (len(cont_gramos)):
            if cont_gramos[i] == gramos_bus:
                print(f'El sabor {sabores[i].getNombre()} tiene {gramos_bus} gr.')
                band = True
        if not band:
            print('No se vendieron helados del tamaño ingresado.')
    def importeTotal(self):
        tipos = np.array([100,150,250,500,1000])
        cont = np.zeros(len(tipos))
        for helado in self.__helados:
            i=0
            while i<len(tipos) and helado.getGramos() != tipos[i]:
                i += 1
            if helado.getGramos() == tipos[i]:
                cont[i] += helado.getPrecio()
        
        for i in range(len(tipos)):
            print(f'El tamaño de {tipos[i]} gr recaudó ${cont[i]}')
            
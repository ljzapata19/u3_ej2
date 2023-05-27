from claseManejadorSabores import ManejaSabores
from claseManejadorHelados import ManejaHelados
class Menu:
    __helados=list()
    __sabores=list()
    
    def __init__(self):
        self.__helados=ManejaHelados()
        self.__sabores=ManejaSabores()
        self.__sabores.testManejadorSabores()
    
    def imprimirOpciones(self):
        print('----------MENÚ----------')
        print('1.     Registrar un helado vendido.')
        print('2.     Mostrar el nombre de los 5 sabores de helado más pedidos.')
        print('3.     Ingresar un número de sabor y estimar el total de gramos vendidos.')
        print('4.     Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño considerando todos los helados vendidos.')
        print('5.     Determinar el importe total recaudado por la Heladería, por cada tipo de helado.')
        opcion=int(input('Ingresar opcion (finaliza con cero): '))
        while opcion != 0:
            self.seleccionarOpcion(opcion)
            opcion=int(input('\nIngresar opcion: '))
        
    
    def seleccionarOpcion(self,op):
        if op == 1:
            self.__helados.addHelado(self.__sabores)
        elif op == 2:
            print("Mostrar los 5 sabores de helado más pedidos")
            Pedidos = self.__helados.masPedidos()
            print("Los 5 sabores de helado más pedidos son:")
            for sabor, contador in Pedidos:
                print(sabor, contador)
        elif op == 3:
            sabor_buscado = int(input('Ingrese el nro de sabor: '))
            gramos = self.__helados.gramosPorSabor(sabor_buscado)
            if gramos != 0:
                print(f'Del sabor {self.__sabores.getSabores()[sabor_buscado-1].getNombre()} se vendió {gramos}gr.')
            else:
                print('No se vendio el sabor ingresado.')
        elif op == 4:
            gramos_buscado = float(input('Ingrese el tamaño del helado: '))
            self.__helados.SaboresPorTamaño(gramos_buscado, self.__sabores.getSabores())
        elif op == 5:
            self.__helados.importeTotal()
        else:
            print('La opcion ingresada es incorrecta.')
        
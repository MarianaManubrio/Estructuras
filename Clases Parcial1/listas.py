from time import sleep
class nodo():
    def __init__(self, valor): #constructor
        self.value = valor
        self.next = None
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next
    def set_value(self, valor):
        self.value = valor
    def set_next (self, siguiente):
        self.next = siguiente #self como parametro para los metodos, las funciones no

class lista():
    def __init__(self):
        self.head=None
    def get_head(self):
        return self.head
    def set_head(self, cabeza):
        self.head = cabeza
    def is_empty(self):
        return self.head == None #from listas import * 
        #nodito = nodo("hamburguesa")
#       >>> nodito.get_value()
#       'hamburguesa'
#       >>> type(nodito.get_value())
#       <class 'str'>
#       >>> 
    def add(self, valor):
        eslabon = nodo(valor) #para que lo haga nodo, objeto
        sleep(0.01)
        eslabon.next = self.head #define el next para que el que tenia el nombre de head no quede sin asignacion
        self.head = eslabon
        #>>> lista1.get_head().get_value()
        #3
        #>>> lista1.get_head().get_next().get_next().get_value()
        #1
        #>>>
    def remove(self):
        self.head = self.head.next
    def __len__(self):
        contador  = 0
        explorador = self.head #empezar desde el ultimo o el inicio
        while explorador != None:
            contador += 1
            explorador = explorador.next
        return contador 
######################################################################
    def __getitem__(self, pos):
        if self.__len__() < pos:
            raise IndexError
        explorador = self.head
        for i in range(pos):
            explorador = explorador.next
        return explorador.value
    def add_last(self, valor):
        eslabon = nodo(valor)
        explorador = self.head
        if explorador == None:
            self.head = eslabon
        else:
            while explorador.next != None:
                
                explorador = explorador.next
            explorador.next = eslabon
            #add last, lista[1] y asi
    def __iter__(self):
        self.posicion = self.head.next
        return self
    def __next__(self): #avanza dentro de iteradores next (iterador)
        if self.posicion !=None: # no imprime cabus, si no lo pones
        #imprime hasta el final de self
            resultado = self.posicion.value
            self.posicion = self.posicion.next
            return resultado #cada elemento que regresa
        else:
            raise StopIteration
    ######################## FUNCIONES PARA PARCIAL 1 #######################
    def get(self, index):
        if index > self.__len__():
            print("Error, no existe")
        else:
            explorador = self.head
            for i in range(index-1):
                explorador = explorador.next
            return explorador.value
    def printAll(self, pegamento):
        result = ""
        explorador = self.head
        while explorador.next != None:
            if explorador is self.head:
                result += str(explorador.value)
            else:
                result += str(pegamento) + str(explorador.value)
            explorador = explorador.next
        result += str(pegamento) + str(explorador.value)
        print(result)
    
    def dlast(self):
        explorador = self.head
        while explorador.next.next != None:
            explorador = explorador.next
        explorador.next = None
    
    def search(self, s):
        found = 0
        index = 0
        explorador = self.head
        while explorador != None:
            if explorador.value == s:
                found += 1
                pos = index
            explorador = explorador.next
            index += 1
        if found != 0:
            return "Existe el elemento " + str(s) + " en la posicion: " + str(pos)
        else:
            return "No existe el elemento " + str(s)
    
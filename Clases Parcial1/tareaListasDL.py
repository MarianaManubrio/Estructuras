from time import sleep
class nodo():
    def __init__(self, valor): #constructor
        self.value = valor
        self.next = None
        self.last = None

    def get_value(self):
        return self.value
    def get_next(self):
        return self.next
    def get_last(self):
        return self.last

    def set_value(self, valor):
        self.value = valor
    def set_next (self, siguiente):
        self.next = siguiente #self como parametro para los metodos, las funciones no
    def set_last(self, anterior):
        self.last = anterior
        
    
class lista():
    def __init__(self):
        self.lider = nodo ('lider')
        self.cabus = nodo ('Cabus')
        self.lider.next = self.cabus
        self.cabus.last = self.lider
        
        self.lider.last=self.cabus
        self.cabus.next=self.lider

    def is_empty(self):
        return self.lider.next is self.cabus

    def add(self, valor):
        newNodo = nodo(valor)
        newNodo.next = self.lider.next
        newNodo.last = self.lider
        newNodo.next.last = newNodo
        self.lider.next = newNodo

    def remove(self):
        if self.lider.next is not self.cabus:
            self.lider.next = self.lider.next.next
            self.lider.next.last = self.lider 

    def __len__(self):
        contador = 0
        explorador = self.lider.next 
        while explorador is not self.cabus:
            contador += 1
            explorador = explorador.next
        return contador 
######################################################################
    def __getitem__(self, pos):
        if self.__len__() < pos:
            raise IndexError
        explorador = self.lider.next
        for i in range(pos):
            explorador = explorador.next
        return explorador.value
        
    def __str__(self):
        return " ".join([str(x) for x in self])
        #return " ".join([str(x) for x in range(0, self.__len__())])
    
    def __iter__(self):
        self.posicion = self.lider.next #iterador empieza aqui en next
        #for llama a iter para obtener contenedor
        #return regresa lo q quieres como tipo iterador
        #si pongo self.posicion = self.lider imprime desde lider
        return self
    def __next__(self): #avanza dentro de iteradores next (iterador)
        if self.posicion is not self.cabus: # no imprime cabus, si no lo pones
        #imprime hasta el final de self
            resultado = self.posicion.value
            self.posicion = self.posicion.next
            return resultado #cada elemento que regresa
        else:
            raise StopIteration
    #next es lo q repite el for
    
    def add_last(self, valor):
        explorador = self.lider.next
        if explorador is self.cabus:
            newNodo = nodo(valor)
            newNodo.next = self.lider.next
            newNodo.last = self.lider
            self.lider.next.last = newNodo
            self.lider.next = newNodo
        else:
            while explorador.next is not self.cabus:
                explorador = explorador.next
            newNodo = nodo(valor)
            newNodo.next = self.cabus
            newNodo.last = explorador
            explorador.next = newNodo
            self.cabus.last = newNodo
            
    def remove_last(self):
        explorador = self.lider.next
        if explorador is self.cabus:
            print("Sorry you have nothing to erase :)")
        else:
            while explorador.next is not self.cabus:
                explorador = explorador.next
            explorador.last.next = self.cabus
            self.cabus.last = explorador.last
            
        
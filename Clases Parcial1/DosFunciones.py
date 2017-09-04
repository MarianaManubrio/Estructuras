import numpy as np 
class dinamico():
###################### CLASE DINAMICO ##########################
    def __init__(self): 
        self.espacio = 1
        self.tam = 0
        self.arreglo = np.empty(self.espacio, dtype=int)
    def __len__(self):
        return self.tam
    def add(self, nuevo):
        if self.tam < self.espacio:
            self.arreglo[self.tam]=nuevo 
            self.tam += 1
        else:
            self.espacio *=2
            newA = np.empty(self.espacio, dtype = int)
            for i in range (self.tam):
                newA[i]= self.arreglo[i]
            newA[self.tam]=nuevo
            self.tam += 1
            self.arreglo = newA
    def __str__(self):
        #print ("Espacio: {0} \t Elementos: {1}".format(self.espacio, self.tam))
        return "-".join([str(x) for x in self.arreglo[:self.tam]])
        #return "--".join([str(x) for x in self.arreglo])
    def __getitem__(self, pos):
        if 0<=pos<self.tam:
            return self.arreglo[pos]
        else:
            raise IndexError

########################## TAREA ################################

    def dlast(self):
        new1 = np.empty(self.espacio, dtype = int)
        for i in range(0,self.tam-1):
            new1[i] = self.arreglo[i]
        self.arreglo = new1
        self.tam -=1
        if self.espacio > self.tam * 2:
            self.fixTam()
    
    def dfirst(self):
        new2 = np.empty(self.espacio, dtype = int)
        for i in range(0,self.tam-1):
            new2[i] = self.arreglo[i+1]
        self.arreglo = new2
        self.tam -= 1
        if self.espacio > self.tam * 2:
            self.fixTam()
            
    def fixTam(self):
        newEspacio = self.espacio * (0.75)
        newEspacio = int(newEspacio//1)
        self.espacio = newEspacio
        newB = np.empty( self.espacio, dtype = int)
        for i in range (0, self.tam):
            newB[i] = self.arreglo[i]
        self.arreglo = newB
    
        
        
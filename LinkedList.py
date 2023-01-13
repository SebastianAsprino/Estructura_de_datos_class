class LinkedList:
    def __init__(self):
        self.PTR = None
        self.ULT = None
    
    def AddNode(self, data):
        P = Nodo(data)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P
        else:
            self.ULT.next = P
            self.ULT = P
        
    def escribir_lista(self):
        P = self.PTR
        while (P != None):
            print(P.data, end= None)
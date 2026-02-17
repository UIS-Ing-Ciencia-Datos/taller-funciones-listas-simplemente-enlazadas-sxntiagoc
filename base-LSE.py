# Agregar al final

def agregarFinal(self, data):
    nuevo_nodo = Nodo(data)

    # Caso 1: lista vacia
    if self.cabeza is None:
        self.cabeza = nuevo_nodo
        return

    # Caso 2: recorrer hasta el final
    actual = self.cabeza
    while actual.siguiente:
        actual = actual.siguiente

    actual.siguiente = nuevo_nodo

# Insertar despues de un elemento X

def insertarDespues(self, valor_buscar, data):
    actual = self.cabeza

    while actual:
        if actual.data == valor_buscar:
            nuevo_nodo = Nodo(data)
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            return
        actual = actual.siguiente

    print("Elemento no encontrado")

# Insertar antes de un elemento X

def insertarAntes(self, valor_buscar, data):
    if self.cabeza is None:
        print("Lista vacia")
        return

    # Caso 1: antes del primero
    if self.cabeza.data == valor_buscar:
        self.agregarInicio(data)
        return

    actual = self.cabeza

    while actual.siguiente:
        if actual.siguiente.data == valor_buscar:
            nuevo_nodo = Nodo(data)
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            return
        actual = actual.siguiente

    print("Elemento no encontrado")

#  Eliminar el primero

def eliminarPrimero(self):
    if self.cabeza is None:
        print("Lista vacía")
        return

    self.cabeza = self.cabeza.siguiente

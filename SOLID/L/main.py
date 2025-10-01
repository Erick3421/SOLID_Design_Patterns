from A import A
from B import B

objetoA = A()
objetoB = B()

def imprimirNome(obj: A):
    return obj.getNome()

print(imprimirNome(objetoA))
print(imprimirNome(objetoB))
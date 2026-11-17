def paran(n:int):
 return n%2==0
def prost(n:int):
    if n<2:
      return False
    if n==2 or n==3:
      return True
    odgovor=True
    for i in range(2,n-1):
        if n%i==0:
            odgovor=False
    return odgovor

def kvadrat(n:int):
    for i in range(1,n):
        if i*i==n:
            return True
def djelitelji(n:int):
    lista=[]
    for i in range(1,n+1):
      if n%i==0:
        lista.append(i)
    return lista
def prostifaktori(n:int):
    lista=[]
    b=n
    ponovi = True
    while ponovi:
        ponovi=False
        for i in range(2,n+1):
          if prost(i)and b%i==0:
            lista.append(i)
            b=b/i
            ponovi=True
            break
    return lista


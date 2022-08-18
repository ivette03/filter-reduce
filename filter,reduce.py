from functools import reduce

def miFuncion(a):
   resultado=filter(lambda a: a%2, lista)
   re=list(resultado)
   print(re)
   suma=reduce( (lambda a,b:a+b),re)
   print(suma)

lista=list(range(50))
miFuncion(lista)





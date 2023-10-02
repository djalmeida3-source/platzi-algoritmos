# Dada una cadena de caracteres, invierte solo todas las vocales de la cadena.
# Las vocales son ‘a’, ‘e’, ‘i’, ‘o’ y ‘u’, ‘A’, ‘E’, ‘I’, ‘O’, ‘U’.

def invertir_vocales(cadena: str) -> str:
   numeros = list(cadena)
   p1 = 0
   p2= len(numeros) - 1
   vocales = {'a','e','i','o','u','A','E','I','O','U'}
   while p1 < p2:
       if numeros[p1] in vocales and numeros[p2] in vocales:
           numeros[p1], numeros[p2] = numeros[p2], numeros[p1]
           p1+=1
           p2-=1
       else:
           while numeros[p1] not in vocales and p1 < p2:
               p1 += 1
           while numeros[p2] not in vocales and p1 < p2:
               p2 -=1
 
   return "".join(numeros)

s = "leetcode"

s = invertir_vocales(s)

print(s)
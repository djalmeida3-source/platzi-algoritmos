# Dada una cadena de caracteres, averigua si la cadena dada es un palíndromo o no. 
# Puedes eliminar un carácter de la cadena. Una cadena es un palíndromo si se lee igual hacia adelante y hacia atrás.

def es_palindrome_valido(frase: str) -> bool:
   p1 = 0
   p2 = len(frase) - 1
  
   def es_palindrome(p1,p2):
       while p1 < p2:
           if frase[p1] == frase[p2]:
               p1 += 1
               p2 -= 1
           else:
               return False
       return True
  
   while p1 < p2:
       if frase[p1] != frase[p2]:
           return es_palindrome(p1+1,p2) or es_palindrome(p1,p2-1)
       else:
           p1 += 1
           p2 -= 1
          
   return True

s = "abca"
print (es_palindrome_valido(s))

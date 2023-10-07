# Encontrar la mayor longitud de un substring dentro de una cadena de caracteres donde no se repitan caracteres

def lengthOfLongestSubstring(s: str) -> int:
  # Complejidad espacial: O(n)
  inicio = 0
  caracteresAposicion = {}
  mayorLongitud = 0
  # Complejidad temporal: O(n)
  for fin in range(len(s)):
    if s[fin] in caracteresAposicion and inicio <= caracteresAposicion[s[fin]]:
      inicio = caracteresAposicion[s[fin]] + 1
    caracteresAposicion[s[fin]] = fin
    mayorLongitud = max(mayorLongitud, fin - inicio + 1)

  return mayorLongitud

s = "abcdaef"

print(lengthOfLongestSubstring(s))
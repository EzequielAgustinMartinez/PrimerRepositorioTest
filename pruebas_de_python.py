def palindromo(frase):
      inicio = 0
      fin = len(frase) - 1
      while frase[inicio] == frase[fin]:
         if inicio >= fin:
            return True
         inicio += 1
         fin -= 1   
      return False
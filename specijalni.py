
# Savršen broj je onaj čiji je zbroj njegovih pravih djelitelja (isključujući njega samog) jednak tom broju.
def savrsen(n):
  if n <= 1:
    return False
  suma_djelitelja = sum(i for i in range(1, n) if n % i == 0)
  return suma_djelitelja == n

# Broj je Armstrongov ako je zbroj njegovih znamenki potenciran na broj znamenki jednak samom broju.
def armstrongov(n):
  if n < 0:
    return False
  s = str(n)
  k = len(s)
  suma = sum(int(znamenka) ** k for znamenka in s)
  return suma == n

# Zbroj znamenaka unešenog broja djeljiv je brojem njegovih znamenaka.
def lijep(n):
  if n <= 0:
    return False
  s = str(n)
  zbroj = sum(int(znamenka) for znamenka in s)
  broj_znamenki = len(s)
  return zbroj % broj_znamenki == 0

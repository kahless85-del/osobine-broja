
# Vraća True ako se broj čita jednako s obje strane.
def palindrom(n):
  s = str(n)
  return s == s[::-1]



# Vraća zbroj znamenki unešenog prirodnog broja.
def zbroj_znamenki(n):
  return sum(int(znamenka) for znamenka in str(abs(n)))



# Vraća binarni prikaz broja kao string bez prefiksa '0b'.
def binarni(n):
  return bin(n)[2:]

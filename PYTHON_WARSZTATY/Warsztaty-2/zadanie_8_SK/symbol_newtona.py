#Autor: Sławomir Kranc

('------------------------------------------------')
('To jest biblioteka obliczająca symbol Newtona . ')
('------------------------------------------------')

#To jest funckja pobierająca argument od użytkownika.
def get_number():
  while True:
   try:
     n = int(input('Podaj liczbę: '))
     return n
   except ValueError:
     print('Proszę wprowadzić liczbę!')
   except SignError:
     print('Proszę wprowadzić liczbę!')

#To jest funckja obliczająca silnię.
def silnia(n):
  if n <= 0 : return 1
  return silnia(n-1) * n

#To jest funckja obliczająca symbol Newtona.
def symbol_newtona(n,k):
  return silnia(n) / (silnia(k) * silnia(n-k))

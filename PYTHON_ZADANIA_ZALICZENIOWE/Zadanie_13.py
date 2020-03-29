# -*- coding: utf-8 -*-
'''
Autor: Sławomir Kranc

Treść zadania 13:
Utworzyć skrypt z interfejsem tekstowym obliczający symbol Newtona n po k.
Utworzyć funkcję, która będzie wywoływać inną funkcję

'''
#To jest funkcja pobierająca argument od użytkownika.
def get_number():
  while True:
   try:
     n = int(input(': '))
     return n
   except ValueError:
     print('Proszę wprowadzić liczbę!')

#To jest funckja obliczająca silnię.
def silnia(n):
  if n <= 0 : return 1
  return silnia(n-1) * n

#To jest funkcja obliczająca symbol Newtona.
def symbol_newtona(n,k):
  return silnia(n) / (silnia(k) * silnia(n-k))

def main():

  print('---------------------------------------------')
  print('To jest program obliczający symbol Newtona. ')
  print('---------------------------------------------')
  while True:
    print('Proszę wprowadzić wprowadzić liczbę n: ')
    n = get_number()
    print('Proszę wprowadzić wprowadzić liczbę k: ')
    k = get_number()
    sm = symbol_newtona(n,k)
    print('\nDla liczb n = {} oraz k = {} symbol Newtona wynosi {}' .format(n,k,sm))

    decyzja = input('Czy chcesz wykonać jeszcze raz? (t/n) ')
    if decyzja == 't':
      continue
    elif decyzja == 'n':
      print('Do zobaczenia!')
      input('Kliknij dowolny klawisz, aby opuścić program ...')
      break
    else:
      print('Proszę podjąć decyzję!')

if __name__ == "__main__":
  main()

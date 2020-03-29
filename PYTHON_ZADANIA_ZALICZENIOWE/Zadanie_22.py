# -*- coding: utf-8 -*-
'''
Autor: Sławomir Kranc

Treść zadania 22:
Utwórz fukcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych, a jej wynikiem będzie mediana (skorzystaj z metody sort działającej na standardowych listach).
'''

#To jest funkcja obliczająca medianę z listy liczb, także zmiennoprzecinkowych.
def mediana(lista):
  lista.sort()
  middle = int(len(lista)/2)
  if (len(lista)%2 == 0):
      return (lista[middle-1]+lista[middle])/2
  else:
      return lista[middle]

def main():
  print('------------------------------------------------------------------------------')
  print('To jest program, który przyjmuje listę liczb, także tych zmiennoprzecinkowych, oraz wylicza ich medianę.')
  print('------------------------------------------------------------------------------')
  lista = [4.5,66.52,16.8,75.2,10.1,82.94,6.1,2.92]

  obl_med = mediana(lista)
  print('\nDla argumentów z listy: \n{} \nmediana wynosi: \n{}' .format(lista,obl_med))

if __name__ == '__main__':
    main()

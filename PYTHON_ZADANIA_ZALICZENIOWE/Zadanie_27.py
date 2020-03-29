# -*- coding: utf-8 -*-
'''
Autor: Sławomir Kranc

Treść zadania 27:
Utwórz funkcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych, a jej wynikiem będzie czwarty moment centralny (kurtoza)
'''

def srednia(lista):
    return sum(lista)/len(lista)

def odchylenie(lista):
    suma = 0
    temp_srednia = srednia(lista)
    for i in range(len(lista)):
        suma = suma + (lista[i] - temp_srednia)**2
    return ((suma/len(lista))**(1/2))

def wariancja(lista):
    suma = 0
    temp_srednia = srednia(lista)
    for i in range(len(lista)):
        suma = suma + (lista[i] - temp_srednia)**2
    return (suma/len(lista))

def kurtoza(lista):
    suma = 0
    temp_srednia = srednia(lista)
    for i in range(len(lista)):
        suma = suma + (lista[i] - temp_srednia)**4
    return (((1/odchylenie(lista)**4)*(suma/len(lista)))-3)

def main():

  print('------------------------------------------------------------------------------')
  print('To jest program, który przyjmuje listę liczb, także tych zmiennoprzecinkowych, oraz wylicza ich czwarty moment centralny, czyli kurtozę.')
  print('------------------------------------------------------------------------------')
  lista = [23.4,67.2,4.9,72.99,36.55]
  obl_srednia = srednia(lista)
  obl_odchylenie = odchylenie(lista)
  obl_wariancja = wariancja(lista)
  obl_kurtoza = kurtoza(lista)
  print('\nDla argumentów z listy: \n{} \nkurtoza wynosi: \n{}' .format(lista,obl_kurtoza))

if __name__ == '__main__':
    main()

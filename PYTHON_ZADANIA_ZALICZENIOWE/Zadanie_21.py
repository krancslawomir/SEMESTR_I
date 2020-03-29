# -*- coding: utf-8 -*-
'''
Autor: Sławomir Kranc

Treść zadania 21:
Utwórz fukcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych, a jej wynikiem będzie średnia arytmetyczna. Porównaj jej wynik z wynikiem fukcji mean z pakietu numpy
'''

import numpy as np

def numpy_srednia(lista):
    return np.mean(lista)


#To jest funkcja obliczająca średnią arytmetyczną z listy liczb, także zmiennoprzecinkowych.
def srednia(lista):
    return sum(lista)/len(lista)

def main():

  lista = [4.5,66.52,16.8,75.2,10.1,82.94,6.1,2.92]

  obl_sre = srednia(lista)
  obl_sre_num = numpy_srednia(lista)
  print('\nDla argumentów z listy: \n{} \nśrednia arytmetyczna wynosi: {} \nNumpy wyliczył, że średnia arytmetyczna wynosi: {}' .format(lista,obl_sre, obl_sre_num))


if __name__ == '__main__':
    main()

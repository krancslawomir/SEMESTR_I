# -*- coding: utf-8 -*-
'''
Autor: Sławomir Kranc

Treść zadania 19:
Korzystając ze słownika, utwórz funkcję, która będzie zwracać liczbę dni danego miesiąca w roku.
'''

miesiace = {"Styczeń" : 31, "Luty" : 28, "Marzec" : 31, "Kwiecień" : 30, "Maj" : 31, "Czerwiec" : 31, "Lipiec" : 31, "Sierpień" : 31, "Wrzesień" : 30, "Październik" : 31, "Listopad" : 30, "Grudzień" : 31}

def dni(miesiace, x):
  return miesiace.get(x)

def main():

  x = input ("Podaj miesiąc: ")
  obl_dzien = dni(miesiace, x)

  print('\nW miesiącu: {} liczba dni wynosi: {} ' .format(x, obl_dzien))

if __name__ == '__main__':
    main()

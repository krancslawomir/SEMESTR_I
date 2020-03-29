# -*- coding: utf-8 -*-
'''
Autor: Sławomir Kranc

Treść zadania 5:
Utwórz skrypt, który będzie komunikować, czy wprowadzona liczba jest dodatnia czy nie.
'''

def main():

  print('----------------------------------------------------------------------------------')
  print("Witaj! To jest program komunikujący, czy wprowadzona liczba jest dodatnia czy nie.")
  print('----------------------------------------------------------------------------------')

  while True:

    try:

      while True:

        liczba = float(input('Wprowadź liczbę: '))
        if liczba >= 0:
          print('Wprowadzona liczba jest dodatnia.')
        else:
          print('Wprowadzona liczba jest ujemna.')

        while True:
          decyzja = input('Czy chcesz wykonać jeszcze raz? (t/n) ')
          if decyzja == 't':
            break
          elif decyzja == 'n':
            print('Do zobaczenia!')
            input('Kliknij dowolny klawisz, aby opuścić program ...')
            return
          else:
            print('Proszę podjąć decyzję! (t/n)')

    except ValueError:
      print('Wprowadziłeś niepoprawną liczbę. Spróbuj jeszcze raz.')
    continue

if __name__ == "__main__":
  main()

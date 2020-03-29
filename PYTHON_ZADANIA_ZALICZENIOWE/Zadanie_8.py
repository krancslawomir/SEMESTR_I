# -*- coding: utf-8 -*-
'''
Autor: Sławomir Kranc

Treść zadania 8:
W klasie przeprowadzono sprawdzian, za który uczniowie mogli otrzymać maksymalnie 40 punktów.
Skala ocen w szkole jest następująca:
0-39% - ndst,
40-49% - dop,
50-69% - dst,
70-84% - db,
85-99% - bdb,
100% - cel.
Utwórz skrypt z interfejsem tekstowym, który na podstawie podanej liczby punktów ze sprawdzianu wyświetli ocenę jaka się należy (skorzystaj z konstrukcji if, elif, else)
'''

class valueError(Exception):
    pass


def main():

  print('------------------------------------------------------------------------------------------------')
  print('To jest program, który na podstawie podanej liczby punktów ze sprawdzianu wyświetli ocenę jaka się należy. \nPamiętaj,że maksymalna liczba punktów do uzyskania z tego sprawdzianu wynosi 40! \nSkala ocen wygląda następująco: \n\t 0%-40% = ocena niedostateczna \n\t40%-49% = ocena dopuszczająca \n\t50%-69% = ocena dostateczna \n\t70%-84% = ocena dobra \n\t85%=99% = ocena bardzo dobra \n\t   100% = ocena celująca')
  print('------------------------------------------------------------------------------------------------')

  decyzja ='t'

  while decyzja == 't':
    while True:

      try:
        a = int(input('Wprowadź liczbę punktów ze sprawdzianu: '))

        if a < 0 or a > 40:
          raise valueError
        else:
          break

      except valueError:
        print('Wprowadzona wartość musi się mieścić w zakresie 0-40')
      except Exception:
        print('Program przyjmuje tylko liczby!')


    obl_procent = round((a/40)*100, 2)
    print("Liczba procent wynosi: " + str(obl_procent) + '%')


    if obl_procent <= 39:
      print('Ocena niedostateczna.')

      while True:
        print('Czy wykonać zamianę jeszcze raz? (t/n)')
        decyzja = input()
        if decyzja == 't':
          break
        elif decyzja == 'n':
          print('Do zobaczenia!')
          print('Wciśnij dowolny klawisz aby opuścić program ...')
          return
        else: print('Proszę podjąć decyzję!')

    elif obl_procent >= 40 and obl_procent <= 49:
      print('Ocena dopuszczająca')

      while True:
        print('Czy wykonać zamianę jeszcze raz? (t/n)')
        decyzja = input()
        if decyzja == 't':
          break
        elif decyzja == 'n':
          print('Do zobaczenia!')
          print('Wciśnij dowolny klawisz aby opuścić program ...')
          return
        else: print('Proszę podjąć decyzję!')

    elif obl_procent >= 50 and obl_procent <= 69:
      print('Ocena dostateczna.')

      while True:
        print('Czy wykonać zamianę jeszcze raz? (t/n)')
        decyzja = input()
        if decyzja == 't':
          break
        elif decyzja == 'n':
          print('Do zobaczenia!')
          print('Wciśnij dowolny klawisz aby opuścić program ...')
          return
        else: print('Proszę podjąć decyzję!')

    elif  obl_procent >= 70 and obl_procent <= 84:
      print('Ocena dobra')

      while True:
        print('Czy wykonać zamianę jeszcze raz? (t/n)')
        decyzja = input()
        if decyzja == 't':
          break
        elif decyzja == 'n':
          print('Do zobaczenia!')
          print('Wciśnij dowolny klawisz aby opuścić program ...')
          return
        else: print('Proszę podjąć decyzję!')

    elif  obl_procent >= 85 and obl_procent <= 99:
      print('Ocena bardzo dobra')

      while True:
        print('Czy wykonać zamianę jeszcze raz? (t/n)')
        decyzja = input()
        if decyzja == 't':
          break
        elif decyzja == 'n':
          print('Do zobaczenia!')
          print('Wciśnij dowolny klawisz aby opuścić program ...')
          return
        else: print('Proszę podjąć decyzję!')


    elif  obl_procent == 100:
      print('Ocena celująca')

      while True:
        print('Czy wykonać zamianę jeszcze raz? (t/n)')
        decyzja = input()
        if decyzja == 't':
          break
        elif decyzja == 'n':
          print('Do zobaczenia!')
          print('Wciśnij dowolny klawisz aby opuścić program ...')
          return
        else: print('Proszę podjąć decyzję!')


if __name__ == "__main__":

  main()

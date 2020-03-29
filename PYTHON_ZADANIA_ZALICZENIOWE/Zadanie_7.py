# -*- coding: utf-8 -*-
'''
Autor: Sławomir Kranc

Treść zadania 7:
Utwórz skrypt z interfejsem tekstowym, który pobierze od użytkownika zdanie i wyświetli w kolejnych wierszach litery tego zdania w odwróconej kolejności.
'''
def main():

  print('-----------------------------------------------------------------------')
  print('To jest program który pobiera od użytkownika zdanie i wyświetla w kolejnych wierszach litery tego zdania w odwróconej kolejności.')
  print('-----------------------------------------------------------------------')

  while True:

    zdanie = input("Wpisz proszę zdanie: ")

    for i in range(0, len(zdanie)):
      print(zdanie[len(zdanie)-1-i])

    while True:
      print('Czy wykonać wyszkukiwanie jeszcze raz? (t/n)')
      decyzja = input()
      if decyzja == 't':
        break
      elif decyzja == 'n':
        print('Do zobaczenia wkrótce!')
        input('Wciśnij dowolny klawisz, aby opuścić program ...')
        return
      else: print('Proszę podjąć decyzję (t/n)')

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
'''
Autor: Sławomir Kranc

Treść zadania 34:
Utwórz klasę Kwadrat z konstruktorem ustalającym jego bok oraz metodami:
wyświetlającymi wartość tego boku, obliczającymi pole i obwód figury.
'''

class Kwadrat:
    def __init__(self, a):
        self.a = a

    def obwod(self):
        return self.a*4

    def pole(self):
        return self.a*self.a

def main():

  n = int(input('Podaj długość boku: \n' ))
  figura = Kwadrat(n)
  print('Dla boku a o długości: {} obwód wynosi: {} \nnatomiast pole jest równe: {}' .format(figura.a, figura.obwod(),figura.pole()))

if __name__ == '__main__':
    main()

#Autor: Sławomir Kranc

from math import sqrt

#To jest funkcja obliczająca pierwszy pierwiastek.
def OBL_X1(a, b, c):
    X1 = (-b+sqrt(b*b-4*a*c))/(2*a)
    return X1

#To jest funkcja obliczająca drugi pierwiastek.
def OBL_X2(a, b, c):
    X2 = (-b-sqrt(b*b-4*a*c))/(2*a)
    return X2

#To jest funkcja obliczająca jedyny pierwiastek.
def OBL_X(a, b, c):
    X = (-b/(2*a))
    return X

#To jest fukcja obliczająca deltę.
def OBL_DELTA(a, b, c):
    DELTA = (b*b)-(4*a*c)
    return DELTA

def main():

  print('----------------------------------------------------------------')
  print('To jest program szukający miejsca zerowe trójmianu kwadratowego.')
  print('----------------------------------------------------------------')

  while True:

    print('\nCo chesz zrobić ? Wybierz proszę opcję ...')
    print('\n\t1.Jeżeli chcesz poszukać miejsc zerowych. \n\t2.Jeżeli chcesz opuścić program.')

    decyzja = input()

    if decyzja == '1':

      while True:
        try:

          a = float(input('Wprowadź liczbę a: '))
          b = float(input('Wprowadź liczbę b: '))
          c = float(input('Wprowadź liczbę c: '))


          DELTA = OBL_DELTA(a, b, c)
          print(' Delta wynosi ' + str(DELTA))

          if DELTA < 0:
            print('Funkcja kwadratowa nie ma miejsc zerowych, trójmian kwadratowy nie ma pierwiastków rzeczywistych, równanie kwadratowe nie ma rozwiązań.')

            print('Czy wykonać zamianę jeszcze raz? (t/n)')
            decyzja = input()
            if decyzja != 't':
              break

          elif DELTA == 0:
            print('Funkcja kwadratowa ma dokładnie jedno miejsce zerowe, trójmian kwadratowy ma jeden pierwiastek podwójny, równanie kwadratowe ma dokładnie jedno rozwiązanie rzeczywiste.')

            x1x2 = OBL_X(a, b, c)
            print('Miejsce zerowe funkcji to: ' + str(x1x2))

            print('Czy wykonać zamianę jeszcze raz? (t/n)')
            decyzja = input()
            if decyzja != 't':
              break

          elif DELTA > 0:
            print('Funkcja kwadratowa ma dwa miejsca zerowe, trójmian kwadratowy ma dwa różne pierwiastki rzeczywiste, równanie kwadratowe ma dwa rozwiązania rzeczywiste.')

            x1 = OBL_X1(a, b, c)
            x2 = OBL_X2(a, b, c)
            print('Pierwsze miejsce zerowe funkcji to: ' + str(x1))
            print('Drugie miejsce zerowe funkcji to: ' + str(x2))

            print('Czy wykonać zamianę jeszcze raz? (t/n)')
            decyzja = input()
            if decyzja != 't':
              break

        except ValueError:
            print('Wprowadzono nieprawidłową liczbę.')
            break
    elif decyzja == '2':
        print('Do zobaczenia!')
        break

    else: print('\n\nSystem uznaje jedynie odpowiedzi \"1\" \"2\".')

main()

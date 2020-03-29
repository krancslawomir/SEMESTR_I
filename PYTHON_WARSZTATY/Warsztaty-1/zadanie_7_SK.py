#Autor: Sławomir Kranc

from fractions import Fraction

def main():

  print('----------------------------------------------')
  print("Witaj! To jest program dodający ułamki zwykłe.")
  print('----------------------------------------------')

  while True:

      print('\nCo chesz zrobić ? Wybierz proszę opcję ...')
      print('\n\t1.Jeżeli chcesz dodawać ułamki. \n\t2.Jeżeli chcesz opuścić program.')

      decyzja = input()

      if decyzja == '1':

        try:

          while True:

            a = Fraction(input(' Wprowadź pierwszy ułamek, na przykład 3/4:  '))
            b = Fraction(input(' Wprowadź drugi ułamek, na przykład 1/2:  '))

            dodawanie = Fraction(a) + Fraction(b)
            print('Wynik dodawania ułamków  ' + str(a) + '  i  ' + str(b) + '  wynosi:  ' + str(dodawanie))

            print("czy wykonać jeszcze raz? (t/n)")
            decyzja = input()
            if decyzja == 't':
              continue
            elif decyzja == "n":
              break
            else:
              print('Proszę podjąć decyzję (t/n)')
              continue

        except ValueError:
          print('Wprowadzono nieprawidłową liczbę.')
        continue

      elif decyzja == '2':
        print('Do zobaczenia!')
        break

      else:
        print('System akceptuje tylko odpowiedzi \"1\" lub \"2\" ')

if __name__ == "__main__":

  main()

#Autor: Sławomir Kranc


#To jest funkcja obliczająca temperaturę w jednostkach Celsjusza.
def FnaC(F):
    C = (F-32)*(5/9)
    return C

#To jest funkcja obliczająca temperaturę w jednostkach Fahrenheita.
def CnaF(C):
    F = (C*9/5)+32
    return F

def main():

  print('------------------------------------------------------------------------------------------')
  print('Witaj! To jest program, który zamienia temperaturę między skalami Celsjusza i Fahrenheita.')
  print('------------------------------------------------------------------------------------------')

  while True:

    print('\nCo chcesz zrobić ? Wybierz proszę opcję ...')

    print('\n\t1.Wybierz jeżeli chcesz przeliczyć wartość na temperaturę w jednostkach Celsjusza. \n\t2.Wybierz jeżeli chcesz przeliczyć wartość na temperaturę w jednostkach Fahrenheita. \n\t3.Wybierz jeżeli chcesz opuścić program.')


    decyzja  = input()

    if decyzja == '1':

      try:

        decyzja = 't'

        while decyzja == 't':
          print('Podaj wartość, którą chcesz zamienić:')

          liczba = float(input())
          x = round(FnaC(liczba),2)
          print(str(liczba) + ' stopni Fahrenheita, to: ' + str(x) + ' stopni Celsjusza. ')

          print('Czy wykonać zamianę jeszcze raz? (t/n)')
          decyzja = input()
          if decyzja != 't':
            break

      except ValueError:
        print('Wprowadzono nieprawidłową liczbę.')

    elif decyzja == '2':

      try:

        decyzja_tak = 't'

        while decyzja_tak == 't':
          print('Podaj wartość, którą chcesz zamienić:')

          liczba = float(input())
          y = round(CnaF(liczba),2)
          print(str(liczba) + ' stopni Celsjusza, to: ' + str(y) + ' stopni Fahrenheita. ')

          print('Czy wykonać zamianę jeszcze raz? (t/n)')
          decyzja = input()
          if decyzja != 't':
            break

      except ValueError:
        print('Wprowadzono nieprawidłową liczbę.')

    elif decyzja == '3':
      print('Do zobaczenia!')
      break

    else: print('\n\nSystem uznaje jedynie odpowiedzi \"1\" \"2\" \"3\".')


main()

#Autor: Sławomir Kranc


#To jest funkcja obliczająca wartość w kilometrach
def MnaK(M):
    K = M/0.62137
    return K

#To jest funkcja obliczająca wartość w milach
def KnaM(K):
    M = K*0.62137
    return M


def main():

  print('-----------------------------------------------------------------------------')
  print('Witaj! To jest program, który zamienia jednostki odległości mili i kilometra.')
  print('-----------------------------------------------------------------------------')

  while True:

      print('\nCo chesz zrobić ? Wybierz proszę opcję ...')
      print('\n\t1.Jeżeli chcesz przeliczyć wartość na mile. \n\t2.Jeżeli chcesz przeliczyć wartość na kilometry. \n\t3.Jeżeli chcesz opuścić program.')

      decyzja = input()

      if decyzja == '1':

        try:

          decyzja = 't'

          while decyzja == 't':
            print('Podaj wartość kilometrów, którą chcesz zamienić zamienić na mile:')

            liczba = float(input())
            x = round(KnaM(liczba),2)
            print(str(liczba) + ' kilometrów, to: ' + str(x) + ' mil. ')

            print('Czy wykonać działanie jeszcze raz? (t/n)')
            decyzja_tak = input()
            if decyzja_tak != 't':
              break


        except ValueError:
          print('Wprowadzono nieprawidłową liczbę.')


      elif decyzja == '2':

        try:

          decyzja = 't'

          while decyzja == 't':
            print('Podaj wartość mil, którą chcesz zamienić zamienić na kilometry:')

            liczba = float(input())
            y = round(MnaK(liczba),2)
            print(str(liczba) + ' mil, to: ' + str(y) + ' kilometrów. ')

            print('Czy wykonać działanie jeszcze raz? (t/n)')
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

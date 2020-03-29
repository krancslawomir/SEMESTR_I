#Autor: Sławomir Kranc

def main():

  print('-------------------------------------------------------------------------------------------')
  print('Witaj! To jest program, który mnoży podaną przez Ciebie liczbę do wielokrotności liczby 10.')
  print('-------------------------------------------------------------------------------------------')

  try:

    while True:

      liczba = float(input('Podaj proszę interesującą Cię liczbę: '))

      for i in range(1, 11):
        print('{0} * {1} = {2}' .format(liczba, i, liczba*i))


      while True:
        decyzja = input('Czy chcesz wykonać jeszcze raz? (t/n) ')
        if decyzja == 't':
          break
        elif decyzja == 'n':
          print('Do zobaczenia!')
          input('Kliknij dowolny klawisz, aby opuścić program ...')
          return
        else:
          print('Proszę podjąć decyzję!')

  except ValueError:
    print('Wprowadzono nieprawidłową liczbę.')
    input('Wciśnij dowolny klawisz, aby opuścić program')


if __name__ == "__main__":

  main()

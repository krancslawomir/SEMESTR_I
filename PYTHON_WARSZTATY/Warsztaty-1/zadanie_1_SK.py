#Autor: Sławomir Kranc

def main():

  print('--------------------------------------------------------------------------------------')
  print('Witaj! To jest program, który wyszukuje wszystkie dzielniki podanej liczby całkowitej.')
  print('--------------------------------------------------------------------------------------')

  try:

    while True:
      liczba = int(input('Podaj proszę interesująca Cię liczbę: '))
      for i in range(2, liczba+1):
        if (liczba%i == 0):
          print(i)

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
    input('Wciśnik enter aby zakończyć program...')

if __name__ == "__main__":

  main()

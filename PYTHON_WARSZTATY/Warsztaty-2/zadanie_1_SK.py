#Autor: Sławomir Kranc

def main():

  print('-----------------------------------------------------------------------')
  print('To jest program który pobiera od użytkownika zdanie i wyświetla w kolejnych wierszach litery tego zdania w odwróconej kolejności.')
  print('-----------------------------------------------------------------------')


  try:

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


  except ValueError:
    print('Wprowadzono nieprawidłową liczbę.')
    input('Wciśnik enter aby zakończyć program...')

main()

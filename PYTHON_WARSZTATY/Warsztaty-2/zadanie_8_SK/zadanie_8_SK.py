#Autor: Sławomir Kranc

import symbol_newtona as sn

print('-------------------------------------------------------------------')
print('To jest program zwracający wiersz n-tego rzędu z trójkąta Pascala. ')
print('-------------------------------------------------------------------')

#To jest funckja zwracając elementy danego rzętu z trójkąta Pascala.
def trojkat_pascala(n):
  return [sn.symbol_newtona(n,i) for i in range(n+1)]


#To jest główna funkcja.
def main():
  while True:
    print('Podaj numer wiersza:')
    n = sn.get_number()
    print(trojkat_pascala(n))

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


if __name__ == "__main__":

  main()

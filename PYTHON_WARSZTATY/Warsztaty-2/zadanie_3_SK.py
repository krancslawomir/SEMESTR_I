#Autor: Sławomir Kranc

print('---------------------------------------------------------------------------------------------------------')
print('To jest program, który wyliczy sumę n kolejnych liczb (użytkownik podaje pierwszą i ostatnią liczbę sumy!')
print('---------------------------------------------------------------------------------------------------------')

#[Funkcja 1] To jest funkcja pobierająca od użytkownika liczby.
def getNumbers():
  while True:
    try:
      a = int(input('Podaj pierwszą liczbę: '))
      b = int(input('Podaj drugą liczbę: '))
      return (a, b)
    except TypeError:
      print('Proszę wprowadzić liczbę: ')
    except ValueError:
      print('Proszę wprowadzić liczbę: ')

#[Funkcja 2] To jest funkcja obliczająca sumę n kolejnych liczb
def calculate(a, b):
  suma = 0
  for i in range (a, b+1):
    suma += i
  return suma


#To jest główna funkcja wywołująca funkcję 1 o obliczająca wynik z funkcji 2
def main():
  while True:
    pierwszaLiczba, drugaLiczba = getNumbers()
    print('Suma kolejnych liczb od {} do {} jest równa {} '.format(pierwszaLiczba, drugaLiczba, calculate(pierwszaLiczba, drugaLiczba)))

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

#Autor: Sławomir Kranc


print('--------------------------------------------------------')
print('To jest program, który liczy silnię od danego argumentu. ')
print('--------------------------------------------------------')

#To jest funkcja przyjmująca argument od użytkownika
def getArgument():
  while True:
    try:
      n = int(input('Podaj argument: '))
      return n
    except TypeError:
      print('Proszę wprowadzić liczbę: ')
    except ValueError:
      print('Proszę wprowadzić liczbę: ')

#To jest funkcja iteracyjna licząca silnię danego argumentu.
def silniaFunkcyjnie(n):
  silnia = 1
  for i in range (2, n+1):
    silnia *= i
  return silnia

#To jest funkcja rekurencyjna licząca silnię danego argumentu.
def silniaRekurencyjnie(n):
  if n == 0: return 1
  return n*silniaRekurencyjnie(n-1)


#To jest główna funkcja.
def main():
  while True:
    n = getArgument()
    silniaFun = silniaFunkcyjnie(n)
    silniaRec = silniaRekurencyjnie(n)
    print('Dla argumentu {} silnia iteracyjna wynosi {}' .format (n, silniaFun))
    print('Dla argumentu {} silnia rekurencyjna wynosi {}' .format (n, silniaRec))

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

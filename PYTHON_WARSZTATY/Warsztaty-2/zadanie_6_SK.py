#Autor: Sławomir Kranc


print('--------------------------------------------------------------')
print('To jest program obliczający n-ty element ciągu Fibonacciego . ')
print('--------------------------------------------------------------')

#To jest funkcja przyjmująca argument od użytkownika.
def getArgument():
  while True:
    try:
      n = int(input('Podaj element: '))
      return n
    except TypeError:
      print('Proszę wprowadzić liczbę: ')
    except ValueError:
      print('Proszę wprowadzić liczbę: ')

#To jest funckja interacyjna obliczająca ciąg Fibonacciego.
def ciagFunkcyjnie(n):
  a1 = 0
  a2 = 1
  for i in range (1, n):
    a3 = a1+a2
    a1=a2
    a2=a3
  return a3

#To jest funckja rekurencyjna obliczająca ciąg Fibonacciego.
def ciagRekurencyjnie(n):
  if n <=1: return n
  return ((ciagRekurencyjnie(n-1)+(ciagRekurencyjnie(n-2))))


#To jest główna funkcja.
def main():
  while True:
    n = getArgument()
    ciagFun = ciagFunkcyjnie(n)
    ciagRec = ciagRekurencyjnie(n)
    print('Dla argumentu {} ciag Fibonacciego iteracyjnie wynosi {}' .format (n, ciagFun))
    print('Dla argumentu {} ciag Fibonacciego rekurencyjnie wynosi {}' .format (n, ciagRec))
    
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

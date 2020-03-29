#Autor: Sławomir Kranc


import numpy as np

print('---------------------------------------------------------------------------------------------')
print('To jest program, który przyjmumje od użytkownika ile elementów chce on wprowadzić do listy, przyjmuje te elementy, a następnie liczy: średnią i odchylenie standardowe średniej. ')
print('---------------------------------------------------------------------------------------------')

#[Funkcja 1] To jest funkcja pobierająca od użytkownika ilość elementów do listy.
def setNumber():
  while True:
    try:
      n = int(input('Podaj ilość elementów do listy: '))
      return n
    except TypeError:
      print('Proszę wprowadzić liczbę: ')
    except ValueError:
      print('Proszę wprowadzić liczbę: ')

#[Funkcja 2]To jest funkcja przyjmująca od użytkownika elementy do listy.
def getElementToList(n):
  while True:
    try:
      i = 0
      myList = []
      while i < n:
        element = int(input('Podaj element: '))
        myList.append(element)
        i += 1
      return myList
    except TypeError:
      print('Proszę wprowadzić liczbę: ')
    except ValueError:
      print('Proszę wprowadzić liczbę: ')

#[Funkcja 3]To jest funkcja obliczająca sumę elementów z listy.
def calculateSum(myList):
  suma = 0
  for i in myList:
    suma += i
  return suma

#[Funkcja 4]To jest funkcja obliczająca średnią z elementów listy.
def calculateAverage(suma, n):
  average = suma / n
  return average

#[Funkcja 5]To jest funkcja obliczająca odchylenie standardowe z elementów listy i zaokrąglająca wynik do dwóch miejsc po przecinku.
def calculateStandardDeviation(myList, average, n):
  sd1 = 0
  for i in myList:
    temporary = ((i - average)**2)
    sd1 += temporary
  return round((sd1 / (n))**0.5, 2)

def numpyCalculation(myList):
  myArray = np.array(myList)
  myStd = np.std(myArray)
  myAvg = np.average(myArray)
  return myStd, myAvg




def main():
  while True:
    #To jest główna funkcja wywołująca funkcję 1
    numberOfElements = setNumber()

    #To jest główna funkcja wywołująca funkcję 2
    elements = getElementToList(numberOfElements)

    #To jest główna funkcja wywołująca funkcję 3
    sumMain = calculateSum(elements)

    #To jest główna funkcja wywołująca funkcję 4
    averageMain = calculateAverage(sumMain, numberOfElements)

    #To jest główna funkcja wywołująca funkcję 5
    standardDeviationMain = calculateStandardDeviation(elements, averageMain, numberOfElements)

    (numpyStd, numpyAvg) = numpyCalculation(elements)

    print('Średnia dla wprowadzonych liczb wynosi: {} natomiast odchylenie standardowe jest równe {} '.format(averageMain, standardDeviationMain))

    print('Numpy wyliczył, że średnia wynosi: {} natomiast odchylenie standardowe jest równe {} ' .format(numpyAvg, numpyStd))

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

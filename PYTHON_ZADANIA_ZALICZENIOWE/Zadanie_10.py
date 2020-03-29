# -*- coding: utf-8 -*-
'''
Autor: Sławomir Kranc

Treść zadania 10:
Utwórz skrypt z interfejsem tekstowym, który przyjmie od użytkownika ile elementów chce on wprowadzić do listy,przyjmie te elementy, a następnie wyliczy: średnią i odchylenie standardowe średniej. Wykonać zadanie na dwa sposoby: poprzez utworzenie funkcji własnych obliczających średnią i odchylenie standardowe oraz korzystając z gotowych funkcji np. z pakietu numpy
'''

import numpy as np

#To jest funkcja pobierająca od użytkownika ilość elementów do listy.
def setNumber():
  while True:
    try:
      n = int(input('Podaj ilość elementów do listy: '))
      return n
    except ValueError:
      print('Proszę wprowadzić liczbę: ')

#To jest funkcja przyjmująca od użytkownika elementy do listy.
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
    except ValueError:
      print('Proszę wprowadzić liczbę: ')

#To jest funkcja obliczająca sumę elementów z listy.
def calculateSum(myList):
  suma = 0
  for i in myList:
    suma += i
  return suma

#To jest funkcja obliczająca średnią z elementów listy.
def calculateAverage(suma, n):
  average = suma / n
  return average

#To jest funkcja obliczająca odchylenie standardowe z elementów listy i zaokrąglająca wynik do dwóch miejsc po przecinku.
def calculateStandardDeviation(myList, average, n):
  sd1 = 0
  for i in myList:
    temporary = ((i - average)**2)
    sd1 += temporary
  return round((sd1 / (n))**0.5, 2)

#To jest funkcja wykorzystująca pakiet numpy w celu obliczeń średniej i odchylenia standardowego.
def numpyCalculation(myList):
  myArray = np.array(myList)
  myStd = np.std(myArray)
  myAvg = np.average(myArray)
  return myStd, myAvg

def main():

  print('---------------------------------------------------------------------------------------------')
  print('To jest program, który przyjmumje od użytkownika ile elementów chce on wprowadzić do listy, przyjmuje te elementy, a następnie liczy: średnią i odchylenie standardowe średniej. ')
  print('---------------------------------------------------------------------------------------------')

  while True:

    numberOfElements = setNumber()

    elements = getElementToList(numberOfElements)

    sumMain = calculateSum(elements)

    averageMain = calculateAverage(sumMain, numberOfElements)

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
        print('Proszę podjąć decyzję! (t/n)')

if __name__ == "__main__":
  main()

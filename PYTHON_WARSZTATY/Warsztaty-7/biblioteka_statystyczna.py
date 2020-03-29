# -*- coding: utf-8 -*-

#Autor: slawomir.kranc

('---------------------------------')
('To jest biblioteka statystyczna. ')
('---------------------------------')


import numpy as np
from collections import Counter


def iloscElementow():
  while True:
    try:
      n = int(input('Podaj ilość elementów do listy: '))
      return n
    except ValueError:
      print('Proszę wprowadzić liczbę: ')

def elementyListy(n):
      myList = []
      for i in range(n):
        while True:
          try:
            element = float(input('Podaj element {}: '.format(i+1)))
            myList.append(element)
            break
          except ValueError:
            print('Proszę wprowadzić liczbę: ')
      return myList
  
def elementyListy1(n):
      myList1 = []
      for i in range(n):
        while True:
          try:
            element = float(input('Podaj element {}: '.format(i+1)))
            myList1.append(element)
            break
          except ValueError:
            print('Proszę wprowadzić liczbę: ')
      return myList1

def elementyListy2(n):
      myList2 = []
      for i in range(n):
        while True:
          try:
            element = float(input('Podaj element {}: '.format(i+1)))
            myList2.append(element)
            break
          except ValueError:
            print('Proszę wprowadzić liczbę: ')
      return myList2
  
def srednia(myList):
    return sum(myList)/len(myList)

def sredniaNumpy(myList):
  myArray = np.array(myList)
  myAvg = np.average(myArray)
  return myAvg
 
def mediana(myList):
    myList.sort()
    index = int(len(myList)/2)
    if (len(myList)%2 == 0):
        return (myList[index-1]+myList[index])/2
    else:
        return myList[index]
   
def dominanta(myList):
    c = Counter(myList)
    return c.most_common(1)[0][0]
 
def odchylenie(myList):
    return wariancja(myList)**0.5
    
def wariancja(myList):
    sre = srednia(myList)
    suma = 0
    for i in range(len(myList)-1):
        suma = suma + (myList[i] - sre)**2
    return suma/len(myList)
  
def skosnosc(myList):
    sre = srednia(myList)
    suma = 0
    for i in range(len(myList)-1):
        suma = suma + (myList[i] - sre)**3
    return (suma/len(myList))/odchylenie(myList)**3
 
def kurtoza(myList):
    sre = srednia(myList)
    suma = 0
    for i in range(len(myList)-1):
        suma = suma + (myList[i] - sre)**4
    return ((suma/len(myList))/odchylenie(myList)**4)-3

def kowariancja(myList1, myList2):
    myList3 = []
    for i in range(len(myList1)):
        iloczyn = myList1[i] * myList2[i]
        myList3.append(iloczyn)
        break 
    sredniaMyList1 = srednia(myList1)
    sredniaMyList2 = srednia(myList2)
    sredniaIloczyn = srednia(myList3) 
    iloczynWartosciOczekiwanej = sredniaMyList1 * sredniaMyList2
    return iloczynWartosciOczekiwanej - sredniaIloczyn

def korelacja(myList1, myList2):
    odchylenieList1 = odchylenie(myList1)
    odchyelenieList2 = odchylenie(myList2)
    iloczynOdchylen = odchylenieList1 * odchyelenieList2
    return kowariancja(myList1, myList2) / iloczynOdchylen

def regresja(myList1, myList2):
    myList3 = []
    myList4 = []
    myList5 = []
    myList6 = []
    for i in range(len(myList1)):
        element1 = myList1[i] - srednia(myList1)
        myList3.append(element1)
        break
    for i in range(len(myList2)):
        element2 = myList2[i] - srednia(myList2)
        myList4.append(element2)
        break
    for i in range(len(myList1)):
        element3 = (myList2[i] - srednia(myList2)) * (myList1[i] - srednia(myList1))
        myList5.append(element3)
        break
    for i in range(len(myList2)):
        element4 = (myList2[i] - srednia(myList2))**2
        myList6.append(element4)
        
    sumaElement3 = suma(myList5)
    sumaElement4 = suma(myList6)
    
    b1 = sumaElement3 / sumaElement4
    a = srednia(myList1) - (b1 * srednia(myList2))
    

    
    
    




        
    

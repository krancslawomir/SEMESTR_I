# -*- coding: utf-8 -*-
'''
Autor: Sławomir Kranc

Treść projektu 3:
Utwórz klasę Vector3D. Wykorzystaj całą wiedzę jaką posiadasz na temat wektorów w przestrzeni. Zdefiniuj wszystkie znane Ci operacje.
'''

'''
Wektor z przestrzeni R1 oraz R2 zostanie zamieniony na wektor w przestrzeni R3 poprzez dodanie zera w miejscu brakującego wersora.
'''
#Tworzenie klasy Wektora przestrzeni R3.
#Sprawdzanie czy wersor każdego z wektorów jest liczbą całkowitą lub zmiennoprzecinkową.
class Vector3D:
    def __init__(self, a=0, b=0, c=0, *args, **kwargs):
        self.__flag = False
        try:
            assert isinstance(a,int) or isinstance(a, float)
            self.__a = a
            assert isinstance(b,int) or isinstance(b, float)
            self.__b = b
            assert isinstance(c,int) or isinstance(c, float)
            self.__c = c
            self.__flag = True

        except AssertionError:
            print('Błąd! Nieprawidłowy wektor!')

    #Zamiana znaków odnoszących się do miejsca przechowywania w pamięci operacyjnej na liczby zrozumiałe
    #dla człowieka.
    def __str__(self):
        if self.__flag:
            return f'({self.__a}, {self.__b}, {self.__c})'

    #Dodawanie wektorów w przestrzeni R3.
    def __add__(self, element):
        if self.__flag and isinstance(element, Vector3D):
            return Vector3D(self.__a + element.__a, self.__b + element.__b, self.__c + element.__c)

    #Odejmowanie wektorów w przestrzeni R3.
    def __sub__(self, element):
        if self.__flag and isinstance(element, Vector3D):
            return Vector3D(self.__a - element.__a, self.__b - element.__b, self.__c - element.__c)

    #Mnożenie wektora R3 przez liczbę z prawej strony.
    def __mul__(self, element):
        if self.__flag and (isinstance(element, int) or isinstance(element, float)):
            return Vector3D(element * self.__a,
                            element * self.__b,
                            element * self.__c)

        if self.__flag and isinstance(element, Vector3D):
            return Vector3D(self.__b * element.__c - self.__c * element.__b,
                            self.__c * element.__a - self.__a * element.__c,
                            self.__a * element.__b - self.__b * element.__a)


    #Mnożenie wektora R3 przez liczbę z lewej strony.
    def __rmul__(self, element):
        if self.__flag and (isinstance(element, int) or isinstance(element, float)):
            return Vector3D(element * self.__a,
                            element * self.__b,
                            element * self.__c)

    #Iloczyn skalarny (wykonywanie przez @)
    def __matmul__(self, vector):
        if self.__flag and isinstance(vector, Vector3D):
            return self.__a * vector.__a + self.__b * vector.__b + self.__c * vector.__c


    #Sprawdzanie równości wektorów.
    def __eq__(self, vector):
        if self.__flag and isinstance(vector, Vector3D):
            return self.__a == vector.__a and self.__b == vector.__b and  self.__c == vector.__c
        return False

    #Getter składowych wektora.
    def __getitem__(self,index):
        temp_item = [self.__a, self.__b, self.__c]

        try:
            assert isinstance(index,int) and -len(temp_item) <= index <= (len(temp_item) - 1)
            return temp_item[index]

        except AssertionError:
            print('Błąd!')

    #Długość wektora.
    def vector_length(self):
        if self.__flag:
            return (self.__a**2 + self.__b**2 + self.__c**2)**(1/2)


def main():
    a = Vector3D(1,2,3)
    b = Vector3D(4,5,6)
    c = Vector3D(7,8,9)
    z = Vector3D(10,11,12)

    print('Długość wektora a wynosi:')
    print(a.vector_length())

    print('Wynikiem dodawania wektorów a i b jest:')
    print(f'a+b={a + b}')

    print('Wynikiem odejmowania wektorów a i b jest:')
    print(f'a-b={a - b}')

    print('Wynikiem mnożenia wektora a i b jest:')
    print(f'a x b={a * b}')

    print('Wynikiem mnożenia wektora a przez liczbę 10 jest:')
    print(f'a x 3={a * 10}')
    print(f'3 x b={10 * b}')

    print('Wynikiem iloczynu skalarnego wektorów a i b jest :')
    print(f'a o b = {a @ b}')

    print('Wynikiem iloczynu mieszanego wektorów a, b, c jest :')
    print(f'c o (b x a) = {c @ (a*b)}')

if __name__ == '__main__':
    main()

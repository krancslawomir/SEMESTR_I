# -*- coding: utf-8 -*-
'''
Autor: Sławomir Kranc

Treść zadania 17:
Utwórz funkcję, która będzie generować listy danych do wykreślenia w oparciu o:
a) fukcję liniową ax+b
b) funkcję kwadratową ax^2+bx+c
c) funkcję odwrotnie-potęgową a/x^n
Każda z fukcji powinna przyjmować parametry równania, natomiast zwracać powinna dwie listy - x i y, które następnie będzie można wykreślić na wykresie
'''

from pylab import plot, title, xlabel, ylabel, legend, show, figure

def linear(a,b):
    x = list(range(-10,10))
    y = list(map(lambda x:a*x+b,x))
    return x,y

def quadratic(a,b,c):
    x = list(range(-10,10))
    y = list(map(lambda x:(a*x)**2+b*x+c,x))
    return x,y

def inverse_power(a,n):
    x = list(range(-10,10))
    x.remove(0)
    y = list(map(lambda x:a/(x**n),x))
    return x,y

def draw_linear(X,Y):
    figure(1)
    plot(X,Y, color='blue', marker='o', markersize='10', linewidth='2')
    xlabel('x', fontname='Times New Roman', fontsize=32, color='black')
    ylabel('f(x)=a*x+b', fontname='Times New Roman', fontsize=32, color='black')
    title('Funkcja linowa', fontname='Times New Roman', fontsize=48, color='black')
    legend(['f(x)=a*x+b'],loc='upper left', fontsize=20)

def draw_quadratic(X,Y):
    figure(2)
    plot(X,Y, color='red', marker='*', markersize='10', linewidth='2')
    xlabel('x', fontname='Times New Roman', fontsize=32, color='black')
    ylabel('f(x)=ax^2+bx+c', fontname='Times New Roman', fontsize=32, color='black')
    title('Funkcja kwadratowa', fontname='Times New Roman', fontsize=48, color='black')
    legend(['f(x)=ax^2+bx+c'],loc='upper left', fontsize=20)

def draw_inverse_power(X,Y):
    figure(3)
    plot(X,Y, color='green', marker='x', markersize='10', linewidth='2')
    xlabel('x', fontname='Times New Roman', fontsize=32, color='black')
    ylabel('f(x)=a/x^n', fontname='Times New Roman', fontsize=32, color='black')
    title('Funkcja odwrotnie potęgowa', fontname='Times New Roman', fontsize=48, color='black')
    legend(['f(x)=a/x^n'],loc='upper left', fontsize=20)

def main():
    W1 = 'y = ax+b'
    W2 = 'y = ax^2+bx+c'
    W3 = 'y = a/x^n'
    X,Y = linear(10,10)
    draw_linear(X,Y)
    print('\nW opraciu o funkcję liniową f = {} oraz dla podanych argumentów: \nx = {} \nwygenerowano następującą listę danych do wykreślenia: \ny = {}' .format(W1,X,Y))

    X,Y = quadratic(10,10,10)
    draw_quadratic(X,Y)
    print('\nW opraciu o funkcję liniową f = {} oraz dla podanych argumentów: \nx = {} \nwygenerowano następującą listę danych do wykreślenia: \ny = {}' .format(W2,X,Y))

    X,Y = inverse_power(10,10)
    draw_inverse_power(X,Y)
    print('\nW opraciu o funkcję liniową f = {} oraz dla podanych argumentów: \nx = {} \nwygenerowano następującą listę danych do wykreślenia: \ny = {}' .format(W3,X,Y))

    show()

if __name__ == '__main__':
    main()

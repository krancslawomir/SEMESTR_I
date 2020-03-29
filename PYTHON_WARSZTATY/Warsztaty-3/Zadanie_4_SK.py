# -*- coding: utf-8 -*-
#Autor Sławomir Kranc


from pylab import plot, title, xlabel, ylabel, legend, show, figure


def linear(a,b):
    x = list(range(-10,10))
    y = list(map(lambda x:a*x+b,x))
    output = ('x: {} \ny: {} ' .format (x,y))
    with open(r'D:\data_linear.txt','w') as file:
         file.write(output)
    return x,y



def quadratic(a,b,c):
    x = list(range(-10,10))
    y = list(map(lambda x:(a*x)**2+b*x+c,x))
    output = ('x: {} \ny: {} ' .format (x,y))
    with open(r'D:\data_quadratic.txt','w') as file:
         file.write(output)
    return x,y

def inverse_power(a,n):
    x = list(range(-10,10))
    x.remove(0)
    y = list(map(lambda x:a/(x**n),x))
    output = ('x: {} \ny: {} ' .format (x,y))
    with open(r'D:\data_inverse_power.txt','w') as file:
         file.write(output)
    return x,y


def main():
    X,Y = linear(10,10)

    X,Y = quadratic(10,10,10)

    X,Y = inverse_power(10,10)

if __name__ == '__main__':
    main()

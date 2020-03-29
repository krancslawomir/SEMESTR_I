# -*- coding: utf-8 -*-
# Autor: Sławomir Kranc

from pylab import plot, title, xlabel, ylabel, legend, show, figure
from collections import Counter
import numpy as np
import biblioteka_statystyczna as bs
import matplotlib.pyplot as plt

s = np.random.normal(mean, sigma, 1000)
p = np.random.normal(size=1000)

def rysuj_histogram(sigma, mean):
    figure(1)
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mean)**2 / (2 * sigma**2) ),linewidth=2, color='r')
    plt.show()


def rysuj_srednia(p):
    figure(2)
    plot(s, color='blue', marker='o', markersize='10', linewidth='2')
    xlabel('x', fontname='Times New Roman', fontsize=32, color='black')
    ylabel('f(x)=a*x+b', fontname='Times New Roman', fontsize=32, color='black')
    title('Funkcja linowa', fontname='Times New Roman', fontsize=48, color='black')
    legend(['f(x)=a*x+b'],loc='upper left', fontsize=20)
    grid()










def main():
    
    # sigma - odchylenie standardowe
    # mean - srednia   
    #rysuj_histogram(sigma, mean)
    #rysuj_srednia(p)
    print(p)
    print(type(p))

if __name__ == '__main__':
    main()
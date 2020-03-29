"""
# -*- coding: utf-8 -*-

Autor: Sławomir Kranc

Implementacja gry w życie Conway'a
Wersja zmodyfikowana przez: Sławomir Kranc

"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
probability = [0.2, 0.8]
'''N - Ustawianie rozmaru planszy. Plansza dostosowuje się do najpopularniejszych ekranów monitorów w proporcjach 16:9.'''
N = 100
M = int(N*(16/9))
vals = [ON, OFF]

def randomGrid():
    """Zwraca planszę N x M losowych wartości"""
    return np.random.choice(vals, N*M, p=probability).reshape(N, M)

def addGlider(i, j, grid):
    """Dodaje szybowiec z lewą górną komórką w (i,j)"""
    glider = np.array([[OFF, OFF, ON],
                       [ON, OFF, ON],
                       [OFF, ON, ON]])
    grid[i:i+3, j:j+3] = glider
    return grid

def addSquare(i, j, grid):
    """Dodaje kwadrat z lewą górną komórką w (i,j)"""
    square = np.array([[ON, ON],
                       [ON, ON]])
    grid[i:i+2, j:j+2] = square
    return grid

def addBeehive(i, j, grid):
    """Dodaje ul z lewą górną komórką w (i,j)"""
    beehive = np.array([[OFF, ON, ON, OFF],
                       [ON, OFF, OFF, ON],
                       [OFF, ON, ON, OFF]])
    grid[i:i+3, j:j+4] = beehive
    return grid

def addLoaf(i, j, grid):
    """Dodaje bochenek z lewą górną komórką w (i,j)"""
    loaf = np.array([[OFF, ON, ON, OFF],
                     [ON, OFF, OFF, ON],
                     [OFF, ON, OFF, ON],
                     [OFF, OFF, ON, OFF]])
    grid[i:i+4, j:j+4] = loaf
    return grid

def addFlower(i, j, grid):
    """Dodaje kwiatek z lewą górną komórką w (i,j)"""
    flower = np.array([[OFF, ON, OFF],
                    [ON, OFF, ON],
                    [ON, OFF, ON]])
    grid[i:i+3, j:j+3] = flower
    return grid

def addBlinker(i, j, grid):
    """Dodaje sygnalizator z lewą górną komórką w (i,j)"""
    blinker = np.array([[ON],
                        [ON],
                        [ON]])
    grid[i:i+3, j:j+1] = blinker
    return grid

def addBeacon(i, j, grid):
    """Dodaje nadajnik z lewą górną komórką w (i,j)"""
    beacon = np.array([[ON, ON, OFF, OFF],
                       [ON, ON, OFF, OFF],
                       [OFF, OFF, ON, ON],
                       [OFF, OFF, ON, ON]])
    grid[i:i+4, j:j+4] = beacon
    return grid

def addToad(i, j, grid):
    """Dodaje nadajnik z lewą górną komórką w (i,j)"""
    toad = np.array([[OFF, OFF, ON, OFF],
                     [ON, ON, ON, ON],
                     [ON, ON, ON, ON],
                     [OFF, ON, OFF, OFF]])
    grid[i:i+4, j:j+4] = toad
    return grid

def addBoat(i, j, grid):
    """Dodaje łódkę z lewą górną komórką w (i,j)"""
    boat = np.array([[ON, ON, OFF],
                     [ON, OFF, ON],
                     [OFF, ON, OFF]])
    grid[i:i+3, j:j+3] = boat
    return grid

def addBrick(i, j, grid):
    """Dodaje cegłe z lewą górną komórką w (i,j)"""
    boat = np.array([[OFF, OFF, OFF],
                     [ON, ON, ON],
                     [ON, ON, ON]])
    grid[i:i+3, j:j+3] = boat
    return grid



def update(frameNum, img, grid):
    '''Kopiowanie planszy, ponieważ potrzebujemy 8 sąsiadów do obliczeń. Idziemy linia po linii.'''
    newGrid = grid.copy()
    for i in range(N):
        for j in range(M):
            '''Obliczanie sumy dla 8 sąsiadów przy użyciu toroidalnych warunków brzegowych - x i y są zawijane, aby symulacja odbywała się na powierzchni toroidalnej.'''
            total = int((grid[i, (j-1)%M] + grid[i, (j+1)%M] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%M] + grid[(i-1)%N, (j+1)%M] +
                         grid[(i+1)%N, (j-1)%M] + grid[(i+1)%N, (j+1)%M])/255)
            '''Zastosowanie reguł Conwaya.'''
            if grid[i, j]  == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    '''Aktualizacja danych.'''
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,


def main():

    global ani

    '''Ustawianie interwału aktualizacji animacji.'''
    updateInterval = 60

    '''Deklarowanie planszy.'''
    grid = np.array([])

    grid = randomGrid()
    grid = addGlider(5, 5, grid)
    grid = addSquare(10, 10, grid)
    grid = addBeehive(15, 15, grid)
    grid = addLoaf(20, 20, grid)
    grid = addFlower(25, 25, grid)
    grid = addBlinker(30, 30, grid)
    grid = addBeacon(35, 35, grid)
    grid = addToad(40, 40, grid)
    grid = addBoat(50, 50, grid)
    grid = addBrick(60, 60, grid)

    '''Konfigurowanie animacji.'''
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, ),
                                  frames = 60,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()


if __name__ == '__main__':
    main()

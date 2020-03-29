
# -*- coding: utf-8 -*-

# Autor: Sławomir Kranc

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


ON = 255
OFF = 0
probability = [0.1, 0.9]
N = 55
M = 55
vals = [ON, OFF]

### ZADANIE 1 ###
def randomGrid():
    """Zwraca planszę N x M losowych wartości"""
    return np.random.choice(vals, N*M, p=probability).reshape(N, M)

#### ZADANIE 2 ###
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

def addSquare(i, j, grid):
    """Dodaje blok z lewą górną komórką w (i,j)"""
    square = np.array([[ON, ON],
                       [ON, ON]])
    grid[i:i+2, j:j+2] = square
    return grid

def addBlinker(i, j, grid):
    """Dodaje sygnalizator z lewą górną komórką w (i,j)"""
    blinker = np.array([[ON],
                        [ON],
                        [ON]])
    grid[i:i+3, j:j+1] = blinker
    return grid

def addBoat(i, j, grid):
    """Dodaje łódkę z lewą górną komórką w (i,j)"""
    boat = np.array([[ON, ON, OFF],
                     [ON, OFF, ON],
                     [OFF, ON, OFF]])
    grid[i:i+3, j:j+3] = boat
    return grid


def addFrog(i, j, grid):
    """Dodaje żabę z lewą górną komórką w (i,j)"""
    frog = np.array([[OFF, ON, OFF, OFF],
                     [OFF, ON, ON, OFF],
                     [OFF, ON, ON, OFF],
                     [OFF, OFF, ON, OFF]])
    grid[i:i+4, j:j+4] = frog
    return grid

def addLightHouse(i, j, grid):
    """Dodaje latarnię morską z lewą górną komórką w (i,j)"""
    lightHouse = np.array([[OFF, OFF, ON, OFF, OFF],
                     [OFF, ON, OFF, ON, OFF],
                     [ON, OFF, ON, OFF, ON],
                     [OFF, ON, OFF, ON, OFF],
                     [OFF, OFF, ON, OFF, OFF],
                     [OFF, OFF, ON, OFF, OFF],
                     [OFF, OFF, ON, OFF, OFF],
                     [OFF, OFF, ON, OFF, OFF]])
    grid[i:i+8, j:j+5] = lightHouse
    return grid


def update(frameNum, img, grid):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(M):

            ### ZADANIE 3 ###
            total = int((grid[i, (j-1)%M] + grid[i, (j+1)%M] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%M] + grid[(i-1)%N, (j+1)%M] +
                         grid[(i+1)%N, (j-1)%M] + grid[(i+1)%N, (j+1)%M])/255)
            
            ###ZADANIE 4 ###
            if grid[i, j]  == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

def main():

    global ani

    updateInterval = 60


    grid = np.array([])

    grid = randomGrid()

    grid = addBoat(1, 1, grid)
    grid = addSquare(7, 7, grid)
    grid = addBeehive(14, 14, grid)
    grid = addLoaf(21, 21, grid)
    grid = addBlinker(28, 28, grid)
    grid = addFrog(35, 35, grid)
    grid = addLightHouse(40, 40, grid)


    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, ),
                                  frames = 60,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()

    ### ZADANIE 5 ###
    for i in range (0,5):
        plt.savefig('D:\image'+str(i+1)+'.png')
        time.sleep(2)


if __name__ == '__main__':
    main()
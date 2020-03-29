# -*- coding: utf-8 -*-
'''
Autor: Sławomir Kranc

Treść zadania 33:
Utwórz funkcję zależną od numeru wiersza i kolumny macierzy (i, j), która będzie obliczać liczbę "żywych" komórek sąsiadujących względem komórki (i, j).
'''

N = 50
M = 50

#To jest funkcja obliczająca liczbę "żywych" komórek sąsiadujących względem komórki (i,j).
def update(grid):
  for i in range(N):
    for j in range(M):
      total = int((grid[i, (j-1)%M] + grid[i, (j+1)%M] +
                    grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                    grid[(i-1)%N, (j-1)%M] + grid[(i-1)%N, (j+1)%M] +
                    grid[(i+1)%N, (j-1)%M] + grid[(i+1)%N, (j+1)%M])/255)
  return total

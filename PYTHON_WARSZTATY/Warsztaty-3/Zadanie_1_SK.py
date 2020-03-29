# -*- coding: utf-8 -*-
"""
Autor: Sławomir Kranc

1. Utwórz skrypt, w którym zamieścisz 3 listy danych, zawierające po 14 temperatur dla 3 wybranych miast na kolejne 14 dni,
oraz utwórz wykres z tych danych. Twój wykres powinien mieć 3 linie z zaznaczonymi punktami danych za pomocą
różnych znaczników, tytuł, opisane osie oraz legendę.

"""

from pylab import plot, title, xlabel, ylabel, legend, xticks, yticks

#Dane pogodowe od dnia 09.12.2019 do 23.12.2019 pochodządze ze stony pogoda.interia.pl
konin    = [8, 5, 3, 3, 5, 2, 1, 2, 5, 5, 4, 4, 1, 1]
szczecin = [7, 6, 5, 5, 4, 6, 6, 6, 6, 5, 5, 5, 3,3 ]
katowice = [8, 4, 3, 2, 5, 4, 5, 5, 6, 6, 5, 4, 1, 1]


print(len(konin))
print(len(szczecin))
print(len(katowice))
plot(konin, color='blue', marker='o', markersize='10', linewidth='3')
plot(szczecin, color='red', marker='*', markersize='10', linewidth='3')
plot(katowice, color='green', marker='^', markersize='10', linewidth='3')


title('Prognoza pogody\n14 dniowa',
      fontname='Times New Roman',
      fontsize=24,
      color = 'black')

xlabel('Grudzień 2019', 
       fontname="Times New Roman",
       fontsize=16,
       color='black')

#Wyświetlanie konkretnych dni miesiąca"
dni = ['9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']

xticks(range(len(dni)), dni, fontsize='medium')
       
ylabel('Temperatura',
       fontname="Times New Roman",
       fontsize=16,
       color='black',)

       
legend(['Konin','Szczecin','Katowice',])
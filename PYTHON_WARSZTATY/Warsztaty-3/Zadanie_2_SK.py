"""
Autor: Sławomir Kranc

2. Utwórz funkcję własną, która jako argument przyjmować będzie listę argumentów i wartości, a jako wynik będzie wyświetlać 
sformatowany wykres (stosowny zakres, opis, kolory, legenda).

"""

from pylab import plot, title, xlabel, ylabel, legend, xticks, yticks

#[Funkcja 1]To jest funkcja przyjmująca od użytkownika elementy do listy dla osi X
def get_element_to_list_axis_x():
  myList = []
  decyzja1 = input('Czy chcesz podać argument X ? (t/n): ')
  while decyzja1 == 't':
    element = int(input('Podaj argument: '))
    myList.append(element)
    decyzja2 = input('Czy chcesz podać kolejny argument? (t/n): ')
    if decyzja2 == 't':
      continue
    elif decyzja2 == 'n':  
      return myList
  
#[Funkcja 2]To jest funkcja przyjmująca od użytkownika elementy do listy dla osi Y
def get_element_to_list_axis_y():
  myList = []
  decyzja1 = input('Czy chcesz podać argument Y ? (t/n): ')
  while decyzja1 == 't':
    element = int(input('Podaj argument: '))
    myList.append(element)
    decyzja2 = input('Czy chcesz podać kolejny argument? (t/n): ')
    if decyzja2 == 't':
      continue
    elif decyzja2 == 'n':  
      return myList


def main():

    #To jest główna funkcja wywołująca funkcję 2
    elements_x = get_element_to_list_axis_x()
    elements_y = get_element_to_list_axis_y()
    print(elements_x)
    print(elements_y)


    plot(elements_x, color='blue', marker='o', markersize='10', linewidth='3')
    plot(elements_y, color='red', marker='*', markersize='10', linewidth='3')
    
    
    title('Postać graficzna wybranych argumentów',
          fontname='Times New Roman',
          fontsize=24,
          color = 'black')
    
    xlabel('Numer kolejno wpisanego argumentu', 
           fontname="Times New Roman",
           fontsize=16,
           color='black')

    ylabel('Wartość podanego argumentu',
           fontname="Times New Roman",
           fontsize=16,
           color='black')
    

    legend(['punkty x','punkty y'])
    


if __name__ == "__main__":

  main()
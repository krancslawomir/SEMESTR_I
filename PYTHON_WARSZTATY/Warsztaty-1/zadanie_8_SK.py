#Autor: Sławomir Kranc

def main():
    while True:
      klawisz = input('Naciśnij przycisk s aby opuścić program:   ')
      if  klawisz == 's':
        print('Udało Ci się!')
        exit()
      else:
        print('Wprowadzono błędny klawisz, spróbuj ponownie :)')

if __name__ == "__main__":

  main()

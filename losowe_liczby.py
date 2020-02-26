import random
    
try:
    start = input('Podaj początek zakresu:')
    start = int(start)

    stop = input('Podaj koniec zakresu:')
    stop = int(stop)

    lenght = input('Podaj ile liczb chcesz wylosować:')
    lenght = int(lenght)

    def random_nums(x, y, z):
        lista = [] 
        for i in range(z):    
            random_number = random.randint(x,y)
            lista.append(random_number)
        return lista

    result = random_nums(start, stop, lenght)
    print(result)

except ValueError:
    print ("Źle podałeś dane! Dane muszą być liczbami całkowitymi!")

finally:
    if start == "" or stop == "" or lenght =="":
        print ("Wypełnij WSZYSTKIE pola! Musimy wiedzieć co chcesz zrobić ;)")
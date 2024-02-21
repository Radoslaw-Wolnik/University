import matplotlib.pyplot as plt
from random import choice
import time

def create_plt(sorting_algorytm):
    '''jako algorytm funkcji przekazywana jest odpowiednia funkcja sortujaca'''
    N = [10, 100, 300, 500, 700]
    # N =[2,3,4,10]

    tries = 10
    optymistic_plt = []
    pesymistic_plt = []
    average_plt = []

    for lenght in N:

        optymistyczny = [el for el in range(lenght)]
        pesymistyczny = [lenght - el - 1 for el in range(lenght)]
        sredni = [choice(optymistyczny) for _ in range(lenght)]

        optymistic_avr = 0
        pesymistic_avr = 0
        average_avr = 0
        for _ in range(tries):
            start = time.time()
            sorting_algorytm(optymistyczny)
            end = time.time()
            optymistic_avr += end - start

            start = time.time()
            sorting_algorytm(pesymistyczny)
            end = time.time()
            pesymistic_avr += end - start

            start = time.time()
            sorting_algorytm(sredni)
            end = time.time()
            average_avr += end - start

        optymistic_plt.append(optymistic_avr / tries)
        pesymistic_plt.append(pesymistic_avr / tries)
        average_plt.append(average_avr / tries)

    plt.figure(figsize=(8, 5))
    plt.plot(N, optymistic_plt, '-', color='skyblue', label='optymistyczna sytuacja')
    plt.plot(N, pesymistic_plt, '-', color='crimson', label='pesymistyczna sytuacja')
    plt.plot(N, average_plt, '-', color='green', label='srednia sytuacja')
    plt.legend(bbox_to_anchor=(1.04, 0.5), loc='center left', shadow=True, fontsize='x-large')
    plt.xlabel('dlugosc listy')
    plt.ylabel('czas [s]')
    plt.title(sorting_algorytm.__name__)
    plt.show()


create_plt(wstawienie_sort)
create_plt(wstawienie_sort_while)
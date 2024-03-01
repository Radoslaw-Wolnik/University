import matplotlib.pyplot as plt
from random import choice
import time

from src.plot.BubbleSort import BubbleSort


def create_plt(sorting_algorythm):
    '''jako algorytm funkcji przekazywana jest odpowiednia funkcja sortujaca'''
    n = [10, 100, 300, 500, 700]
    # small_n =[2,3,4,10]

    tries = 10
    optimistic_plt = []
    pessimistic_plt = []
    average_plt = []

    for length in n:

        optimistic_data = [el for el in range(length)]
        pessimistic_data = [length - el - 1 for el in range(length)]
        average_data = [choice(optimistic_data) for _ in range(length)]

        optimistic_avr = 0
        pessimistic_avr = 0
        average_avr = 0
        for _ in range(tries):

            sorting_algorythm.load_data(optimistic_data)
            start = time.time()
            sorting_algorythm.execute()
            end = time.time()
            optimistic_avr += end - start

            sorting_algorythm.load_data(pessimistic_data)
            start = time.time()
            sorting_algorythm.execute()
            end = time.time()
            pessimistic_avr += end - start

            sorting_algorythm.load_data(average_data)
            start = time.time()
            sorting_algorythm.execute()
            end = time.time()
            average_avr += end - start

        optimistic_plt.append(optimistic_avr / tries)
        pessimistic_plt.append(pessimistic_avr / tries)
        average_plt.append(average_avr / tries)

    plt.figure(figsize=(8, 5))
    plt.plot(n, optimistic_plt, '-', color='skyblue', label='optimistic situation')
    plt.plot(n, pessimistic_plt, '-', color='crimson', label='pessimistic situation')
    plt.plot(n, average_plt, '-', color='green', label='average situation')
    plt.legend(bbox_to_anchor=(1.04, 0.5), loc='center left', shadow=True, fontsize='x-large')
    plt.xlabel('length of list')
    plt.ylabel('time [s]')
    plt.title(type(sorting_algorythm).__name__)
    plt.show()


if __name__ == '__main__':
    bubble = BubbleSort()
    create_plt(bubble)
    # plot legend not in graphic fix it
    # create_plt() - in different file - project structure
    # not sure if merge sort is correct in case of heritage because it hase 2 more functions then sort interface
    # insertion sort should be good though
    # https://realpython.com/python-interface/

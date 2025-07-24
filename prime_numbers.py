import time
import math


def time_measuring(other_fun, num):
    start_time = time.perf_counter()
    other_fun(num)
    end_time = time.perf_counter()
    return end_time - start_time


def check(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            print("To nie jest liczba pierwsza")
            break
        if i == int(math.sqrt(number)):
            print("To jest liczba pierwsza")


while True:
    try:
        user_number = int(input("Podaj liczbę do sprawdzenia: "))
        print(
            f"Czas wykonania działania to: {time_measuring(check, user_number)} sekundy."
        )
        break
    except ValueError:
        print("To nie jest liczba!")

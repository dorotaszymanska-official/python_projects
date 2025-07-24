import random

point_guessing_tries = 5

point_x = random.randint(1, 10)
point_y = random.randint(1, 10)

try:
    for i in range(0, 6):
        user_x = int(input("Podaj współrzędną na osi x w zakresie od 1-10:\n"))
        user_y = int(input("Podaj współrzędną na osi y w zakresie od 1-10:\n"))
        if not user_x in range(1, 10) or not user_y in range(1, 10):
            print("Liczba spoza zakresu")
            break
        if user_x == point_x or user_y == point_y:
            print("Wygrana")
            break
        elif user_x in range(point_x - 2, point_x + 2) or user_y in range(
            point_y - 2, point_y + 2
        ):
            print("Blisko...")
        else:
            print("Daleko...")
    print("Koniec gry")
except ValueError:
    print("Podaj liczbę nie literę")

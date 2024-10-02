"""
Szukanie binarne
"""

"""
Przykład 1
Napisz algorytm w postaci pseudokodu, który zwróci Prawda lub Fałsz w zależności od tego, czy liczba a należy do uporządkowanej niemalejąco tablicy T[0..n-1], czy nie należy.
Specyfikacja:
Dane:
a – liczba całkowita
n – liczba całkowita dodatnia n oznaczającą liczbę elementów w tablicy T
T[0..n-1] – tablica zawierająca n liczb całkowitych uporządkowanych niemalejąco
Wyniki:
Wartość Prawda, gdy a należy do tablicy T, Fałsz w przeciwnym przypadku
"""


def binarySearch(T: list, a: int) -> bool:
    n = len(T)
    left = 0
    right = n - 1
    while left < right:
        middle = (left + right) // 2
        if T[middle] < a:
            left = middle + 1
        else:
            right = middle
    return T[left] == a


"""
Zadanie 1.
Napisz program, który wczytuje ze standardowego wejścia ciąg 10 uporządkowanych niemalejąco liczb całkowitych t[0..9].
Następnie program zapyta o liczbę całkowitą a i wyświetli na standardowym wyjściu tekst „tak”, gdy liczba a znajduje się wśród liczb t[0..9] oraz tekst „nie” w przeciwnym przypadku.
Wykorzystaj wyszukiwanie binarne w wersji iteracyjnej.
W przypadku podania przez użytkownika ciągu, który nie jest uporządkowany niemalejąco program wyświetli komunikat „Ciąg musi być uporządkowany niemalejąco”.
"""


def giveFromUserInts() -> list:
    i = 0
    ints = list()
    while i < 10:
        userInput = int(input(f"Podaj {i+1} liczbe: "))
        if len(ints) == 0:
            ints.append(userInput)
            i += 1
        elif ints[i - 1] < userInput:
            ints.append(userInput)
            i += 1
        else:
            print("Ciąg musi być uporządkowany niemalejąco")
    return ints


a = int(input("Zadanie 1: Podaj a:"))
if binarySearch(giveFromUserInts(), a):
    print("tak")
else:
    print("nie")
"""
Zadanie 2.
Wykonaj zadanie 1 wykorzystując wyszukiwanie binarne w wersji rekurencyjnej.
"""
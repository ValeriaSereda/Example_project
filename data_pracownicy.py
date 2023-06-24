import csv

pracownicy = [
    {"first_name": "Jan", "last_name": "Kowalski", "salary": 3500},
    {"first_name": "Tomasz", "last_name": "Torpeda", "salary": 3450.553},
    {"first_name": "Alicja", "last_name": "Kłopek", "salary": 8700.45},
    {"first_name": "Tina", "last_name": "Ficek", "salary": 4500.55},
    {"first_name": "Aleks", "last_name": "Szczotka", "salary": 8500}
]

naglowki = ["first_name", "last_name", "salary"]

with open("data_pracownicy.csv", "w", newline="", encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=naglowki)
    writer.writeheader()
    writer.writerows(pracownicy)

print("Dane zostały zapisane do pliku CSV: data_pracownicy.csv")
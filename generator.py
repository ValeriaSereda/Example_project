import csv
import random

first_names = ["Adam", "Bartosz", "Cecylia", "Dionizy", "Emil", "Franek", "Grażyna", "Halina", "Ingrid", "Janusz"]
last_names = ["Ziółko", "Yeti", "Xenon", "Więcek", "Vendetta", "Ulubieniec", "Tauryna", "Szczaniec", "Rydzyk", "Pałka"]

with open("pracownicy.csv", "w", encoding="UTF8", newline="") as file:
  writer = csv.writer(file)
  writer.writerow(["first_name", "last_name", "salary"])
  for i in range(100):
    writer.writerow([first_names[random.randint(0, 9)], last_names[random.randint(0, 9)], random.randint(1e3, 1e4)])

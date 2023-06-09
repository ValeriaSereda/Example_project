import csv

class Pracownik:
  def __init__(self, first_name, last_name, salary):
    self.first_name = first_name
    self.last_name = last_name
    self.salary = salary 

  def __str__(self):
    return self.first_name + ' ' + self.last_name + ',' + ' ' + str (self.salary)

  def oblicz_netto(self):
    skladka_emeryt = self.salary * 0.0976
    skladka_rentowa = self.salary * 0.015
    skladka_ubezp_chor = self.salary * 0.0245
    podstawa_na_zdrowotne = self.salary - skladka_emeryt - skladka_rentowa - skladka_ubezp_chor

    skladka_zdrowotna = podstawa_na_zdrowotne * 0.09

    podstawa_na_dochodowy = round(podstawa_na_zdrowotne - 250, 0)
    zaliczka_na_dochodowy = 0.12 * podstawa_na_dochodowy - 300
    
    return round(podstawa_na_zdrowotne - skladka_zdrowotna - zaliczka_na_dochodowy, 2)
  
  def koszty_pracodawcy(self) -> float:
    skladka_emerytalna = self.salary * 0.0976
    skladka_rentowa = self.salary * 0.065
    skladka_na_ubezpieczenie_wypadkowe = self.salary * 0.0167
    skladka_na_Fundusz_pracy = self.salary * 0.0245
    skladka_na_Fund_Gwar_Swiad_Prac = self.salary * 0.001
    laczne_skladki_na_ubezp_spol = skladka_emerytalna + skladka_na_Fund_Gwar_Swiad_Prac + skladka_na_Fundusz_pracy + skladka_na_ubezpieczenie_wypadkowe + skladka_rentowa
    koszty_pracodawcy = self.salary + laczne_skladki_na_ubezp_spol 
    return round (koszty_pracodawcy, 2) 
  
  def wygeneruj_raport(self):
    skladka_emeryt = self.salary * 0.0976
    skladka_rentowa = self.salary * 0.015
    skladka_ubezp_chor = self.salary * 0.0245
    podstawa_na_zdrowotne = self.salary - skladka_emeryt - skladka_rentowa - skladka_ubezp_chor

    skladka_zdrowotna = podstawa_na_zdrowotne * 0.09

    podstawa_na_dochodowy = round(podstawa_na_zdrowotne - 250, 0)
    zaliczka_na_dochodowy = 0.12 * podstawa_na_dochodowy - 300
    
    print(f"Składka emerytalna: {round(skladka_emeryt, 2)}")
    print(f"Składka rentowa: {round(skladka_rentowa, 2)}")
    print(f"Składka na ubezpieczenie chorobowe: {round(skladka_ubezp_chor, 2)}")
    print(f"Składka na ubezpieczenie zdrowotne: {round(skladka_zdrowotna, 2)}")
    print("=====================")
    print(f"Kwota wynagrodzenia: {round(podstawa_na_zdrowotne - skladka_zdrowotna - zaliczka_na_dochodowy, 2)}")

pracownicy = []  

import csv
with open('data_pracownicy.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file) 
    for row in reader:
        first_name = row['first_name']
        last_name = row['last_name']
        salary = float(row['salary'])
        
        pracownik = Pracownik(first_name, last_name, salary)
        pracownicy.append(pracownik)

for pracownik in pracownicy:
    print(pracownik)
    print("Koszty pracodawcy:", pracownik.koszty_pracodawcy())
    print()
class Pracownik:
  def __init__(self, first_name, last_name, salary):
    self.first_name = first_name
    self.last_name = last_name
    self.salary = salary

  def oblicz_netto(self):
    skladka_emeryt = self.salary * 0.0976
    skladka_rentowa = self.salary * 0.015
    skladka_ubezp_chor = self.salary * 0.0245
    podstawa_na_zdrowotne = self.salary - skladka_emeryt - skladka_rentowa - skladka_ubezp_chor

    skladka_zdrowotna = podstawa_na_zdrowotne * 0.09

    podstawa_na_dochodowy = round(podstawa_na_zdrowotne - 250, 0)
    zaliczka_na_dochodowy = 0.12 * podstawa_na_dochodowy - 300
    
    return round(podstawa_na_zdrowotne - skladka_zdrowotna - zaliczka_na_dochodowy, 2)

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

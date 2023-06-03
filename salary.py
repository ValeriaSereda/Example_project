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


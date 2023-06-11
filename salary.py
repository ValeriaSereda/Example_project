class Pracownik:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def __str__(self):
        return self.first_name + ',' + self.last_name + ',' + str(self.salary)
    
    def koszty_pracodawcy(self) -> float:
        skladka_emerytalna = self.salary * 0.0976
        skladka_rentowa = self.salary * 0.065
        skladka_na_ubezpieczenie_wypadkowe = self.salary * 0.0167
        skladka_na_Fundusz_pracy = self.salary * 0.0245
        skladka_na_Fund_Gwar_Swiad_Prac = self.salary * 0.001
        laczne_skladki_na_ubezp_spol = skladka_emerytalna + skladka_na_Fund_Gwar_Swiad_Prac + skladka_na_Fundusz_pracy + skladka_na_ubezpieczenie_wypadkowe + skladka_rentowa
        koszty_pracodawcy = self.salary + laczne_skladki_na_ubezp_spol 
        return (koszty_pracodawcy) 
        
Pracownik_1 = Pracownik('Jan', 'Kowalski',3500) 
Pracownik_2 = Pracownik('Tomasz', "Torpeda", 3450.553)

assert print(Pracownik_1) == "Jan Kowalski, 3500"
assert print(Pracownik_2) == "Tomasz Torpeda, 3450.55"
assert Pracownik_1.koszty_pracodawcy() == 4216.8
assert Pracownik_2.koszty_pracodawcy() == 4157.23

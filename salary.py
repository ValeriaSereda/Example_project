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
print (Pracownik_1)
koszty_pracodawcy_Pracownik_1 = Pracownik_1.koszty_pracodawcy()
print(f"Koszty pracodawcy dla pracownika 1 wynoszą: {koszty_pracodawcy_Pracownik_1:.2f}")

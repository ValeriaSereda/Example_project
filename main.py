# funkcja liczaca objetosc kuli 
def kula(r):
    pi = 3.14159265359
    ob_kula = 4/3*pi*(r**3)
    return ob_kula 
print (f'Obijetosc kuli wynosi: {kula(2)}')

assert kula(5) == 523.5987755983333
assert kula(3.4) == 164.63621020893513
assert kula(0) == 0
assert kula(-3) == -113.09733552924

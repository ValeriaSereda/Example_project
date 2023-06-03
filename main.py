# funkcja liczaca objetosc kuli 
def kula(r):
    if r < 0:
     return ("error: radius is negative")
    pi = 3.14159265359
    ob_kula = 4/3*pi*(r**3)
    return ob_kula 
print (f'Obijetosc kuli wynosi: {kula(2)}')

assert kula(5) == 523.5987755983333
assert kula(3.4) == 164.63621020893513
assert kula(0) == 0
assert kula(-3) == "error: radius is negative"

def cube_params(side: float):
  """This function computes and returns volume and area of a cube with a given side length."""

  if side < 0:
    return { "code error" }

  volume = side ** 3
  area = 6 * side ** 2
  return {
    "volume": volume,
    "area": area 
  }

assert cube_params (3) == { "volume": 27, "area": 54 }
assert cube_params (-1) == { "code error"}
assert cube_params (0.5) == { "volume": 0.125, "area": 1.5}
assert cube_params (10) == { "volume": 1000, "area": 600}
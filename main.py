# funkcja liczaca objetosc kuli 
def stozek(r,h):
    if r < 0:
     return ("error: radius is negative")
    if h < 0:
      return ("error: high is negative")
    pi = 3.14159265359
    ob_stozek = 1/3*pi*(r**2)*h
    return ob_stozek
print (f'Obijetosc stożka wynosi: {stozek(3,2)}')

assert stozek(5, 6) == 157.0796326795
assert stozek(3.4, 3.2) == 38.73793181386709
assert stozek(0, 3) == 0
assert stozek(3, -0.1) == "error: high is negative"

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
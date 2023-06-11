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

def pyramid_params(base_edge: float, side_height: float, height: float):
  """This function computes and returns volume and area of a four-sided regular pyramid with a given edges' lengths and height."""

  if base_edge < 0 or side_height < 0 or height < 0:
    return "error: one of the values is negative"
  
  # assuming four-sidedness
  base_area = base_edge ** 2
  side_area = base_edge * side_height / 2
  total_area = base_area + 4 * side_area

  volume = base_area * height / 3

  return {
    "volume": volume,
    "area": total_area
  }
assert pyramid_params (3, 2, 1.5) == { "volume": 4.5, "area": 21 }
assert pyramid_params (-1, 5, 4) ==  "error: one of the values is negative" 
assert pyramid_params (0,0,0) == { "volume": 0, "area": 0 }
assert pyramid_params (3,-1,5) == "error: one of the values is negative"
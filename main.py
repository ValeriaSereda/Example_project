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
def cube_params(side: float):
  """This function computes and returns volume and area of a cube with a given side length."""
  volume = side ** 3
  area = 6 * side ** 2

  return {
    "volume": volume,
    "area": area
  }

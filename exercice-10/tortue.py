class Tortue:
  def __init__(self, x, y):
    self._x = x
    self._y = y
    self._direction = None

  def walk(n: int):
    if self._direction is None:
      raise ValueError("La tortue a besoin d'une direction")
    self.x += int(self._direction[0] * n)
    self.y += int(self._direction[1] * n)

  def look_left():
    self._direction = (-1, 0)

  def look_right():
    self._direction = (1, 0)

  def look_down():
    self._direction = (0, 1)

  def look_up():
    self._direction = (0, -1)


class Tortue:
  def __init__(self, x: float = 0, y: float = 0):
    self.x = x
    self.y = y
    self._direction = None

  def walk(self, n: int) -> None:
    if self._direction is None: raise ValueError("La tortue a besoin d'une direction")
    self.x += int(self._direction[0] * n)
    self.y += int(self._direction[1] * n)

  def look_left(self) -> None:
    self._direction = (-1, 0)

  def look_right(self) -> None:
    self._direction = (1, 0)

  def look_down(self) -> None:
    self._direction = (0, 1)

  def look_up(self) -> None:
    self._direction = (0, -1)

  def teleport(self, x: float, y: float) -> None:
    self.x = x
    self.y = y

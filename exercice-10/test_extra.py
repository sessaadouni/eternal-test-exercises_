from tortue import Tortue

def test_diagonales():
  """La tortue a gagné des capacités !
  
  Elle peut se déplacer en diagonales et aussi
  marcher à rebours. Si par exemple elle regarde
  vers le bas et qu'elle marche d'une quantité
  négative de pas, elle monte vers le haut!

  Implémenter ces fonctionnalités.
  """
  t = Tortue(0, 0)
  t.look_down_right()
  t.walk(10)
  assert t.x == 10 and t.y == 10
  t.look_up()
  t.walk(10)
  assert t.x == 10 and t.y == 0
  t.look_down_left()
  t.walk(10)
  assert t.x == 0 and t.y == 10
  t.teleport(100, 100)
  t.look_up_right()
  t.walk(10)
  assert t.x == 110 and t.y == 90
  t.look_down_right()
  t.walk(10)
  assert t.x == 120 and t.y == 100
  t.look_down()
  t.walk(-100)
  assert t.x == 120 and t.y == 0

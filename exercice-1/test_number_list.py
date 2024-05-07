import pytest

def test_convert_to_integer() -> None:
  """
  test_number_list.py: écris une fonction satisfaisant tous ces tests
  - Teste la fonction convert_to_integer avec une liste d'entiers
  - Teste la fonction convert_to_integer avec une liste de chaînes de caractères
  - Teste la fonction convert_to_integer avec une liste de chaînes de caractères et d'entiers
  - Teste la fonction convert_to_integer avec une liste vide
  - Teste la fonction convert_to_integer avec une liste d'entiers et de chaînes de caractères et renvoie une liste d'entiers
  """
  from number_list import convert_to_integer
  
  assert convert_to_integer([]) == []
  assert convert_to_integer([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
  assert convert_to_integer(['1', '2', '3', '4', '5']) == [1, 2, 3, 4, 5]
  assert convert_to_integer(['1', 2, '3', 4, '5']) == [1, 2, 3, 4, 5]
  assert convert_to_integer([1, 2, 'a', 4, 5]) == [1, 2, 4, 5]
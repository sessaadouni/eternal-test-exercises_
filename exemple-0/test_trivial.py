"""test_trivial_tdd.py: écris une fonction satisfaisant tous ces tests"""

import random

def test_reponse():
    """test for reponse(question=xxx).

    Expected behavior:
    - when question is '*' (everything), the function must return the string '42'
    - when question is 'quoi', the function must return 'feur'
    - when question is anything else or is absent, the function must return 'non'
    """
    from trivial import reponse
    assert reponse(question='*') == '42'
    assert reponse(question='quoi') == 'feur'
    assert reponse() == 'non'
    assert reponse(random.randint(0, 999)) == 'non'
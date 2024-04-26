# ceci est la liste des premiers mots du toki pona
toki_pona_pu_vocabulary = [
    "a",
    "ala",
    "ale",
    "ali",
    "anpa",
    "ante",
    "awen",
    "en",
    "esun",
    "ijo",
    "ike",
    "ilo",
    "insa",
    "jaki",
    "jan",
    "jelo",
    "jo",
    "kala",
    "kalama",
    "kama",
    "kasi",
    "ken",
    "kepeken",
    "kili",
    "kin",
    "kiwen",
    "ko",
    "kon",
    "kule",
    "kulupu",
    "la",
    "lape",
    "laso",
    "lawa",
    "len",
    "lete",
    "li",
    "lili",
    "linja",
    "lipu",
    "loje",
    "lon",
    "luka",
    "lukin",
    "lupa",
    "ma",
    "mama",
    "mani",
    "meli",
    "mi",
    "mije",
    "moku",
    "moli",
    "monsi",
    "mu",
    "mun",
    "musi",
    "mute",
    "nanpa",
    "nasa",
    "nasin",
    "nena",
    "ni",
    "nimi",
    "o",
    "oko",
    "olin",
    "ona",
    "open",
    "pakala",
    "pali",
    "palisa",
    "pan",
    "pana",
    "pi",
    "pilin",
    "pimeja",
    "pini",
    "pipi",
    "poka",
    "poki",
    "pona",
    "sama",
    "seli",
    "selo",
    "seme",
    "sewi",
    "sijelo",
    "sike",
    "sin",
    "sina",
    "sinpin",
    "sitelen",
    "sona",
    "soweli",
    "suli",
    "suno",
    "supa",
    "suwi",
    "tan",
    "taso",
    "tawa",
    "telo",
    "tenpo",
    "toki",
    "tomo",
    "tu",
    "unpa",
    "uta",
    "utala",
    "walo",
    "wan",
    "waso",
    "wawa",
    "weka",
    "wile",
]


def is_valid_toki_pona_text(s: str):
    raise NotImplementedError()


def is_valid_toki_pona_word(s: str):
    """Le Toki Pona est une langue construite extrêmement simple, faite pour
     être prononçable par quiconque et ne pas avoir de pièges.

     On veut valider qu'un mot respecte les règles du Toki Pona que voici:

     - Les voyelles sont: a, e, i, o, u
     - Les consonnes sont: j, k, l, m, n, p, s, t, w
     - Une consonne est toujours suivie d'une voyelle ou de la lettre n
     - la lettre n peut être suivie d'une consonne
     - les suites de lettres "wo(n)", "wu(n)", "ti(n)", "ji(n)", ne sont pas autorisées (on remplace "ti(n)" par "si(n)")
         (car c'est ambigü à prononcer pour les locuteurs de différentes langues)
         -> "wuwojiti = interdit"
     - Les lettres ne sont jamais doublées (pas de double a, pas de double l...)
     - Les mots ne peuvent finir que par une voyelle ou par la lettre 'n'
     - les noms propres sont les seuls à prendre une majuscule. en particulier une phrase ne comporte pas de majuscules au début.
     - la ponctuation n'est pas importante
     - un nom propre est toujours précédé du mot "jan" qui signifie "personne".
         Exemple: "mi jan Mataka": je suis 'jan Mataka' (mon nom en toki pona)
         est valide et la bonne façon de se présenter

     Note: les lettres se prononcent toujours de la même façon qu'en français (ou en japonais plus exactement)
     à l'exception du "j" qui se prononce comme un y.
     Le u rime avec "mou", "pou", "roue"
     Le e rime avec "blé", "ouais", "mémé"
     Le a rime avec "tata"
     Le o rime avec "cachalot"
     Le i rime avec "papi", "riz", "otarie"

     Implémenter une fonction qui valide qu'un mot respecte les règles du
    Toki pona.

     http://lvogel.free.fr/tokipona/lecons.html
    """
    raise NotImplementedError()


def is_valid_toki_pona_name(s: str):
    """Vérifie qu'un nom en toki pona est valide"""
    split_words = s.split(" ")
    return (
        len(split_words) == 2
        and split_words[0] == "jan"
        and split_words[1] == split_words[1].capitalize()
        and is_valid_toki_pona_word(split_words[1].lower())
    )


def test_toki_pona_word():
    assert not is_valid_toki_pona_word("faka")
    assert is_valid_toki_pona_word("namako")  # "spécial", "particulier"
    assert not is_valid_toki_pona_word("salto")  # 'lt' -> invalide
    assert not is_valid_toki_pona_word("wuwojiti")  # les syllabes interdites
    for word in toki_pona_pu_vocabulary:
        # on teste tous les mots du vocabulaire de base
        assert is_valid_toki_pona_word(word)


def test_toki_pona_text():
    assert is_valid_toki_pona_text("mi jan Mataka")  # "je suis jan Mataka"
    assert is_valid_toki_pona_text(
        "mi kijetesantakalu pona"
    )  # je suis un gentil raton-laveur
    assert not is_valid_toki_pona_text("yo bonjour")
    assert not is_valid_toki_pona_text("transport control protocol")
    assert is_valid_toki_pona_text(  # un poème
        """
ona li wawa li lawa li tawa
ali la ona li ken awen ala
ona li mute li suli li lon
li kama e moli
li weka e kon
tenpo
li lili
e musi e mi
e ken pali ali pi jan pali ni
tenpo li moku e tenpo mi sona
mi wile e tenpo tan wile mi pona"""
    )
    assert not is_valid_toki_pona_word(
        "Mi wile e tenpo tan wile mi pona"
    )  # majuscule incorrecte


def test_toki_pona_name():
    assert is_valid_toki_pona_name("jan Mataka")
    assert not is_valid_toki_pona_name("jan Mataka")
    assert is_valid_toki_pona_name("jan Kijetesantakalu")  # veut dire jan Raton-Laveur

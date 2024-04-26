import art


def number2anybase(num: int, base: int) -> tuple[int]:
    """Tester cette fonction et décrire ses paramètres"""
    digits = []
    while num:
        digits.append(num % base)
        num //= base
    return reversed(digits)


class NumberDisplay:
    """Tester cette classe et documenter ce qu'elle fait"""
    TYPE_NUMBERS = {
        "16": "0123456789ABCDEF",
        "10": "0123456789",
        "secret": "OIZELVG#Bq",
    }

    def __init__(self, display_len: int = 4, code: str = "10"):
        self.display_len = display_len
        self.encoding = code

    def show_number(self, number: str, number_source_base: int):
        our_encoding = self.TYPE_NUMBERS[self.encoding]
        our_base = len(our_encoding)
        to_show = "".join(
            our_encoding[a]
            for a in number2anybase(int(number, base=number_source_base), our_base)
        ).rjust(self.display_len, our_encoding[0])
        art.tprint(to_show)



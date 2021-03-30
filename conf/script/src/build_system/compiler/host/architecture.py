import sys
from enum import IntFlag, unique


@unique
class Architecture(IntFlag):
    UNKNOWN = 0
    A_16 = 2 ** 4
    A_32 = 2 ** 5
    A_64 = 2 ** 6
    A_128 = 2 ** 7

    def arch_to_bit_name(self) -> str:
        return str(self.value) + 'bit'


def detect_arch() -> Architecture:
    exclusive_max_word = sys.maxsize + 1
    word_size = exclusive_max_word.bit_length()

    return Architecture(word_size)

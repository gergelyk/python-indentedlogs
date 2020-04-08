from typing import Iterable, Tuple

from indentedlogs.monitor import StackMonitor


def test_round_down1():
    data = """
    0 a
    1 abc
    2 abcde
    2 abcd
    """
    generic_test(data)


def test_round_down2():
    data = """
    0 a
    1 abc
    2 abcde
    1 ab
    """
    generic_test(data)


def test_equal():
    data = """
    0 a
    1 abc
    1 abc
    2 abcde
    2 abcd
    1 abc
    """
    generic_test(data)


def test_new_call():
    data = """
    0 a
    1 abc
    2 abcde
    1 ab
    2 abfgh
    """
    generic_test(data)


def test_alternative_call():
    data = """
    0 a
    1 abc
    2 abcde
    0 a
    1 afghijk
    1 afghij
    """
    generic_test(data)


def test_jump():
    data = """
    0 a
    1 abc
    2 abcde
    1 afghijk
    1 afghij
    """
    generic_test(data)


def generic_test(data: str) -> None:
    monitor = StackMonitor()
    levels, stacks = parse_data(data)
    for index, (level, stack) in enumerate(zip(levels, stacks)):
        assert monitor._get_level(stack) == level, f"Error in line {index}"


def parse_data(data: str) -> Tuple[Iterable[int], Iterable[str]]:
    lines = [line.strip().split() for line in data.strip().splitlines()]
    levels, stacks = zip(*lines)
    levels = tuple(map(int, levels))
    return levels, stacks

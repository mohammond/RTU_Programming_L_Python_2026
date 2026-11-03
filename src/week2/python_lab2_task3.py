"""
Lab 2.3 – Operator Frequency Counter

>>> count_operators("3 + 5 * (2 - 1) + 7 / 2")
{'+': 2, '-': 1, '*': 1, '/': 1, '(': 1, ')': 1}
>>> count_operators("2 ** 3 - -4")
{'+': 0, '-': 2, '*': 2, '/': 0, '(': 0, ')': 0}
>>> count_operators("")
{'+': 0, '-': 0, '*': 0, '/': 0, '(': 0, ')': 0}
"""

OPERATORS = ['+', '-', '*', '/', '(', ')']


def count_operators(expression: str) -> dict[str, int]:
    """Return a dict with the count of each operator in expression."""
    counts = {op: 0 for op in OPERATORS}

    for character in expression:
        if character in counts:
            counts[character] += 1

    return counts


if __name__ == "__main__":
    expression = input("Enter an arithmetic expression: ")
    result = count_operators(expression)
    print(f"Operator counts: {result}")
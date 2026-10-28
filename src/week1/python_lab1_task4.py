def count_characters(text: str) -> int:
    count = 0
    for character in text:
        if not character.isspace():
            count = count + 1
    return count


def count_words(text: str) -> int:
    return len(text.split())


def extract_numbers(text: str) -> list[int]:
    numbers = []

    for word in text.split():
        word = word.rstrip(".,!?;:")

        if word.isdigit():
            numbers.append(int(word))
        elif word.startswith("-") and word[1:].isdigit():
            numbers.append(int(word))

    return numbers


def analyze_text(text: str) -> dict:
    characters = count_characters(text)
    words = count_words(text)
    numbers = extract_numbers(text)
    total = sum(numbers)

    if len(numbers) == 0:
        average = 0.0
    else:
        average = total / len(numbers)

    return {
        "characters": characters,
        "words": words,
        "numbers": numbers,
        "sum": total,
        "average": average
    }


if __name__ == "__main__":
    text = input("Enter text: ")
    result = analyze_text(text)

    print(f"Characters (no spaces): {result['characters']}")
    print(f"Words: {result['words']}")
    print(f"Numbers: {result['numbers']}")
    print(f"Sum: {result['sum']}")
    print(f"Average: {result['average']:.2f}")
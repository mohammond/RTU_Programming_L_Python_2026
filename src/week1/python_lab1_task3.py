def analyze_sentence(text: str) -> tuple[int, int, bool]:
    characters = len(text)
    words = len(text.split())
    contains_python = "python" in text.lower()

    return characters, words, contains_python


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    characters, words, contains_python = analyze_sentence(text)

    print(f"Characters: {characters}")
    print(f"Words: {words}")
    print(f"Contains 'Python': {contains_python}")
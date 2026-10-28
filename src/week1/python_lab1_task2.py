def greet_user(name: str) -> str:
    name = name.strip()
    name = name.capitalize()

    if name == "":
        name = "Stranger"

    return f"Hello, {name}! Welcome to Python!"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet_user(name))
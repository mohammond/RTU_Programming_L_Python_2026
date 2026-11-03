"""
Lab 2.1 – Simple Datasets and Aggregates

>>> average([1, 2, 3, 4])
2.5
>>> average([])
0.0
>>> cities = {"Riga": 605000, "Daugavpils": 78000, "Liepaja": 67000}
>>> largest_city(cities)
('Riga', 605000)
>>> smallest_city(cities)
('Liepaja', 67000)
>>> total_population(cities)
750000
>>> largest_city({})
('', 0)
>>> smallest_city({})
('', 0)
>>> total_population({})
0
>>> largest_city({"A": 10, "B": 10})
('A', 10)
>>> smallest_city({"A": 10, "B": 10})
('A', 10)
"""


def average(values: list[float]) -> float:
    if len(values) == 0:
        return 0.0

    total = 0
    for value in values:
        total += value

    return total / len(values)


def largest_city(populations: dict[str, int]) -> tuple[str, int]:
    if len(populations) == 0:
        return ("", 0)

    largest_name = ""
    largest_population = 0
    first = True

    for city in populations:
        if first or populations[city] > largest_population:
            largest_name = city
            largest_population = populations[city]
            first = False

    return (largest_name, largest_population)


def smallest_city(populations: dict[str, int]) -> tuple[str, int]:
    if len(populations) == 0:
        return ("", 0)

    smallest_name = ""
    smallest_population = 0
    first = True

    for city in populations:
        if first or populations[city] < smallest_population:
            smallest_name = city
            smallest_population = populations[city]
            first = False

    return (smallest_name, smallest_population)


def total_population(populations: dict[str, int]) -> int:
    total = 0

    for city in populations:
        total += populations[city]

    return total


if __name__ == "__main__":
    temperatures = [3, 5, 4, 6, 2, 7, 3]

    city_population = {
        "Riga": 600000,
        "Daugavpils": 80000,
        "Liepaja": 70000,
        "Jelgava": 55000,
        "Valmiera": 25000
    }

    avg = average(temperatures)
    largest = largest_city(city_population)
    smallest = smallest_city(city_population)
    total = total_population(city_population)

    print(f"Average temperature: {avg:.1f}")
    print(f"Largest city: {largest[0]} - {largest[1]}")
    print(f"Smallest city: {smallest[0]} - {smallest[1]}")
    print(f"Total population: {total}")
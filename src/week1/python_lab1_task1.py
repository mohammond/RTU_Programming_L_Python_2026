import math


def circle_area(radius: float) -> float:
    return math.pi * radius * radius


if __name__ == "__main__":
    radius = float(input("Enter radius: "))
    area = circle_area(radius)
    print(f"Area of the circle: {area:.2f}")
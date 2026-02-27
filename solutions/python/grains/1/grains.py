def square(number: int) -> int:
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    square_value = 1
    for _ in range(1, number):
        square_value *= 2

    return square_value


def total() -> int:
    total_grains = 0
    for i in range(1, 65):
        total_grains += square(i)
    return total_grains


print(total())




"""
Add type hints to the functions below. 
"""

def filter_odd_numbers(numbers):
    """Filters odd numbers from a sequence of numbers."""
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result


def square_numbers(numbers):
    """Square numbers in a sequence."""
    result = []
    for num in numbers:
        result.append(num**2)
    return result


def count_chars(words):
    """Counts the number of characters in a sequence of words."""
    result = []
    for word in words:
        result.append(len(word))
    return result


def main():
    """Show some example uses of the above function"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_numbers = filter_odd_numbers(numbers=numbers)
    squared_even_numbers = square_numbers(even_numbers)
    print(f"{squared_even_numbers=}")

    words = ["apple", "banana", "cherry"]
    numb_chars = count_chars(words=words)
    print(f"{numb_chars=}")


if __name__ == "__main__":
    main()
    
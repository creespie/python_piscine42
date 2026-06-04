def input_temperature(temp_str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    input_str = input("Input data is: ")
    try:
        print(f"Temperature is now: {input_temperature(input_str)}")
    except ValueError:
        print(
            f"Caught input_temperature error: invalid literal "
            f"for int() with base 10: {input_str}"
        )


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")

def input_temperature(temp_str) -> int:
    if int(temp_str) < 0:
        raise ValueError("-50°C is too cold for plants (min 0°C)")
    elif int(temp_str) > 40:
        raise ValueError("100°C is too hot for plants (max 40°C)")
    else:
        return int(temp_str)


def test_temperature() -> None:
    input_str = input("Input data is: ")
    try:
        print(f"Temperature is now: {input_temperature(input_str)}")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print()
    test_temperature()
    print()
    test_temperature()
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")

def garden_operations(operation_number: int) -> int:
    if operation_number == 0:
        raise ValueError("invalid literal for int() with base 10: 'abc'")
    elif operation_number == 1:
        raise ZeroDivisionError("division by zero")
    elif operation_number == 2:
        raise FileNotFoundError(
            "[Errno 2] No such file or directory: '/non/existent/file'"
        )
    elif operation_number == 3:
        raise TypeError('can only concatenate str (not "int") to str')
    else:
        return operation_number


def test_error_typer(input: int) -> None:
    try:
        garden_operations(input)
        print("Operation completed successfully")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    test_error_typer(0)
    print("Testing operation 1...")
    test_error_typer(1)
    print("Testing operation 2...")
    test_error_typer(2)
    print("Testing operation 3...")
    test_error_typer(3)
    print("Testing operation 4...")
    test_error_typer(4)
    print("\nAll error types tested successfully!")

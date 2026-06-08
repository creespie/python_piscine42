def secure_archive(
        filename: str, option: str, to_write: str = "") -> tuple[bool, str]:
    try:   
        if option == "write":
            with open(filename, "w") as file:
                file.write(to_write)
                return(True, 'Content successfully written to file')
        elif option == "read":
            with open(filename) as file:
                return(True, file.read())
        else:
            raise ValueError('Option must be either "write" or "read".'
                                ' No other input is allowed')
    except Exception as e:
        return (False, str(e))


if __name__ == "__main__":
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("ciao", "read"))
    print("Using 'secure_archive' to read with a wrong flag:")
    print(secure_archive("ciao", "rea"))
    print("Using 'secure_archive' to read from a regular file")
    print(secure_archive("ancient_fragment.txt", "read"))
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("test.txt", "write", "ndemooo"))
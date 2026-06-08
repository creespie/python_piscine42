import sys


def reading() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        try:
            print("=== Cyber Archives Recovery ===")
            file = open(sys.argv[1])
            text = file.read().split("\n")
            print(f"Accessing file '{sys.argv[1]}'")
            print("---\n")
            for line in text:
                print(line)
            print("\n---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
        except Exception as e:
            file.close()
            print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    reading()

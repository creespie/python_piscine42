import sys
import typing

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
            file.close()
            print(f"File '{sys.argv[1]}' closed.\n")
            print("Transform data:")
            print("---\n")
            for line in text:
                print(f"{line}#")
            print("\n---")
            new_file = input("Enter new file name (or empty): ")
            if new_file is None:
                print("Not saving data")
            else:
                file = open(new_file, "w")
                print(f"Saving data to '{new_file}'")
                for line in text:
                    file.write(f"{line}#\n")
                print(f"Data saved in file '{new_file}'")
                file.close()

            
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        
if __name__ == "__main__":
    reading()
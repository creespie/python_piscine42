import math

def get_player_pos():
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coords = None
    while not coords:
        try:
            coords = tuple(float(n) for n in input("Enter new coordinates as floats in format 'x,y,z': ").split(","))
        except:
            print("Invalid syntax")
    print(f"Got a first tuple: {coords}")
    print(f"It includes: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")
    distance = math.sqrt(coords[0]**2 + coords[1]**2 + coords[2]**2)
    print(f"Distance to center: {distance}\n")
    second_coords = None
    while not second_coords:
        strings = input("Enter new coordinates as floats in format 'x,y,z': ").split(",")
        for n in strings:
            try:
                float(n)
            except:
                print(f"Error on parameter 'abc': could not convert string to float: {n}")
        second_coords = tuple(float(n) for n in strings)
    distance_between = math.sqrt((coords[0] - second_coords[0])**2 + (
        coords[1] - second_coords[1])**2 + (coords[2] - second_coords[2])**2)
    print(f"Distance between the 2 sets of coordinates: {distance_between}")
    



if __name__ == "__main__":
    get_player_pos()
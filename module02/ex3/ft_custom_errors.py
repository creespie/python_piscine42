class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant: str = "Tomato"):
        super().__init__(f"The {plant} plant is wilting!")


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("banana")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    for error in [PlantError(), WaterError()]:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("All custom error types work correctly!")

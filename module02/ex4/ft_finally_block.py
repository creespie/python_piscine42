class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant: str = "Tomato"):
        super().__init__(f"Invalid plant name to water: '{plant}'")


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Not enough water in the tank!")


def water_plant(plant_name: str):
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(plant_name)


def test_watering_system(plant1, plant2, plant3):
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for instance in [plant1, plant2, plant3]:
            try:
                water_plant(instance)
            except PlantError as e:
                print(f"Caught PlantError: {e}")
    finally:
        print(".. ending tests and returning to main")
        print("Closing watering system")


if __name__ == "__main__":
    test_watering_system("Tomato", "banana", "Beans")

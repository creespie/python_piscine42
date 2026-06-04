class Plant:
    instances = []

    def __init__(self, name: str, height: float = 0, age: int = 0,
                 growth_rate: float = 0.8):
        self.name = name
        if height < 0:
            self._height = 0
        else:
            self._height = height
        if age < 0:
            self._ages = 0
        else:
            self._ages = age
        self.growth_rate = growth_rate
        Plant.instances.append(self)

    def __str__(self) -> str:
        if self._ages != 1:
            return (f"{self.name.capitalize()}: "
                    f"{self._height}cm, {self._ages} days old")
        else:
            return (f"{self.name.capitalize()}: "
                    f"{self._height}cm, {self._ages} day old")

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative"
                  )
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {int(self._height)}cm")

    def get_age(self) -> int:
        return self._ages

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative"
                  )
            print("Age update rejected")
        else:
            self._ages = value
            print(f"Age updated: {self._ages} days")

    def show(self) -> None:
        print(str(self))

    def age(self) -> None:
        self._ages += 1

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 1)


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str,
        growth_rate: float = 0.8
    ):
        super().__init__(name, height, age, growth_rate)
        self.color = color
        self._blooming = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._blooming:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")

    def bloom(self) -> None:
        self._blooming = True


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
        growth_rate: float = 0.8,
    ):
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name.capitalize()} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        growth_rate: float = 0.8,
    ):
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lurossi <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/02 12:43:04 by lurossi           #+#    #+#              #
#    Updated: 2026/06/02 12:43:04 by lurossi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3


class Plant:
    instances: list = []

    class Stats:
        def __init__(self):
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def show_stats(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show"
            )

    def __init__(
        self, name: str, height: float = 0, ages: int = 0, growth_rate: float = 0.8
    ):
        self.name = name
        self._height: float = height if height >= 0 else 0
        self._ages: int = ages if ages >= 0 else 0
        self.growth_rate = growth_rate
        self._stats = Plant.Stats()
        Plant.instances.append(self)

    def __str__(self) -> str:
        if self._ages != 1:
            return f"{self.name.capitalize()}: {self._height}cm, {self._ages} days old"
        else:
            return f"{self.name.capitalize()}: {self._height}cm, {self._ages} day old"

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {int(self._height)}cm")

    def get_age(self) -> int:
        return self._ages

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._ages = value
            print(f"Age updated: {self._ages} days")

    def show(self) -> None:
        self._stats._show_calls += 1
        print(str(self))

    def age(self) -> None:
        self._stats._age_calls += 1
        self._ages += 1

    def grow(self) -> None:
        self._stats._grow_calls += 1
        self._height = round(self._height + self.growth_rate, 1)


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str, growth_rate: float = 0.8
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
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_calls: int = 0

        def show_stats(self) -> None:
            super().show_stats()
            print(f"{self._shade_calls} shade")

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
        self._stats = Tree.Stats()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._stats._shade_calls += 1
        print(
            f"Tree {self.name.capitalize()} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide."
        )


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str, growth_rate: float = 0.8
    ):
        super().__init__(name, height, age, color, growth_rate)
        self._seeds: int = 0

    def bloom(self) -> None:
        super().bloom()

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
    plant._stats.show_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_a_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    for _ in range(10):
        sunflower.grow()
        sunflower.age()
    sunflower.bloom()
    sunflower._seeds = 42
    sunflower.show()
    print("[statistics for Sunflower]")
    display_statistics(sunflower)

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    display_statistics(unknown)

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
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plants_type.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lurossi <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/02 12:43:04 by lurossi           #+#    #+#              #
#    Updated: 2026/06/02 12:43:04 by lurossi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3


class Plant:
    instances = []

    def __init__(
        self, name: str, height: float = 0, age: int = 0, growth_rate: float = 0.8
    ):
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
        self._stats = self.Stats()
        Plant.instances.append(self)

    def __str__(self) -> str:
        if self._ages != 1:
            return f"{self.name.capitalize()}: {self._height}cm, {self._ages} days old"
        else:
            return f"{self.name.capitalize()}: {self._height}cm, {self._ages} day old"

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
        print(str(self))
        self._stats.increase("show")

    def age(self) -> None:
        self._ages += 1
        self._stats.increase("age")

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 1)
        self._stats.increase("grow")

    def stats_display(self):
        self._stats.display()

    @staticmethod
    def is_old(n):
        return n > 365
    
    @classmethod
    def anonymous_plant(cls, name: str = "Unknown plant"):
        return cls(name)
    
    class Stats:
        def __init__(self):
            self.grow = 0
            self.age = 0
            self.show = 0
        
        def increase(self, argument):
            if argument == "grow":
                self.grow += 1
            elif argument == "age":
                self.age += 1
            elif argument == "show":
                self.show += 1
        
        def display(self):
            print(f"Stats: {self.grow} grow, {self.age} age, {self.show} show")



class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str = "white", growth_rate: float = 0.8
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

class Seed(Flower):
    def __init__(self, name, height, age, color = "white", growth_rate = 0.8):
        super().__init__(name, height, age, color, growth_rate)
        self._seeds = 0
    
    def grow(self):
        self._seeds += 23
        super().grow()

    def show(self):
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    def __init__(self, name: str,height: float, age: int, trunk_diameter: float = 1.0, growth_rate: float = 0.8,):
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name.capitalize()} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide."
        )
        self._stats.increase("shade")

    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self.shade = 0
        
        def increase(self, argument):
            super().increase(argument)
            if argument == "shade":
                self.shade += 1
        
        def display(self):
            super().display()
            print(f"{self.shade} shade")
        

class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, growth_rate: float = 0.8,):
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
    print("=== Check Year Old")
    print(f"Is 30 days more than a year? -> {Plant.is_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_old(400)}\n")
    
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    rose.stats_display()
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    rose.stats_display()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    oak.stats_display()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak.stats_display()
    print() 
    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    sunflower.stats_display()
    print()

    print("=== Anonymus")
    idk = Plant.anonymous_plant()
    idk.show()
    print("[statistics for idk]")
    idk.stats_display()

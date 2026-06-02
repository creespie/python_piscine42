# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lurossi <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/02 12:43:04 by lurossi           #+#    #+#              #
#    Updated: 2026/06/02 12:43:04 by lurossi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    instances = []

    def __init__(
        self, name: str, height: float = 0, ages: int = 0, growth_rate: float = 0.8
    ):
        self.name = name
        if height < 0:
            self._height = 0
        else:
            self._height = height
        if ages < 0:
            self._ages = 0
        else:
            self._ages = ages
        self.growth_rate = growth_rate
        Plant.instances.append(self)

    def __str__(self):
        if self.ages != 1:
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

    def show(self):
        print("=== Garden Plant Registry ===")
        for instance in Plant.instances:
            print(instance)

    def age(self):
        self._ages += 1

    def grow(self):
        self._height = round((self._height + self.growth_rate), 1)


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant}")

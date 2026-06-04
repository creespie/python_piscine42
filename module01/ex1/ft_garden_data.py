class Plant:
    instances = []

    def __init__(self, name: str, height: str, age: str):
        self.name = name
        self.height = height
        self.age = age
        Plant.instances.append(self)

    def __str__(self):
        return (f"{self.name.capitalize()}: "
                f"{self.height} cm, {self.age} age old")

    def show(self):
        print("=== Garden Plant Registry ===")
        for instance in Plant.instances:
            print(instance)


if __name__ == "__main__":
    Plant("rose", "25", "30")
    Plant("carrot", "10", "15")
    Plant("tomato", "40", "60")

    Plant.instances[0].show()

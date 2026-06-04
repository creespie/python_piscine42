def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type.capitalize()} seed: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seed: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seed: covers {quantity} square meters"
              )
    else:
        print("Unknown unit type")


if __name__ == "__main__":
    ft_seed_inventory("tomato", 15, "packets")
    ft_seed_inventory("carrot", 8, "grams")
    ft_seed_inventory("lettuce", 12, "area")
    ft_seed_inventory("lettuce", 12, "ciao")

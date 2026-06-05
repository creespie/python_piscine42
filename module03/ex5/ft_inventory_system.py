import sys

def     inventory_manager():
    inventory = {}
    print("=== Inventory System Analysis ===")
    for insertion in sys.argv[1:]:
        insertion = insertion.split(":")
        if len(insertion) != 2:
            print(f"Error - invalid parameter '{insertion}'")
            continue
        key = insertion[0]
        if key in inventory.keys():
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            quantity = int(insertion[1])
        except:
            print(f"Quantity error for {key}: invalid literal for int() with base 10: '{insertion[1]}'")
            continue
        inventory[key] = quantity
    print(f"Got inventory: {list(inventory)}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory.keys())} items: {sum(inventory.values())}")
    for key, quantity in inventory.items():
        print(f"Item {key} represents {round(quantity/ sum(inventory.values())* 100, 1) }%")
    biggest = None
    for item, quantity in inventory.items():
        if biggest == None:
            biggest = (item, quantity)
        elif biggest[1] < quantity:
            biggest = (item, quantity)
    print(f"Item most abundant: {biggest[0]} with quantity {biggest[1]}")
    smallest = None
    for item, quantity in inventory.items():
        if smallest == None:
            smallest = (item, quantity)
        elif smallest[1] > quantity:
            smallest = (item, quantity)
    print(f"Item least abundant: {smallest[0]} with quantity {smallest[1]}")
    inventory.update({"magic item":1})
    print(f"Updated inventory: {inventory}")

if __name__ == "__main__":
    inventory_manager()
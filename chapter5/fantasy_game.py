def display_inventory(inventory):
    total_items = 0
    print("Inventory:")
    for key, value in inventory.items():
        print(f"{value} {key}")
        total_items += value
    print(f"\nTotal number of items: {total_items}")


def add_to_inventory(inventory, add_items):
    for item in add_items:
        try:
            inventory[item] += 1
        except KeyError:
            inventory[item] = 1

    return inventory


def main():
    stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
    display_inventory(stuff)

    inv = {"gold coin": 42, "rope": 1}
    dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)




if __name__ == "__main__":
    main()

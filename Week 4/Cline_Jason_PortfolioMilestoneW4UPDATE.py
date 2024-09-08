class ItemToPurchase:
    def __init__(
        self,
        item_name: str = "none",
        item_price: float = 0,
        item_quantity: int = 0,
    ) -> None:
        """
        Initializes an instance of ItemToPurchase class.

        Args:
            item_name (str): The name of the item. Defaults to "none".
            item_price (float): The price of the item. Defaults to 0.
            item_quantity (int): The quantity of the item. Defaults to 0.
        """
        self.item = {
            "name": item_name,
            "price": item_price,
            "quantity": item_quantity,
        }

    def print_item_cost(self) -> None:
        """
        Prints the cost of the item.
        """
        cost = self.item["price"] * self.item["quantity"]
        print(
            f"{self.item['name']} {self.item['quantity']} @ ${self.item['price']:.2f} = ${cost:.2f}"
        )


def main() -> None:
    """
    Main function to get input for items and calculate total cost.
    """
    items = []
    num_items = int(input("Enter the number of items: "))
    for n in range(num_items):
        print(f"\nItem {n + 1}")
        item_name = input("Enter the item name:\n")
        item_price = float(input("Enter the item price:\n"))
        item_quantity = int(input("Enter the item quantity:\n"))
        item = ItemToPurchase(item_name, item_price, item_quantity)
        items.append(item)

    print("\nTOTAL COST")
    total = 0
    for item in items:
        item.print_item_cost()
        total += item.item["price"] * item.item["quantity"]

    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()

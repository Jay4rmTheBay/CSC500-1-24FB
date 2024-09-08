class ItemToPurchase:
    def __init__(
        self,
        item_name: str = "none",
        item_price: float = 0,
        item_quantity: int = 0,
    ):
        """
        Initializes an instance of ItemToPurchase class.

        Args:
            item_name (str): The name of the item. Defaults to "none".
            item_price (float): The price of the item. Defaults to 0.
            item_quantity (int): The quantity of the item. Defaults to 0.
        """
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self) -> None:
        """
        Prints the cost of the item.
        """
        print(
            f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_price * self.item_quantity:.2f}"
        )


def main() -> None:
    """
    Main function to get input for items and calculate total cost.
    """
    # Get input for item 1
    print("\nItem 1")
    item_name1 = input("Enter the item name:\n")
    item_price1 = float(input("Enter the item price:\n"))
    item_quantity1 = int(input("Enter the item quantity:\n"))

    # Get input for item 2
    print("\nItem 2")
    item_name2 = input("Enter the item name:\n")
    item_price2 = float(input("Enter the item price:\n"))
    item_quantity2 = int(input("Enter the item quantity:\n"))

    # Calculate and print total cost
    print("\nTOTAL COST")
    item1 = ItemToPurchase(item_name1, item_price1, item_quantity1)
    item2 = ItemToPurchase(item_name2, item_price2, item_quantity2)
    item1.print_item_cost()
    item2.print_item_cost()
    total_cost = (item1.item_price * item1.item_quantity) + (
        item2.item_price * item2.item_quantity
    )
    print(f"Total: ${total_cost:.2f}")


if __name__ == "__main__":
    main()

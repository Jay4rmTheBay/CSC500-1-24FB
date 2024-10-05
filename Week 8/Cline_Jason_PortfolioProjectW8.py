# File Name: Cline_Jason_PortfolioProjectW8.py

# Author: Jason Todd Cline

# Institution: Colorado State University Global
# Class: CSC500-1
# Term: 24FB
# Module: 8


# Date Created: 10/05/2024
# Last Modified: 10/05/2024

WIDTH = 40

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
        cost: float = self.item["price"] * self.item["quantity"]
        print(
            f"{self.item['name']} {self.item['quantity']} @ ${self.item['price']:.2f} = ${cost:.2f}".center(WIDTH)
        )


class ShoppingCart:
    def __init__(
        self,
        customer_name: str = "none",
        current_date: str = "January 1, 2020",
    ) -> None:
        self.customer_name: str = customer_name
        self.current_date: str = current_date
        self.cart_items: list = []

    def add_item(self, item: ItemToPurchase) -> None:
        """
        Adds an item to cart_items list. Has parameter item of type ItemToPurchase. Does not return anything.

        Args:
            item (ItemToPurchase): The item to be added to the cart_items list.
        """
        self.cart_items.append(item)

    def remove_item(self, item_name: str) -> None:
        """
        Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
        If item name cannot be found, output this message: Item not found in cart. Nothing removed.
        """
        for item in self.cart_items:
            if item.item["name"].lower() == item_name.lower():
                self.cart_items.remove(item)
                print(f"{item_name} has been removed from the cart")
                return
        else:
            print("Item not found in cart. Nothing removed.")

    def modify_item(item: ItemToPurchase) -> None:
        """
        Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
        If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
        If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
        """
        pass

    def get_num_items_in_cart(self) -> int:
        """
        Returns quantity of all items in cart. Has no parameters.
        """
        total_quantity: int = 0
        for item in self.cart_items:
            total_quantity += item.item["quantity"]
        return total_quantity

    def get_cost_of_cart(self) -> float:
        """
        Determines and returns the total cost of items in cart. Has no parameters.
        """
        total: int = 0
        for item in self.cart_items:
            total += item.item["price"] * item.item["quantity"]

        return total

    def print_total(self) -> None:
        """
        Outputs total of objects in cart.
        If cart is empty, output this message: SHOPPING CART IS EMPTY
        """

        if self.cart_items:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}".center(WIDTH))
            print(f"Number of items: {len(self.cart_items)}".center(WIDTH))
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}".center(WIDTH))
            print()
        else:
            print(f"SHOPPING CART IS EMPTY".center(WIDTH))

    def print_descriptions(self) -> None:
        """
        Outputs each item's description.
        """
        if self.cart_items:
            print(
                f"{self.customer_name}'s Shopping Cart - {self.current_date}".center(WIDTH)
            )
            print(f"Item Descriptions".center(WIDTH))
            for item in self.cart_items:
                description = item.item.get("description", "No description available")
                print(f"{item.item['name']}: {description}".center(WIDTH))
        else:
            print(f"{'SHOPPING CART IS EMPTY'}".center(WIDTH))


def main() -> None:
    """
    Main function to...
    """
    cart: ShoppingCart = ShoppingCart("John Doe", "February 1, 2020")

    def print_menu(cart: ShoppingCart):
        while True:
            print()
            print(f"{'MENU':^{WIDTH}}")
            print(f"{'a - Add item to cart':^{WIDTH}}")
            print(f"{'r - Remove item from cart':^{WIDTH}}")
            print(f"{'c - Change item quantity':^{WIDTH}}")
            print(f"{'i - Output items\' descriptions':^{WIDTH}}")
            print(f"{'o - Output shopping cart':^{WIDTH}}")
            print(f"{'q - Quit':^{WIDTH}}")
            print(f"{'Choose an option: ':^{WIDTH}}")
            user_input = input(f"{'':^{WIDTH / 2}}")
            match user_input:
                case "q":
                    print(f"{'Thanks for shopping with us. Goodbye!':^{WIDTH}}")
                    return
                case "a":
                    item_name: str = input("Enter the item name: ")
                    item_price: float = float(input("Enter item price: "))
                    item_quantity: int = int(input("Enter item quantity: "))
                    cart.add_item(ItemToPurchase(item_name, item_price, item_quantity))
                case "r":
                    item_name = input("Enter the item name to remove: ")
                    cart.remove_item(item_name)
                case "c":
                    item_name = input("Enter the item name to modify: ")
                    cart.modify_item(item_name)
                case "i":
                    print()
                    print(f"{'OUTPUT ITEMS\' DESCRIPTIONS':^{WIDTH}}")
                    cart.print_descriptions()
                case "o":
                    print()
                    print(f"{'OUTPUT SHOPPING CART':^{WIDTH}}")
                    cart.print_total()
                case _:
                    print(f"{'Invalid input. Please choose a valid option.':^{WIDTH}}")
    
    print_menu(cart)

    print("\n")

    # Hard-coded for assignment as proof of concept without user input:
    
    # Create items with hardcoded descriptions as placeholders
    item1 = ItemToPurchase("Nike Romaleos", 189.00, 2)
    item1.item['description'] = "Volt color, Weightlifting shoes"  # Placeholder description for now

    item2 = ItemToPurchase("Chocolate Chips", 3.00, 5)
    item2.item['description'] = "Semi-sweet"  # Placeholder description for now

    item3 = ItemToPurchase("Powerbeats 2 Headphones", 128.00, 1)
    item3.item['description'] = "Bluetooth headphones"  # Placeholder description for now

    # Add items to shopping cart
    shopping_cart = ShoppingCart(customer_name = "John Doe", current_date = "February 1, 2020")
    shopping_cart.add_item(item1)
    shopping_cart.add_item(item2)
    shopping_cart.add_item(item3)

    # Print item descriptions as proof of concept
    shopping_cart.print_descriptions()


if __name__ == "__main__":
    main()

# File Name: Cline_Jason_PortfolioProjectFinalW8.py

# Author: Jason Todd Cline

# Institution: Colorado State University Global
# Class: CSC500-1
# Term: 24FB
# Module: 8


# Date Created: 10/05/2024
# Last Modified: 10/06/2024

WIDTH = 40

class ItemToPurchase:
    def __init__(
        self,
        item_name: str = "none",
        item_description: str = "none",
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
            "description": item_description,
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
                print(f"{item_name} has been removed from the cart".center(WIDTH))
                return
        else:
            print("Item not found in cart. Nothing removed.".center(WIDTH))

    def modify_item(self, item: ItemToPurchase) -> None:
        """
        Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
        If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
        If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
        """
        found = False
        for cart_item in self.cart_items:
            if cart_item.item['name'].lower() == item.item['name'].lower():
                found = True
                if item.item['quantity'] != 0:
                    cart_item.item['quantity'] = item.item['quantity']
                    print(f"{item.item['name']} found in cart. Quantity modified.".center(WIDTH))
                if item.item['price'] != 0:
                    cart_item.item['price'] = item.item['price']
                    print(f"{item.item['name']} found in cart. Price modified.".center(WIDTH))
                if item.item['description'] != "none":
                    cart_item.item['description'] = item.item['description']
                    print(f"{item.item['name']} found in cart. Description modified.".center(WIDTH))
                break
        if not found:
            print(f"{item.item['name']} not found in cart. Nothing modified.".center(WIDTH))

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
        total: float = 0
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
                print(f"{item.item['name']}: {item.item['description']}".center(WIDTH))
        else:
            print(f"{'SHOPPING CART IS EMPTY'}".center(WIDTH))


def get_float_input(prompt: str) -> float:
    """Helper function to get a valid float input from the user."""
    while True:
        print(prompt.center(WIDTH))
        user_input = input(" " * (WIDTH // 2))
        if user_input == "":
            return 0.0
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number or press enter to skip.".center(WIDTH))

def get_int_input(prompt: str) -> int:
    """Helper function to get a valid integer input from the user."""
    while True:
        print(prompt.center(WIDTH))
        user_input = input(" " * (WIDTH // 2))
        if user_input == "":
            return 0
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer or press enter to skip.".center(WIDTH))

def main() -> None:
    """
    Main function to...
    """
    print(f"{'Enter customer\'s name:':^{WIDTH}}")
    customer_name: str = input(f"{'':^{WIDTH // 3}}")
    print(f"{'Enter today\'s date:':^{WIDTH}}")
    current_date: str = input(f"{'':^{WIDTH // 3}}")
    print(f"{f'Customer\'s name: {customer_name}':^{WIDTH}}")
    print(f"{f'Today\'s date: {current_date}':^{WIDTH}}")
    cart: ShoppingCart = ShoppingCart(customer_name, current_date)

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
            user_input = input(" " * (WIDTH // 2))
            match user_input:
                case "q":
                    print(f"{'Thanks for shopping with us. Goodbye!':^{WIDTH}}")
                    print()
                    return
                case "a":
                    print()
                    print("ADD ITEM TO CART".center(WIDTH))
                    print("Enter the item name:".center(WIDTH))
                    item_name: str = input(f"{'':^{WIDTH // 3}}")
                    print("Enter the item description:".center(WIDTH))
                    item_description: str = input(" " * (WIDTH // 3))
                    item_price: float = get_float_input("Enter item price:")
                    item_quantity: int = get_int_input("Enter item quantity:")
                    cart.add_item(ItemToPurchase(item_name, item_description, item_price, item_quantity))
                case "r":
                    print()
                    print("REMOVE ITEM FROM CART".center(WIDTH))
                    print("Enter name of item to remove:".center(WIDTH))
                    item_name: str = input(" " * (WIDTH // 2))
                    cart.remove_item(item_name)
                case "c":
                    print()
                    print("CHANGE ITEM QUANTITY".center(WIDTH))
                    print("Enter the item name to modify:".center(WIDTH))
                    new_name: str = input(" " * (WIDTH // 3))
                    new_quantity: int = get_int_input("Enter the new quantity:")
                    new_item = ItemToPurchase(item_name = new_name, item_quantity = new_quantity)
                    cart.modify_item(new_item)
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

if __name__ == "__main__":
    main()
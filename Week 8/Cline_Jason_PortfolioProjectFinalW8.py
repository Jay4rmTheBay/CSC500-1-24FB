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
        item_price: float = 0.0,
        item_quantity: int = 0,
    ) -> None:
        """
        Initializes an instance of ItemToPurchase class.

        Args:
            item_name (str): The name of the item. Defaults to "none".
            item_price (float): The price of the item. Defaults to 0.
            item_quantity (int): The quantity of the item. Defaults to 0.
        Returns:
            None: This method does not return anything.
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
        """
        Initialize a new instance of the class.
        Args:
            customer_name (str): The name of the customer. Defaults to "none".
            current_date (str): The current date. Defaults to "January 1, 2020".
        Returns:
            None: This method does not return anything.
        """
        self.customer_name: str = customer_name
        self.current_date: str = current_date
        self.cart_items: list = []

    def add_item(self, item: ItemToPurchase) -> None:
        """
        Adds an item to cart_items list. Has parameter item of type ItemToPurchase. Does not return anything.

        Args:
            item (ItemToPurchase): The item to be added to the cart_items list.
        Returns:
            None: This method does not return anything.
        """
        self.cart_items.append(item)

    def remove_item(self, item_name: str) -> None:
        """
        Removes item from cart_items list.

        Args:
            item_name (str): The name of the item to be removed.
        Returns:
            None: This method does not return anything.
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
        Modifies an item's description, price, and/or quantity.

        Args:
            item (ItemToPurchase): The item to be modified.
        Returns:
            None: This method does not return anything.
        """
        found = False
        for cart_item in self.cart_items:
            if cart_item.item['name'].lower() == item.item['name'].lower():
                found = True
                if item.item['quantity'] != 0:
                    cart_item.item['quantity'] = item.item['quantity']
                    print(f"{item.item['name']} found in cart. Quantity modified.".center(WIDTH))
                if item.item['price'] != 0.0:
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
        Returns the quantity of all items in the cart.

        Args:
            This method does not require any parameters.
        Returns:
            int: The total quantity of all items in the cart.
        """
        total_quantity: int = 0
        for item in self.cart_items:
            total_quantity += item.item["quantity"]
        return total_quantity

    def get_cost_of_cart(self) -> float:
        """
        Determines and returns the total cost of items in the cart.
        Args:
            This method does not require any parameters.
        Returns:
            float: The total cost of items in the cart.
        """
        total: float = 0.0
        for item in self.cart_items:
            total += item.item["price"] * item.item["quantity"]

        return total

    def print_total(self) -> None:
        """
        Outputs total of objects in cart.
        Args:
            This method does not require any parameters.
        Returns:
            None: This method does not return anything.
        """

        if self.cart_items:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}".center(WIDTH))
            print(f"Number of items: {self.get_num_items_in_cart()}".center(WIDTH))
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}".center(WIDTH))
        else:
            print(f"SHOPPING CART IS EMPTY".center(WIDTH))

    def print_descriptions(self) -> None:
        """
        Outputs total of objects in cart.

        Args:
            This method does not require any parameters.
        Returns:
            None: This method does not return anything.
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
    """
    Helper function to get a valid float input from the user.

    Args:
        prompt (str): The prompt message to display to the user.
    Returns:
        float: The valid float input from the user.
    """
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
    """
    Helper function to get a valid integer input from the user.

    Args:
        prompt (str): The prompt message to display to the user.
    Returns:
        int: The valid integer input from the user.
    """
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
    Main function that serves as the entry point of the program.
    It prompts the user to enter customer's name and today's date.
    Then, it creates a ShoppingCart object using the provided information.
    It displays a menu of options for the user to interact with the shopping cart.
    The user can add items to the cart, remove items from the cart, change item quantity, 
    change item price, change item description, output items' descriptions, output the shopping cart, 
    or quit the program.
    The function continues to display the menu until the user chooses to quit.
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
            print(f"{'p - Change item price':^{WIDTH}}")
            print(f"{'d - Change item description':^{WIDTH}}")
            print(f"{'i - Output items\' descriptions':^{WIDTH}}")
            print(f"{'o - Output shopping cart':^{WIDTH}}")
            print(f"{'q - Quit':^{WIDTH}}")
            print(f"{'Choose an option: ':^{WIDTH}}")
            user_input = input(" " * (WIDTH // 2)).lower()
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
                    item_name: str = input(" " * (WIDTH // 3))
                    cart.remove_item(item_name)
                case "c":
                    print()
                    print("CHANGE ITEM QUANTITY".center(WIDTH))
                    print("Enter the item name to modify:".center(WIDTH))
                    item_name: str = input(" " * (WIDTH // 3))
                    new_quantity: int = get_int_input("Enter the new quantity:")
                    new_item = ItemToPurchase(item_name = item_name, item_quantity = new_quantity)
                    cart.modify_item(new_item)
                case "p":
                    print()
                    print("CHANGE ITEM PRICE".center(WIDTH))
                    print("Enter the item name to modify:".center(WIDTH))
                    item_name: str = input(" " * (WIDTH // 3))
                    new_price: float = get_float_input("Enter the new price:")
                    new_item = ItemToPurchase(item_name = item_name, item_price = new_price)
                    cart.modify_item(new_item)
                case "d":
                    print()
                    print("CHANGE ITEM DESCRIPTION".center(WIDTH))
                    print("Enter the item name to modify:".center(WIDTH))
                    item_name: str = input(" " * (WIDTH // 3))
                    print("Enter the new description:".center(WIDTH))
                    new_description: str = input(" " * (WIDTH // 3))
                    new_item = ItemToPurchase(item_name = item_name, item_description = new_description)
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
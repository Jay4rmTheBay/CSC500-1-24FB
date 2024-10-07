import unittest
from unittest.mock import patch
from Cline_Jason_PortfolioProjectFinalW8 import ItemToPurchase, ShoppingCart


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart("John Doe", "October 10, 2024")

    def test_add_item(self):
        item = ItemToPurchase("Shirt", "Blue shirt", 15.99, 2)
        self.cart.add_item(item)
        self.assertEqual(len(self.cart.cart_items), 1)

    def test_remove_item(self):
        item1 = ItemToPurchase("Shirt", "Blue shirt", 15.99, 2)
        item2 = ItemToPurchase("Pants", "Black pants", 29.99, 1)
        self.cart.add_item(item1)
        self.cart.add_item(item2)
        self.cart.remove_item("Shirt")
        self.assertEqual(len(self.cart.cart_items), 1)

    def test_modify_item_quantity(self):
        item = ItemToPurchase("Shirt", "Blue shirt", 15.99, 2)
        self.cart.add_item(item)
        new_item = ItemToPurchase("Shirt", item_quantity=3)
        self.cart.modify_item(new_item)
        self.assertEqual(self.cart.cart_items[0].item["quantity"], 3)

    def test_modify_item_price(self):
        item = ItemToPurchase("Shirt", "Blue shirt", 15.99, 2)
        self.cart.add_item(item)
        new_item = ItemToPurchase("Shirt", item_price=19.99)
        self.cart.modify_item(new_item)
        self.assertEqual(self.cart.cart_items[0].item["price"], 19.99)

    def test_modify_item_description(self):
        item = ItemToPurchase("Shirt", "Blue shirt", 15.99, 2)
        self.cart.add_item(item)
        new_item = ItemToPurchase("Shirt", item_description="Red shirt")
        self.cart.modify_item(new_item)
        self.assertEqual(
            self.cart.cart_items[0].item["description"], "Red shirt"
        )

    def test_get_num_items_in_cart(self):
        item1 = ItemToPurchase("Shirt", "Blue shirt", 15.99, 2)
        item2 = ItemToPurchase("Pants", "Black pants", 29.99, 1)
        self.cart.add_item(item1)
        self.cart.add_item(item2)
        self.assertEqual(self.cart.get_num_items_in_cart(), 3)

    def test_get_cost_of_cart(self):
        item1 = ItemToPurchase("Shirt", "Blue shirt", 15.99, 2)
        item2 = ItemToPurchase("Pants", "Black pants", 29.99, 1)
        self.cart.add_item(item1)
        self.cart.add_item(item2)
        self.assertEqual(self.cart.get_cost_of_cart(), 61.97)

    @patch("builtins.print")
    def test_print_total(self, mock_print):
        item1 = ItemToPurchase("Shirt", "Blue shirt", 15.99, 2)
        item2 = ItemToPurchase("Pants", "Black pants", 29.99, 1)
        self.cart.add_item(item1)
        self.cart.add_item(item2)
        self.cart.print_total()
        expected_calls = [
            unittest.mock.call(
                "John Doe's Shopping Cart - October 10, 2024".center(40)
            ),
            unittest.mock.call("Number of items: 3".center(40)),
            unittest.mock.call("Shirt 2 @ $15.99 = $31.98".center(40)),
            unittest.mock.call("Pants 1 @ $29.99 = $29.99".center(40)),
            unittest.mock.call("Total: $61.97".center(40)),
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch("builtins.print")
    def test_print_descriptions(self, mock_print):
        item1 = ItemToPurchase("Shirt", "Blue shirt", 15.99, 2)
        item2 = ItemToPurchase("Pants", "Black pants", 29.99, 1)
        self.cart.add_item(item1)
        self.cart.add_item(item2)
        self.cart.print_descriptions()
        expected_calls = [
            unittest.mock.call(
                "John Doe's Shopping Cart - October 10, 2024".center(40)
            ),
            unittest.mock.call("Item Descriptions".center(40)),
            unittest.mock.call("Shirt: Blue shirt".center(40)),
            unittest.mock.call("Pants: Black pants".center(40)),
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)


if __name__ == "__main__":
    unittest.main()

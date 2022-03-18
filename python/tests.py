import unittest

from shopping_cart import ShoppingCartConcreteCreator
from test_utils import Capturing

class ShoppingCartTest(unittest.TestCase):
    def test_print_receipt(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple x 2 = €2.00", output[0])

    def test_doesnt_explode_on_mystery_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("banana", 5)
        sc.add_item("pear", 5)
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple x 2 = €2.00", output[0])
        self.assertEqual("banana x 5 = €10.00", output[1])
        self.assertEqual("pear x 5 = €0.00", output[2])

    """
        I've altered the unit tests above
        Below are new tests I've added
    """

    def test_print_total_price_with_one_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)

        with Capturing() as output:
            sc.print_total_price()
        self.assertEqual("Total Price of ['apple x 2'] is €2.00", output[0])

    def test_print_total_price_with_multiple_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2) # price * quantity --> 200
        sc.add_item("banana", 5) # price * quantity --> 1000

        with Capturing() as output:
            sc.print_total_price()
        self.assertEqual("Total Price of ['apple x 2', 'banana x 5'] is €12.00", output[0])

    def test_add_item_with_one_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)

        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple x 2 = €2.00", output[0])

    def test_add_item_with_multiple_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("banana", 3)
        sc.add_item("pear", 1)

        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple x 2 = €2.00", output[0])
        self.assertEqual("banana x 3 = €6.00", output[1])
        self.assertEqual("pear x 1 = €0.00", output[2])

    def test_add_item_with_wrong_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("kinder bueno", 1)

        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("kinder bueno x 1 = €0.00", output[0])

    def test_with_price_first(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("banana", 3)
        sc.add_item("pear", 1)

        with Capturing() as output:
            sc.print_receipt(True) # we set to true as we want prices first.
        self.assertEqual("€2.00 = apple x 2", output[0])
        self.assertEqual("€6.00 = banana x 3", output[1])
        self.assertEqual("€0.00 = pear x 1", output[2])

    def test_add_item_with_same_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("apple", 5)

        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple x 7 = €7.00", output[0])

    def test_add_item_with_multiple_same_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("apple", 5)
        sc.add_item("banana", 1)
        sc.add_item("banana", 2)

        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple x 7 = €7.00", output[0])
        self.assertEqual("banana x 3 = €6.00", output[1])

    def test_add_item_with_multiple_same_item_in_different_order(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("banana", 1)
        sc.add_item("apple", 5)
        sc.add_item("banana", 2)

        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple x 7 = €7.00", output[0])
        self.assertEqual("banana x 3 = €6.00", output[1])

    def test_print_receipt_with_no_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("No items in the basket", output[0])

    def test_convert_cents_to_euros_method(self):
        sc = ShoppingCartConcreteCreator().operation()
        self.assertEqual("€5.00", sc.convert_cents_to_euros(500))
        self.assertEqual("€10.00", sc.convert_cents_to_euros(1000))
        self.assertEqual("€10.50", sc.convert_cents_to_euros(1050))

    def test_convert_cents_to_euros_method_with_num_string(self):
        sc = ShoppingCartConcreteCreator().operation()
        self.assertEqual("€5.00", sc.convert_cents_to_euros("500"))
        self.assertEqual("€10.00", sc.convert_cents_to_euros("1000"))
        self.assertEqual("€10.50", sc.convert_cents_to_euros("1050"))

unittest.main(exit=False)

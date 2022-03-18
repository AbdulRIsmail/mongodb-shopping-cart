from abc import ABC, abstractmethod
from typing import Dict

from shopping_cart_interface import IShoppingCart
from pricer import Pricer
from format import Format


class ShoppingCart(IShoppingCart):
    """
    Implementation of the shopping tills in our supermarket.
    """
    def __init__(self, pricer: Pricer):
        self.pricer = pricer
        # self.format = format
        self._contents: Dict[str,int] = {}

    def convert_cents_to_euros(self, number):
        return '€{:,.2f}'.format(int(number)/100)

    def add_item(self, item_type: str, number: int):
        # adds new item to or update existing item in the shopping cart
        if item_type not in self._contents:
            self._contents[item_type] = number
        else:
            self._contents[item_type] = self._contents[item_type] + number

    def print_receipt(self, price_first = False):
        if len(self._contents.items()) > 0:
            for key, value in self._contents.items():
                price = self.pricer.get_price(key) * value

                if price_first:
                    print(f"{self.convert_cents_to_euros(price)} = {key} x {value}")
                else:
                    print(f"{key} x {value} = {self.convert_cents_to_euros(price)}")
        else:
            print("No items in the basket")

    def print_total_price(self):
        total_price = 0
        items = []

        for key, value in self._contents.items():
            total_price = total_price + self.pricer.get_price(key) * value
            items.append(key + " x " + str(value))

        print(f"Total Price of {items} is {self.convert_cents_to_euros(total_price)}")
        

class ShoppingCartCreator(ABC):
    """
    Interface for the ShoppingCart creator.
    The creation process will be delegated to the subclasses of this class.
    """
    @abstractmethod
    def factory_method(self) -> ShoppingCart:
        # return the ShoppingCart object
        pass

    def operation(self) -> ShoppingCart:
        # Here more operations can be performed on the ShoppingCart object
        # returns ShoppingCart object
        return self.factory_method()

class ShoppingCartConcreteCreator(ShoppingCartCreator):
    """
    Concrete class for the ShoppingCart creator.
    Implements the factory_method
    """
    def factory_method(self) -> ShoppingCart:
        # returns ShoppingCart object
        return ShoppingCart(Pricer())


class Format:
    """
    a datastore for the receipt price format
    """
    def __init__(self, defaultChoice: 1):
        self.__format_database = {1: "{price} = ${key} x ${value}", 2: "{key} x ${value} = ${price}"}

    def get_format(self, itemtype: str):
        if itemtype not in self.__format_database:
            return 0
        return self.__pricing_database[itemtype]

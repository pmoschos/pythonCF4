class OutOfStockError(Exception):
    def __init__(self, item_name):
        super().__init__(f"{item_name} is out of stock")

class Item():
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.quantity}"
    
    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)

class Inventory:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item_name_to_remove):
        if Item(item_name_to_remove, None) not in self.items:
            raise ValueError(f"{item_name_to_remove} is not in the inventory")
        
        for item in self.items:
            if item == Item(item_name_to_remove, None):
                if item.quantity > 0:
                    item.quanity -= 1
                    return Item(item.name, item.quantity) # my item
                else:
                    raise OutOfStockError(item.name)

    def print_items(self):
        for item in self.items:
            print(item)
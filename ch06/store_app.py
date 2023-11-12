import store
from store import Inventory, Item, OutOfStockError

invetory = store.Inventory()

invetory.add_item(store.Item("Milk", 0))

invetory.print_items()

try:
    invetory.remove_item('Milk')
except (store.OutOfStockError, ValueError) as e:
    print(e)
    
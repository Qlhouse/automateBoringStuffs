from item import Item
from phone import Phone

item1 = Item('MyItem', 750)

print(item1.name)

# item1.name = "OtherItemItem"
item1.name = "OtherItem"

print(item1.name)

item1.apply_discount()

print(item1)

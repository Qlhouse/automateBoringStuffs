import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = list()

    def __init__(self, name: str, price: float, quantity = 0):
        # Run validation to the received arguements
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    def calcute_total_price(self):
        return self.price * self.quantity
 
    def apply_discount(self):
        # self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'), 
                price=float(item.get('price')), 
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(self):

Item.instantiate_from_csv()
print(Item.all)
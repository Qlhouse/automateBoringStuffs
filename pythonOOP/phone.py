from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity = 0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # Run validation to the received arguements
        assert broken_phones >= 0, f"Broken phone {broken_phones} is not greater than or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones

# # Add Laptop class, test: print(Laptop.all)
# class Laptop(Item):
#     def __init__(self, name: str, price: float, quantity = 0, size=13):
#         # Call to super function to have access to all attributes / methods
#         super().__init__(name, price, quantity)

#         # Run validation to the received arguements
#         assert size >= 0, f"Broken phone {size} is not greater than or equal to zero!"

#         # Assign to self object
#         self.size = size



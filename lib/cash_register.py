#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transactions = []  # To track prices and quantities
    
    def add_item(self, item_name, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item_name] * quantity)
        self.transactions.append((item_name, price, quantity))
    
    def apply_discount(self):
        if self.discount:
            self.total *= (1 - self.discount / 100)
            self.total = round(self.total, 2)  # Round to 2 decimal places
        else:
            print("No discount to apply")
    
    def void_last_transaction(self):
        if self.transactions:
            last_item, last_price, last_quantity = self.transactions.pop()
            self.total -= last_price * last_quantity
            self.total = round(self.total, 2)  # Ensure precision
            for _ in range(last_quantity):
                self.items.remove(last_item)

# Example usage:
# register = CashRegister(20)  # 20% discount
# register.add_item("Apple", 1.0, 3)
# register.apply_discount()

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0
        self.previous_transactions = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity
        self.items.extend([title] * quantity)
        self.previous_transactions.append(price * quantity)

    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * (1 - self.discount / 100)) if self.discount > 1 else int(self.total * (1 - self.discount))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
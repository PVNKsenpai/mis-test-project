class MIS:
    def __init__(self):
        self.users = {"admin": "123456"}
        self.orders = []

    def login(self, username, password):
        return self.users.get(username) == password

    def create_order(self, product, quantity):
        if quantity <= 0:
            return False
        self.orders.append({"product": product, "quantity": quantity})
        return True

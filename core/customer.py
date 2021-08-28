import stripe


class Customer:
    def create(self):
        return stripe.Customer.create()

    def list(self):
        return stripe.Customer.list()

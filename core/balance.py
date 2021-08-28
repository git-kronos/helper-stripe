import stripe


class Balance:
    def retrieve(self):
        return stripe.Balance.retrieve()

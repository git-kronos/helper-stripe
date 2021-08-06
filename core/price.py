import stripe


class Price:

    """ all stripe price methods """

    def get_price_list(self):
        """price list all"""
        return stripe.Price.list()


    def get_price(self, id:str):
        """price retrive"""
        return stripe.Price.retrieve(id)


    def price_create(self, ammount:int, prod_id:str):
        """price create"""
        return stripe.Price.create(
            unit_amount=ammount,
            currency="usd",
            recurring={"interval": "month"},
            product=prod_id
            )


    def price_modify(self, id:str, active: bool):
        """price modify"""
        return stripe.Price.modify(id, active=active)

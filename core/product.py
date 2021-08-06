import stripe

class Product:

    """ all stripe production methods """

    def get_product_list(self):
        """ product list all """

        return stripe.Product.list()


    def get_priduct(self, id:str):
        """ product retrive """

        return stripe.Product.retrieve(id)


    def product_create(self, name:str):
        """ product create """

        return stripe.Product.create(name=name)


    def product_modify(self, id:str, active:bool):
        """ product modify """

        return stripe.Product.modify(id, active=active)


    def product_delete(self, id: str):
        """ product delete """

        return stripe.Product.delete(id)

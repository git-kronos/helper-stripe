import stripe


class Subscription:
    """ all stripe subscription methods """

    def get_subscription_list(self):
        """ subscription list all """
        return stripe.Subscription.list()

    def get_subscription(self, id: str):
        """ get indivisual subscription detail """
        return stripe.Subscription.retrieve(id)

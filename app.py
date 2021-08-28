import settings
import stripe
from core import (
    Price, Product, Subscription, Customer, Balance
)

stripe.api_key = settings.SECRET_KEY


# my code

price = Price()
product = Product()
subscription = Subscription()
customer = Customer()
balance = Balance()

# # ======================================
# # Test Stripe API
# # ======================================


# # ======================================
# # products
# # ======================================
# products = product.all_products()
# for p in products:
#     print(p.id)


# # ======================================
# # price
# # ======================================
# prices = price.all_price()
# price_list = []

# for p in prices:
#     price_list.append(p.id)

# print(price_list)
# print()

# if settings.price1 in price_list:
#     print(p)
# else:
#     print('not available')


# # ======================================
# # Subscription
# # ======================================
# all_sub = [s.id for s in subscription.get_subscription_list()]
# print('==================================')
# for s in all_sub:
#     sub = subscription.get_subscription(s)
#     print(sub.id, sub.plan.name, sub.plan.interval, sub.plan.amount / 100)


# # ======================================
# # Customer
# # ======================================
# cus = customer.create()
# print(cus)
# print(cus.last_response.request_id)
# list_cus = customer.list()
# print([c.id for c in list_cus])
#
#
# print([b.id for b in balance.retrieve()])
bal = balance.retrieve()
print(bal['available'][0]['currency'])

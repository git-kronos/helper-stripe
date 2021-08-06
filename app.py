import settings
import stripe
from core import Price, Product, Subscription

stripe.api_key = settings.SECRET_KEY


# my code

price = Price()
product = Product()
subscription = Subscription()


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
# all_sub = subscription.get_all_subscription()

# print('==================================')
# for s in all_sub:
#     sub = subscription.get_subscription(s.id)
#     print(sub.plan.name)
#     print(sub.plan.interval)

print('hello and welcome to your shopping list!')

items = ['bread', 'milk', 'oranges']
prices = [1.00, 1.19, 0.30]

def calculate_price(prices):
    new_price = 0
    for price in prices:
        new_price += price
    new_price = round(new_price, 2)
    print('total price (rounded), ',  new_price)
        
item = input('Type to add an item to your shopping list, or press x to exit. ')
if item == 'x':
    calculate_price(prices)
    # print('have a good day shopping! Your total is: ', total_price)
else:
    items.append(item)
    price = input('What is the price of the new item?')
    prices.append(price)
    calculate_price(prices)
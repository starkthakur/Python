from operator import itemgetter

stocks = [
    {'ticker': 'AAPL', 'price': 201},
    {'ticker': 'IBM', 'price': 400},
    {'ticker': 'Google', 'price': 700},
    {'ticker': 'Msft', 'price': 1010},
    {'ticker': 'Tesla', 'price': 900},
    {'ticker': 'Amazon', 'price': 1200},
    {'ticker': 'HP', 'price': 143},
    {'ticker': 'Dell', 'price': 192},
    {'ticker': 'Facebook', 'price': 421},
    {'ticker': 'Alibaba', 'price': 93},
    {'ticker': 'Tata', 'price': 245},
    {'ticker': 'zscaler', 'price': 231}
]

print('--------Value Sorted By NAME--------')
for x in sorted(stocks, key=itemgetter('ticker')):
    print(x)
print('-------VALUE SORTED BY PRICE--------')
for y in sorted(stocks, key=itemgetter('price')):
    print(y)
print('----------Multiple Sort By Price(key) along with the Name(key) if having similar value -----------')
for z in sorted(stocks, key=itemgetter('price', 'ticker')):
    print(z)

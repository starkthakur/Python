import heapq

grades = [32, 43, 654, 34, 112, 132, 66, 99, 532]
print(heapq.nlargest(4, grades))

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

print(heapq.nlargest(4, stocks, key=lambda x: x['price']))
print(heapq.nsmallest(4, stocks, key=lambda stock: stock['price']))

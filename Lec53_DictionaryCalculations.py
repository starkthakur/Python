stocks = {
    'AAPL': 201,
    'IBM': 400,
    'Google': 700,
    'Microsoft': 1010,
    'Tesla': 900,
    'Amazon': 1200,
    'HP': 143,
    'Dell': 192,
    'Facebook': 421,
    'Alibaba': 93,
    'Tata': 245,
    'zscaler': 231
}
print(min(stocks))  # it takes the key insteadof value i.e. the minimum in alphabetical order i.e. Aapl
print(min(stocks.values()))  # it takes the stock minimum value

# (201 ,AAPL) (400, IBM) creating a variable min_price to store data in this format and print
min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)

stocks = {
    'Google': 520,
    'FB': 76,
    'Yahoo': 12,
    'APPLE': 600,
    'Microsoft': 540,
    'Twitter': 40,
    'ASML': 110
}

print("Min Valued Stock : ", min(zip(stocks.values(), stocks.keys())))
print("Max Valued Stock :", max(zip(stocks.values(), stocks.keys())))
print("Min to Max Valued sorted Stock: ", sorted(zip(stocks.values(), stocks.keys())))

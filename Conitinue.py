NumbersTaken = [2, 5, 12, 33, 17]
print(" These Numbers are available")

for n in range(1, 20):
    if n in NumbersTaken:
        continue
    print(n)
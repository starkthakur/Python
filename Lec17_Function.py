def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)


add_numbers(3, 32)
add_numbers(8, 32)

# Here Print is in Inner for loop hence number will get printed twice for 3,32 and 8,32

def add_numbers(*args):
    total = 0
    for a in args:
        total += a
        print(total)


add_numbers(5, 50)
add_numbers(55, 15)



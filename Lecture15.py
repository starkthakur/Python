"""

a = 7823


def corn():
    print(a)


def fudge():
    print(a)


corn()
fudge()

"""

# This code below will give error as variable 'a' is declared within the function not outside the function
# Now if we declare the function again in fudge it works


def corn():
    a = 7823
    print(a)


def fudge():
    a = 7824
    print(a)


corn()
fudge()

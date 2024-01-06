magicnumber = 26
print("The magic number is " + str(magicnumber))

#this program finds magic number

'''
#the 3 quotes are used to comment out the code
for n in range(101):
    if n is magicnumber:
        print()
'''
magicnumber = 29
for n in range(101):
    if n is magicnumber:
        print(n, "is a magic number")

magicnumber = 42
for n in range(39,45):
    if n is magicnumber:
        print(n, "is a magic number")
        break
    else:
        print(n, "is not a magic number")

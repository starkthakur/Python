from struct import *

# the data output is stored as bytes data below :

packed_data = pack("iif", 6, 18, 5.74)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# To get byte data back to normal binary format

Original_Data = unpack('iif', packed_data)
print(Original_Data)

# If already aware of the format then we can unpack using the below ex here its iif i.e. int ,int, float
print(unpack('iif', b'\x06\x00\x00\x00\x12\x00\x00\x00\x14\xae\xb7@'))

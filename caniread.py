import struct
binaryFILE = open("bin.bin", 'rb')
player ='10h 17H'
binary = binaryFILE.readline()
binary_unpack = struct.unpack((3* player), binary)
print(binary_unpack)


import struct
binaryFILE = open("bin.bin", 'rb')
binary = binaryFILE.readline()
binary_unpack = struct.unpack('I I I I', binary)
print (bin(binary_unpack[0]))
print (bin(binary_unpack[0]))
print(binary_unpack)

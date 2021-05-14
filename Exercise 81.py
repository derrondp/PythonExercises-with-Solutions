# Question 81:

# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

import zlib

str = "hello world!hello world!hello world!hello world!"
t = zlib.compress(str.encode())

print("Compressed:", t)
print("Decompressed:", str)
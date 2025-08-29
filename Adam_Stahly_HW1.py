import random
import math

plaintext = input("Enter the plaintext message: ")
key_length = random.randint(4, 10)
print(key_length)
tmatrix = [math.ceil(float(len(plaintext)/key_length))][key_length]
for i in range(len(plaintext)):
    for j in range(len(plaintext)):
        tmatrix[i][j] = plaintext[i]
print(tmatrix)
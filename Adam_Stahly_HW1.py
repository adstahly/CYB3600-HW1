import random
import math

plaintext = "The quick brown fox jumps over the lazy dog" #input("Enter the plaintext message: ")
key_length = 4 #random.randint(4, 10)
motified_text = plaintext.replace(' ', '')
#print(key_length)
row_amount = math.ceil(float(len(motified_text)/key_length))
tmatrix = [[" " for _ in range(key_length)] for _ in range(row_amount)]
row_counter = 0
col_counter = 0
for char in motified_text:
    tmatrix[row_counter%row_amount][col_counter%key_length] = char
    print(tmatrix)
    if col_counter%key_length == key_length-1 and col_counter > 0:
        row_counter += 1
    col_counter += 1
# #tmatrix = [math.ceil(float(len(plaintext)/key_length))][key_length]
# #for i in range(len(plaintext)):
# #    for j in range(len(plaintext)):
# #        tmatrix[i][j] = 1

#Adam Stahly
import random
import math

def populate_matrix(text,matrix):
    row_counter = 0
    for letter_index, char in enumerate(text):
        current_row = row_counter % row_amount
        current_col = letter_index % key_length
        matrix[current_row][current_col] = char
        if current_col == key_length - 1:
            row_counter += 1
    return matrix

plaintext = input("Enter the plaintext message: ")
key_length = random.randint(4, 10)
motified_text = plaintext.replace(' ', '')
row_amount = math.ceil(float(len(motified_text)/key_length))
tmatrix = [[" " for _ in range(key_length)] for _ in range(row_amount)]
tmatrix = populate_matrix(motified_text, tmatrix)
ciphertext = ""

for col_index in range(key_length):
    for row_index in range(row_amount):
        ciphertext += tmatrix[row_index][col_index]

for row in tmatrix:
    for letter_index, char in enumerate(row):
        if (letter_index % key_length) != 0:
            print(char, end="")
        else:
            print(char)
print("Key Length: " + str(key_length))
print("Plaintext: " + plaintext)
print("Ciphertext: " + ciphertext.rstrip())


#Adam Stahly
import random
import math

def populate_matrix(text):
    matrix = [[" " for _ in range(key_length)] for _ in range(row_amount)]
    for letter_index, char in enumerate(text):
        current_row = letter_index // key_length
        current_col = letter_index % key_length
        matrix[current_row][current_col] = char
    return matrix

plaintext = input("Enter the plaintext message: ")
key_length = random.randint(4, 10)
motified_text = plaintext.replace(' ', '')
row_amount = math.ceil(float(len(motified_text)/key_length))
tmatrix = populate_matrix(motified_text)
ciphertext = ""


for col_index in range(key_length):
    for row_index in range(row_amount):
        ciphertext += tmatrix[row_index][col_index]

for row in tmatrix:
    for letter_index, char in enumerate(row):
        if letter_index == key_length - 1:
            print(char)
        else:
            print(char, end="")

print("\nPlaintext: " + plaintext)
print("Ciphertext: " + ciphertext.rstrip())

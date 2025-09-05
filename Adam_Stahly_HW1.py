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

def create_ciphertext():
    cipher_list = []
    for col_index in range(key_length):
        for row_index in range(row_amount):
            cipher_list.append(tmatrix[row_index][col_index])
    return "".join(cipher_list)

plaintext = input("Enter the plaintext message: ")
key_length = random.randint(4, 10)
motified_text = plaintext.replace(' ', '')
row_amount = math.ceil(float(len(motified_text)/key_length))
tmatrix = populate_matrix(motified_text)

ciphertext = create_ciphertext()

for row in tmatrix:
    for letter_index, char in enumerate(row):
        if letter_index == key_length - 1:
            print(char)
        else:
            print(char, end="")

print("\nKey Length: " + str(key_length))
print("Plaintext: " + plaintext)
print("Ciphertext: " + ciphertext.rstrip())

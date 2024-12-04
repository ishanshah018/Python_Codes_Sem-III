# Write a Python program to create a Caesar encryption.

# Note: In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar 
# shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in 
# which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For 
# example, with a right shift of 3, A would be replaced by D, E would become H, and so on. The method is named 
# after Julius Caesar, who used it in his private correspondence.
# For Example:
# Input Text  : LJIET ENG
# Shift : 3
# Cipher:  OMLHW HQJ

text = input("Enter Text: ")
shift = int(input("Enter Shift: "))

cipher = ""  # To store the encrypted text

for char in text:
    if char.isalpha():  # Check if the character is a letter
        if char.isupper():  # For uppercase letters
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:  # For lowercase letters
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        cipher += new_char
    else:
        cipher += char  # Keep spaces or other characters as is

print("Cipher: ", cipher)

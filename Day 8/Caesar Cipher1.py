# This is my logic

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Encryption(plain_text, shift_amount):
    cipher_text = ""
    for i in range(len(plain_text)):
        for j in range(26):
            if plain_text[i] == alphabet[j]:
                shift_index = j + shift_amount
                if shift_index <= 25:
                    cipher_text += alphabet[shift_index]
                else:
                    shift_index -= 26
                    cipher_text += alphabet[shift_index]
    print(f"Your encrypted message is {cipher_text}.")

def Decryption(cipher_text, shift_amount):
    new_plain_text = ""
    for i in range(len(cipher_text)):
        for j in range(26):
            if cipher_text[i] == alphabet[j]:
                shift_index = j - shift_amount
                if shift_index >= 0:
                    new_plain_text += alphabet[shift_index]
                else:
                    shift_index += 26
                    new_plain_text += alphabet[shift_index]
    print(f"Your encrypted message is {new_plain_text}.")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))
if direction == "encode":
    Encryption(text, shift)
elif direction == "decode":
    Decryption(text, shift)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def Decryption(cipher_text, shift_amount):
    plain_text = ""
    for el in cipher_text:
        idx = alphabet.index(el)
        shift_index = idx - shift_amount
        if shift_index >= 0:
            plain_text += alphabet[shift_index]
        else:
            shift_index += 26
            plain_text += alphabet[shift_index]
    print(f"Your decrypted message is {plain_text}.")

def Encryption(plain_text, shift_amount):
    s_amount = shift_amount
    cipher_text = ""
    for el in plain_text:
        idx = alphabet.index(el)
        shift_index = idx + shift_amount
        if shift_index <= 25:
            cipher_text += alphabet[shift_index]
        else:
            shift_index -= 26
            cipher_text += alphabet[shift_index]

    print(f"Your encrypted message is {cipher_text}.")
    decision = input("Do you want to decode this message?y/n ")
    if decision == "y":
        Decryption(cipher_text, s_amount)
    else:
        return

def Caeser(plain_text, shift_amount, decision):
    if direction == "encode":
        Encryption(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        Decryption(cipher_text=text, shift_amount=shift)

Caeser(text, shift, direction)


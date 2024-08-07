import art
print(Art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def CaeserCipher(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for el in start_text:
        position = alphabet.index(el)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Your {cipher_direction}d message is {end_text}.")

CaeserCipher(text, shift, direction)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def CeaserCipher(text, shift):
    end_text = ""
    for el in text:
        position = alphabet.index(el)
        new_position = shift + position
        original_shift = new_position % 26
        end_text += alphabet[original_shift]

    print(end_text)

def decryption(cipher_text, shift):
    end_text =""
    for el in cipher_text:
        position = alphabet.index(el) - shift
        new_position = position % 26
        end_text += alphabet[new_position]
    print(end_text)

CeaserCipher("Hridoy".lower(), 45)
decryption("akbwhr", 45)


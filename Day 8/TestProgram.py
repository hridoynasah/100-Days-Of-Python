alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = "XYZ".lower()
alphaList = []
encrypted_text = ""
shift = 3
for i in range(len(text)):
    for j in range(26):
        if alphabet[j] == text[i]:
            idx = j + shift

            if idx <= 25:
                encrypted_text += alphabet[idx]
            else:
                idx -= 26
                encrypted_text += alphabet[idx]

print(f"Your encrypted message: {encrypted_text}")


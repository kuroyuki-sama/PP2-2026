# 파일 암호화 (p.475)
# a -> D, b -> E, c -> F, ...z -> C
# a : 97, A = 65

key = "abcdefghijklmnopqrstuvwxyz"

def encrypt(n ,plaintext):
    result = ""
    for letter in plaintext:
        try:
            i = (key.index(letter) + n) % 26
            result += key[i].upper()
        except ValueError:
            result += letter

    return result

def decrypt(n, ciphertext):
    result = ""

    for letter in ciphertext:
        try:
            i = (key.index(letter.lower()) - n) % 26
            result += key[i]
        except ValueError:
            result += letter

    return result

n = 3
text = "welcome to python."

print(f"평문 : {text}")
enc = encrypt(n, text)
print(f"암호문 : {encrypt(n, text)}")
print(f"복호문 : {decrypt(n, enc)}")

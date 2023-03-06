S = input()
enc = ''
for char in S:
    if char.islower():
        enc += chr(97+(ord(char)+13-97)%26)
    elif char.isupper():
        enc += chr(65+(ord(char)+13-65)%26)
    else:
        enc += char
print(enc)
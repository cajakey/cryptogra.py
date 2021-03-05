import os
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
while True:
    # settings
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    beta = "SUBDERMATOGLYPHICFJKNQVWXZ"
    rotate = 9
    row = 4
    vinegar = "DADOJULIESITTINGONTHETREEKISSING"
    # main menu
    print("Type [exit] to close the program")
    print("     [encr] to encrypt a plaintext")
    print("     [decr] to decrypt a ciphertext")
    selected = input()
    os.system("cls")
    if selected == "exit" or selected == "EXIT":
        break
    elif selected == "encr" or selected == "ENCR":
        plain = input("Type your plain text: ")
        # character count
        count = 0
        for x in plain:
            if x.isalpha():
                count += 1
        if all(x.isalpha() or x.isspace() for x in plain) and count % 12 == 0:
            plain = plain.upper()
            # encryption
            encrypted = ""
            for x in range(len(plain)):
                for y in range(len(alpha)):
                    if plain[x] == alpha[y]:
                        encrypted += beta[y]
                if plain[x] != " ":
                    # left rotation
                    beta = beta[rotate:] + beta[:rotate]
            # matrix transfer
            z = 0
            w, h = int(len(encrypted) / row), row
            matrix = [['' for x in range(w)] for y in range(h)]
            for x in range(h):
                if z != 0:
                    z += 1
                for y in range(w):
                    matrix[x][y] = encrypted[y + z]
                z += y
            # transposition
            encrypted = ""
            for y in range(w):
                for x in range(h):
                    encrypted += matrix[x][y]
            # vigenere
            cipher_text = []
            key = generateKey(encrypted, vinegar)
            for i in range(len(encrypted)):
                x = (ord(encrypted[i]) + ord(key[i])) % 26
                x += ord('A')
                cipher_text.append(chr(x))
            encrypted = "" . join(cipher_text)
            # result display
            print("\nEncrypted text: ", end="")
            print(*[encrypted[x:x + 3] for x in range(0, len(encrypted), 3)])
            input("\nPress any key to continue...")
            os.system("cls")
        # entry restriction
        else:
            os.system("cls")
            print("Alphabetical letters and spaces only")
            print("Character count must be a multiple of 12\n")
    elif selected == "decr" or selected == "DECR":
        cipher = input("Type your cipher text: ")
        # character count
        count = 0
        for x in cipher:
            if x.isalpha():
                count += 1
        if all(x.isalpha() or x.isspace() for x in cipher) and count % 12 == 0:
            cipher = cipher.upper()
            cipher = cipher.replace(" ", "")
            # vigenere
            orig_text = []
            key = generateKey(cipher, vinegar)
            for i in range(len(cipher)):
                x = (ord(cipher[i]) - ord(key[i]) + 26) % 26
                x += ord('A')
                orig_text.append(chr(x))
            cipher = "" . join(orig_text)
            # matrix transfer
            z = 0
            w, h = row, int(len(cipher) / row)
            matrix = [['' for x in range(w)] for y in range(h)]
            for x in range(h):
                if z != 0:
                    z += 1
                for y in range(w):
                    matrix[x][y] = cipher[y + z]
                z += y
            # transposition
            cipher = ""
            for y in range(w):
                for x in range(h):
                    cipher += matrix[x][y]
            # decryption
            decrypted = ""
            for x in range(len(cipher)):
                for y in range(len(alpha)):
                    if cipher[x] == beta[y]:
                        decrypted += alpha[y]
                beta = beta[rotate:] + beta[:rotate]
            # result display
            print("\nDecrypted text: ", end="")
            print(*[decrypted[x:x + 3] for x in range(0, len(decrypted), 3)])
            input("\nPress any key to continue...")
            os.system("cls")
        # entry restriction
        else:
            os.system("cls")
            print("Alphabetical letters and spaces only")
            print("Character count must be a multiple of 12\n")
    else:
        print("Please try again\n")

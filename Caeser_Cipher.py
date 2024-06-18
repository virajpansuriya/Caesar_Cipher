letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key

    for letter in text:
        if letter.isalpha():
            index = letters.find(letter.lower())
            new_index = (index + key) % num_letters
            if letter.isupper():
                result += letters[new_index].upper()
            else:
                result += letters[new_index]
        else:
            result += letter
    return result

print()
print('*** CAESAR CIPHER PROGRAM ***')
print()

print('Do you want to encrypt or decrypt?')
user_input = input('e/d : ').lower()
print()

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key(1 through 26) : '))
    text = input('Enter the text to encrypt : ')
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f'CIPHERTEXT : {ciphertext}')

elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key(1 through 26) : '))
    text = input('Enter the text to decrypt : ')
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f'PLAINTEXT : {plaintext}')

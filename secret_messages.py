from affine import Affine
from atbash import Atbash
from caesar import Caesar
from keyword_cipher import Keyword

import sys


def create_menu():
    """prompt input for the user (for enc/dec & cipher choice)
    and store the answers to variables within the method.
    """
    option = input('Would you like to encrypt or decrypt your code?(E/D) ')
    option = option.upper()
    if option != 'E' and option != 'D':
        print('Invalid input! Please type E for encrypt, and D for decrypt. ')
        sys.exit(0)
    print('Here is the list of ciphers: ')
    print('1. Affine Cipher')
    print('2. Atbash Cipher')
    print('3. Caesar Cipher')
    print('4. Keyword Cipher')
    print()
    cipher_choice = input('Which cipher would you like to choose?'
                          '(Enter the number) ')
    if cipher_choice not in list('1234'):
        sys.exit(0)
    return option, cipher_choice


def encode(cipher_instance, opt, message):
    """based on the answer encrypt or decrypt the message
     and print the encoded message to the user.
     """
    encoded = cipher_instance.encrypt(message) if opt == 'E' \
        else cipher_instance.decrypt(message)
    print('Your message is: '+encoded)


def choose(cipher, opt, messg):
    """based on the cipher choice call the necessary class
    & call the encode method
    """
    if cipher == '1':
        af = Affine()
        encode(af, opt, messg)
    elif cipher == '2':
        at = Atbash()
        encode(at, opt, messg)
    elif cipher == '3':
        cs = Caesar()
        encode(cs, opt, messg)
    elif cipher == '4':
        key_input = input('What key would you like to use? ')
        kd = Keyword(key=key_input.upper())
        encode(kd, opt, messg)


# prompting the user for the first message and providing the menu
secret_message = input('What message would you like to encrypt/decrypt? ')
option1, cipher_cho = create_menu()
choose(cipher_cho, option1, secret_message)

# continuous loop of communicating to the user until they type 'nope'
while True:
    inp = input('Anything else you want to decrypt or encrypt?'
                '(Nope/type something) ')
    if inp.lower() == 'nope':
        break
    else:
        option2, cipher_cho2 = create_menu()
        choose(cipher_cho2, option2, inp)

import string

from ciphers import Cipher


class Atbash(Cipher):

    atbash_dict = {forward_letter: backward_letter for forward_letter, backward_letter
                   in zip(string.ascii_uppercase, string.ascii_uppercase[::-1])}

    def __init__(self):
        pass

    def encrypt(self, text):
        text = text.upper()
        output = []
        text_list = list(text)
        for letter in text_list:
            output.append(self.atbash_dict.get(letter, letter))
        return ''.join(output)

    def decrypt(self, text):
        return self.encrypt(text)

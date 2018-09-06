import string

from ciphers import Cipher


class Keyword(Cipher):

    def __init__(self, key='PYTHON'):
        self.key = key
        self.arr = self.fill_array(self.key)
        self.keyword_dict = {key_lttr: letter for letter, key_lttr in zip(list(string.ascii_uppercase), self.arr)}

# TODO: YOU SHOULD LOOK UP FOR STATIC METHODS FOR THE METHOD BELOW
    def fill_array(self, key):
        arr = list(key)
        for letter in string.ascii_uppercase:
            if letter not in list(key):
                arr.append(letter)
        return arr

    def encrypt(self, text):
        output = []
        text = text.upper()
        text_list = list(text)
        for char in text_list:
            output.append(self.get_key(char))
        return ''.join(output)

    def decrypt(self, text):
        output = []
        text = text.upper()
        text_list = list(text)
        for char in text_list:
            output.append(self.keyword_dict.get(char, char))
        return ''.join(output)

    def get_key(self, letter):
        for key, value in self.keyword_dict.items():
            if value == letter:
                return key
        return letter  # returns the letter itself in case the letter is a non-alpha element


kd = Keyword()
print(kd.encrypt('sena is the number 1 programmer and freelancer in the world !!! @ # '))
print(kd.decrypt('QOIP CQ RBO ISGYOM 1 KMJAMPGGOM PIH NMOOFPITOM CI RBO VJMFH !!! @ # '))

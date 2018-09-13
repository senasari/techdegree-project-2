import string

from ciphers import Cipher


class Keyword(Cipher):
    """keyword cipher encrypts the data by matching the letter with a letter in a special alphabet
    which starts with the keyword that was given & for decryption vice versa.
    """

    def __init__(self, key):
        self.key = key
        self.arr = Keyword.fill_array(self.key)
        self.keyword_dict = {key_lttr: letter for letter, key_lttr in zip(list(string.ascii_uppercase), self.arr)}

    @staticmethod
    def fill_array(key):
        """creates an array according to the key for creating a dictionary for keyword cipher encryption purposes"""
        arr = list(key)
        for letter in string.ascii_uppercase:
            if letter not in list(key):
                arr.append(letter)
        return arr

    def encrypt(self, text):
        """encrypts the text based on keyword cipher encryption method"""
        output = []
        text = text.upper()
        text_list = list(text)
        for char in text_list:
            output.append(self.get_key(char))
        return ''.join(output)

    def decrypt(self, text):
        """decrypts the formally encrypted text based on keyword cipher encryption method"""
        output = []
        text = text.upper()
        text_list = list(text)
        for char in text_list:
            output.append(self.keyword_dict.get(char, char))
        return ''.join(output)

    def get_key(self, letter):
        """creating a method for getting the key in the dictionary when the value is given."""
        for key, value in self.keyword_dict.items():
            if value == letter:
                return key
        return letter  # returns the letter itself in case the letter is a non-alpha element

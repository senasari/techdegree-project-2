import string

from ciphers import Cipher


class Atbash(Cipher):
    """atbash cipher encrypts the data by replacing the letter with the corresponding letter in the reversed alphabet
    -for decryption vice versa"""

    atbash_dict = {forward_letter: backward_letter for forward_letter, backward_letter
                   in zip(string.ascii_uppercase, string.ascii_uppercase[::-1])}

    def encrypt(self, text):
        """encrypts the text based on atbash encryption method"""
        text = text.upper()
        output = []
        text_list = list(text)
        for letter in text_list:
            output.append(self.atbash_dict.get(letter, letter))
        return ''.join(output)

    def decrypt(self, text):
        """decrypts the formally encrypted text based on caesar encryption method
         -which is the same process with encrypting the text
         """
        return self.encrypt(text)

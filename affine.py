import string

from ciphers import Cipher


class Affine(Cipher):

    affine_dict = {number: letter for letter, number in zip(string.ascii_uppercase, range(0, 26))}

    def __init__(self, coefficient=3, plus_nmbr=10, alpha_count=26):
        self.coefficient = coefficient
        self.plus_nmbr = plus_nmbr
        self.alpha_count = alpha_count

    def encrypt(self, text):
        output = []
        text = text.upper()
        text_list = list(text)
        for member in text_list:
            count = self.get_nmbr(member)
            if count != member:
                count = self.coefficient*count + self.plus_nmbr
                count = count % self.alpha_count
                count = self.affine_dict.get(count)
            output.append(count)
        return ''.join(output)

    def decrypt(self, text):
        output = []
        text = text.upper()
        text_list = list(text)
        for member in text_list:
            count = self.get_nmbr(member)
            if count != member:
                count -= self.plus_nmbr
                i = 1
                while True:
                    if (i*self.alpha_count + count) % self.coefficient == 0:
                        count = ((i*self.alpha_count + count) / self.coefficient) % self.alpha_count
                        count = self.affine_dict.get(count)
                        break
                    else:
                        i += 1
            output.append(count)
        return ''.join(output)

    def get_nmbr(self, value):
        for nmbr, lttr in self.affine_dict.items():
            if lttr == value:
                return nmbr
        else:
            return value

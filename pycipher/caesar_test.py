#implements Caesar substitution cipher
#Author: James Lyons 
#Created: 2012-04-28

from .base import Cipher

class Caesar_test(Cipher):
    """The Caesar Cipher has a key consisting of an integer 1-25.
    This cipher encrypts a letter according to the following equation::
    
        c = (p + key)%26
        
    where c is the ciphertext letter, p the plaintext letter.
    For more details on the Caesar cipher, see http://www.practicalcryptography.com/ciphers/caesar-cipher/
    
    :param key: The additive key. Allowable values are integers 0-25.
    """       
    
    def __init__(self,cipher_or_key):
        if type(cipher_or_key) is int:
            self.key = cipher_or_key % 26
        if type(cipher_or_key) is str:
            self.cipher = cipher_or_key
        
    def encipher(self,cipher_or_key,keep_punct=False):
        """Encipher string using Caesar cipher according to initialised key.

        Example::

            ciphertext = Caesar(3).encipher(plaintext)     

        :param string: The string to encipher.
        :param keep_punct: if true, punctuation and spacing are retained. If false, it is all removed. Default is False. 
        :returns: The enciphered string.
        """        
        if type(cipher_or_key) is int:
            self.key = cipher_or_key % 26

        if type(cipher_or_key) is str:
            if not keep_punct: cipher_or_key = self.remove_punctuation(cipher_or_key)
            self.cipher = cipher_or_key        

        ret = ''
        for c in self.cipher:
            if c.isalpha(): ret += self.i2a( self.a2i(c) + self.key )
            else: ret += c
        return ret    

    def decipher(self,cipher_or_key,keep_punct=False):
        r"""Decipher string using Caesar cipher according to initialised key.

        Example::

            plaintext = Caesar(3).decipher(ciphertext)     

        :param string: The string to decipher.
        :param keep_punct: if true, punctuation and spacing are retained. If false, it is all removed. Default is False. 
        :returns: The deciphered string.
        """
        if type(cipher_or_key) is int:
            self.key = cipher_or_key % 26
        if type(cipher_or_key) is str:
            if not keep_punct: cipher_or_key = self.remove_punctuation(cipher_or_key)
            self.cipher = cipher_or_key
        
        ret = ''
        for c in self.cipher:
            if c.isalpha(): ret += self.i2a( self.a2i(c) - self.key )
            else: ret += c
        return ret
                
if __name__ == '__main__': 
    print 'use "import pycipher" to access functions'

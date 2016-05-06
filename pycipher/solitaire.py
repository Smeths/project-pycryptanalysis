# Solitaire cipher

from .base import Cipher

class Solitaire(Cipher):

# Reading in cipher and converting to numbers

# letter to number conversion dictionary

    def __init__(self,cipher_text):

        self.l2n = {'a': 1,  'b': 2,  'c': 3,  'd': 4,  'e': 5,  'f': 6,  'g': 7,
                    'h': 8,  'i': 9,  'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 
                    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 
                    'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

        self.n2l = { 1 :'a', 2 :'b', 3 :'c', 4 :'d', 5 :'e', 6 :'f', 7 :'g', 
                     8 :'h', 9 :'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 
                     15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 
                     22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

        self.cipher_text = cipher_text.lower()
        self.cipher_num = [self.l2n[letter] for letter in self.cipher_text]
        self.plain_num = [100]*len(self.cipher_text)
        self.debug = 0

# Cipher key parameters

        self.ja_value = 53
        self.jb_value = 54
        self.last_card_index = 53

        if self.debug == 1:
            print "initial key"
            print key[0:54]

# Loop over the cipher number list

    def decipher(self,key):
        for i in range(0,len(self.cipher_text)):
            if self.debug == 1:
                print "##############################################"
                print "loop"
                print i
                print "##############################################"
            key_number = 0
################################################
# Generating key stream                        #
################################################
            while key_number == 0:
# Move Jokers
# Move joker A 
                ja_index = key.index(self.ja_value)
                if ja_index == self.last_card_index:
# move cards down to make space for joker
                    key[2:54] = key[1:53]
# insert joker at second position
                    key[1] = ja_value   
                else:
                    key[ja_index] = key[ja_index + 1]
                    key[ja_index + 1] = self.ja_value
# Move joker B
                jb_index = key.index(self.jb_value)
                if jb_index == self.last_card_index:
# move cards down to make space for joker
                    key[3:54] = key[2:53] 
                    key[2] = self.jb_value
                elif jb_index == self.last_card_index - 1:
                    key[2:53] = key[1:52]
                    key[1] = self.jb_value
                else:
                    key[jb_index:jb_index + 2] = key[jb_index + 1:jb_index + 3]
                    key[jb_index+2] = self.jb_value
                if self.debug == 1:
                    print "key after joker move"
                    print key
# Triple cut
# locating first and second joker
                j1_index = min(key.index(self.ja_value),key.index(self.jb_value))
                j2_index = max(key.index(self.ja_value),key.index(self.jb_value))
                key_old = key
# performing triple cut
                key = key_old[j2_index+1:54] + [key_old[j1_index]] + \
                key_old[j1_index + 1:j2_index] + [key_old[j2_index]] + \
                key_old[0:j1_index]
                if self.debug == 1:
                    print "key after triple cut"
                    print key
# Count cut
                cut_index = key[53]
                if cut_index == 54:
                    cut_index = 53
                key_old = key
# performing count cut
                key = key_old[cut_index:53] + key_old[0:cut_index] + [key_old[53]]
                if self.debug == 1:
                    print "key after count cut"
                    print key
# Output card and modular arithmetic
                top_index = key[0]
                if top_index == 54:
                    top_index = 53
                output_card = key[top_index] 
                if output_card == 52:
                    key_number = 26
                elif output_card == 53 or output_card ==54:
                    key_number = 0
                elif output_card > 26:
                    key_number = output_card%26
                else:
                    key_number = output_card
################################################
# Encrypting letter                            #
################################################
            self.plain_num[i] = self.cipher_num[i] - key_number
            if self.plain_num[i] == 0:
                self.plain_num[i] = 26
            elif self.plain_num[i] < 0:
                self.plain_num[i] = 26 + self.plain_num[i]
################################################
# Putting plain text together                  #
################################################
        plain_list = [self.n2l[number] for number in self.plain_num]
        plain_text = ''.join(plain_list)
        return plain_text
        if debug == 1:
            print plain_text
    
       

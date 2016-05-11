from pycipher import ColTrans
from pycryptanalysis import ngram
from pycryptanalysis import clean_cipher
from itertools import permutations

# opening and clean the cipher

cipher_address = 'ciphers/plaintext.txt'
cipher_file = open(cipher_address,'r')
cipher_str = cipher_file.read()
cipher_str = clean_cipher().run(cipher_str)

# enciphering using columnar transposition

pt_encipher = ColTrans(keyword="FRED").encipher(cipher_str)

# Using ngram test to decipher

quadgrams = ngram("quadgrams.txt")
bestscore = -1000000

for perm in permutations(["A","B","C","D"],4):
    test_key = ''.join(list(perm))
    pt_decipher = ColTrans(test_key).decipher(pt_encipher)
    score = quadgrams.run(pt_decipher)
    if score > bestscore:
       decipher = pt_decipher
       key = test_key
       bestscore = score

print decipher
print key

       









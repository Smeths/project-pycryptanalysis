from pycipher import ColTrans_test
from pycryptanalysis import ngram
from pycryptanalysis import clean_cipher
from itertools import permutations

# opening and clean the cipher

cipher_address = 'ciphers/plaintext.txt'
cipher_file = open(cipher_address,'r')
cipher_str = cipher_file.read()
cipher = clean_cipher().run(cipher_str)

# enciphering using columnar transposition

encipher = ColTrans_test(keyword="FRED").encipher(cipher)

# initialising col transposition

col = ColTrans_test(cipher=encipher)

# initialising the ngram test

quadgrams = ngram("quadgrams.txt")
bestscore = -1000000

for perm in permutations(["A","B","C","D"],4):
    test_key = ''.join(list(perm))
    decipher = col.decipher(test_key)
    score = quadgrams.run(decipher)
    if score > bestscore:
       deciphered = decipher
       key = test_key
       bestscore = score

print deciphered
print key

       









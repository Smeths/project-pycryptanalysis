from pycipher import ColTrans
from pycryptanalysis import ngram
from pycryptanalysis import clean_cipher
from itertools import permutations

# opening the plain text file

pt_address = "ciphers/plaintext.txt"
pt_file = open(pt_address,'r')
pt_str = pt_file.read()

# removing non-alphabetic and non-numerical characters

clean = clean_cipher()
pt_str = clean.run(pt_str)

# enciphering using columnar transposition

col = ColTrans("FRED")
pt_encipher = col.encipher(pt_str)

# Using ngram test to decipher

quadgrams = ngram("quadgrams.txt")
bestscore = -1000000

for perm in permutations(["A","B","C","D"],4):
    test_key = ''.join(list(perm))
    col_decipher = ColTrans(test_key)
    pt_decipher = col_decipher.decipher(pt_encipher)
    score = quadgrams.run(pt_decipher)
    if score > bestscore:
       decipher = pt_decipher
       key = test_key
       bestscore = score

print decipher
print key

       









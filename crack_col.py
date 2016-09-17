from pycipher import ColTrans_test
from pycryptanalysis import ngram
from pycryptanalysis import clean_cipher
from itertools import permutations

# opening and clean the cipher

cipher_address = 'ciphers/columnar.txt'
cipher_file = open(cipher_address,'r')
cipher_str = cipher_file.read()
cipher = clean_cipher().run(cipher_str)

# initialising col transposition

col = ColTrans_test(cipher=cipher)

# initialising the ngram test

quadgrams = ngram("quadgrams.txt")
bestscore = -1000000

for perm in permutations(["A","B","C","D","E"],5):
    test_key = ''.join(list(perm))
    decipher = col.decipher(test_key)
    score = quadgrams.run(decipher)
    if score > bestscore:
       deciphered = decipher
       key = test_key
       bestscore = score

print deciphered
print key

       









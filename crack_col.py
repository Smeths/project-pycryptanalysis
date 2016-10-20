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
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
         "P","Q","R","S","T","U","V","W","X","Y","Z"]

for i in range(1,7):
    print alpha[0:i],i
    for perm in permutations(alpha[0:i],i):
        test_key = ''.join(list(perm))
        decipher = col.decipher(test_key)
        score = quadgrams.run(decipher)
        if score > bestscore:
            deciphered = decipher
            key = test_key
            bestscore = score

print deciphered
print key

       









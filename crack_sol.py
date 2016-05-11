from pycipher import Solitaire
from pycryptanalysis import ngram
from pycryptanalysis import clean_cipher

# Initialising cipher

cipher_address = 'ciphers/challenges/2015/challenge8b.txt'
cipher_file = open(cipher_address,'r')
cipher_str = cipher_file.read()
cipher_str = clean_cipher().run(cipher_str)
sol = Solitaire(cipher_str)

# Opening key file
key_file = open("key.lis", "r")

# Initialising cipher test

quadgrams = ngram("quadgrams.txt")
bestscore = -1000000

for i in range(0,40320):
    key_str = key_file.readline()
    key = [int(string) for string in key_str.split(",")]
    plain_text = sol.decipher(key)
    plain_text = plain_text.upper()
    score = quadgrams.run(plain_text)   
    if score >= bestscore:
        bestscore = score
        print i  
        print score
        print plain_text

    

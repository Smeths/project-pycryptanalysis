# loading modules

from pycryptanalysis import chi_squared
from pycryptanalysis import clean_cipher
from pycipher import Caesar

# opening and cleaning a cipher

cipher_address = 'ciphers/challenges/2014/challenge1A.txt'
cipher_file = open(cipher_address,'r')
cipher_str = cipher_file.read()

clean = clean_cipher()
cipher_clean = clean.run(cipher_str)
chi = chi_squared()

# initialising chi squared test

chi_large = 5000.0

for i in xrange(0,25):
    decipher = Caesar(key=i).decipher(cipher_clean)
    chi_stat = chi.run(decipher.lower())
    if chi_stat < chi_large:
       deciphered = decipher
       key = i
       chi_large = chi_stat

print deciphered
print key

#remove this code, inserted as a quick check for the incidence of 
#coincidence and the ngram module

from pycryptanalysis import inc_of_coin
from pycryptanalysis import ngram

ioc = inc_of_coin()
print ioc.run(cipher_clean)

quadgram = ngram('quadgrams.txt')
print quadgram.run(cipher_clean)








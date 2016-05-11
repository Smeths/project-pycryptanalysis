# loading modules

from pycryptanalysis import chi_squared
from pycryptanalysis import clean_cipher
from pycipher import Caesar

# opening and cleaning a cipher

cipher_address = 'ciphers/challenges/2014/challenge1A.txt'
cipher_file = open(cipher_address,'r')
cipher_str = cipher_file.read()
cipher_str = clean_cipher().run(cipher_str)

# initialising chi squared test

chi = chi_squared(0)
chi_large = 5000.0

for i in xrange(0,26):
    decipher = Caesar(i).decipher(cipher_str)
    chi_stat = chi.run(decipher.lower())
    if chi_stat < chi_large:
       deciphered = decipher
       key = i
       chi_large = chi_stat

# print decipher and key

print deciphered
print key







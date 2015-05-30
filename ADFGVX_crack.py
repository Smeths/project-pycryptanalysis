from pycipher import ADFGVX
from pycipher import ColTrans
from pycryptanalysis import clean_cipher
from pycryptanalysis import chi_squared
from itertools import permutations
import sys

# opening the plain text file

pt_address = "ciphers/plaintext.txt"
pt_file = open(pt_address,'r')
pt_str = pt_file.read()

# removing non-alphabetic and non-numerical characters

clean = clean_cipher()
chi = chi_squared(1)
pt_str = clean.run(pt_str)

# enciphering using the ADFGVX cipher

adfgvx = ADFGVX('ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8','HELLO')
pt_encipher = adfgvx.encipher(pt_str)

# defining a ADFGVX matrix

ADFGVX_mat = [ "AA","AD","AF","AG","AV","AX", \
               "DA","DD","DF","DG","DV","DX", \
               "FA","FD","FF","FG","FV","FX", \
               "GA","GD","GF","GG","GV","GX", \
               "VA","VD","VF","VG","VV","VX", \
               "XA","XD","XF","XG","XV","XX"]

# Selecting number of columns from user input

colsize = int(float(sys.argv[1]))
alpha = chi.alphabet[0:colsize]
alpha_ordered = chi.alphabet_ordered + ["0","1","2","3","4","5","6","7","8","9"]

# Create frequency dictionary for ADFGVX bigrams

ADFGVX_dict = {}

# Set tolerance for the chi squared test
chi_max = 10000

for perm in permutations(alpha,colsize):
# Initialise frequency dictionary to 0
    for XX in ADFGVX_mat:
        ADFGVX_dict[XX] = 0
# Perform columnar transposition part of decryption
    test_key = ''.join(list(perm))
    pt_decipher = ColTrans(test_key).decipher(pt_encipher)
# Create dictionary of ADFGVX bigrams matrix and frequencies
    for n in xrange(0,len(pt_encipher)/2):
        ADFGVX_dict[pt_decipher[2*n:2*n + 2]] = ADFGVX_dict[pt_decipher[2*n:2*n + 2]] + 1
# Substitute most frequent letters for most frequent bigrams
    i = 0
    for XX in sorted(ADFGVX_dict, key=ADFGVX_dict.get, reverse=True):
        ADFGVX_dict[XX] = alpha_ordered[i]
        i = i + 1
# Perform letter substitution part of decryption 
    pt_decipher_2 = ""
    for n in xrange(0,len(pt_encipher)/2):
        pt_decipher_2 += ADFGVX_dict[pt_decipher[2*n:2*n + 2]]

# Perform chi squared test  
    chi_current = chi.run(pt_decipher_2)

    if chi_current < chi_max:
        chi_max = chi_current
        pt_deciphered = pt_decipher_2
        key = test_key

print pt_deciphered
print chi_max
print key
    





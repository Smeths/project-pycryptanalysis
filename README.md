#Main area:

A collection of routines for the 'brute force' cracking of classic ciphers

##pycryptanalysis:

A python package containing a collection of cryptoanalytic tests

###tests.py 

contains the following classes each of which are a cryptoanalytic tests
####chi_squared 
chi squared test
can be an 'order test' where by the frequencies are put in order (useful 
for identifying hidden substitution ciphers). Option must be identified
upon instantiation with either chi_squared(0) or chi_squared(1)
####inc_of_coin
incidence of coincidence
####clean_cipher
removes any non alphabetic or number characters

##pycipher:

A package for enciphering and deciphering classic ciphers. contains most of the classic
ciphers and has been cloned from github

###ngram.py

trigram,quadgram etc frequency test

##ciphers:

A collection of classic ciphers for cracking

##data:

data needed for the ngram tests in the pycryptanalysis package








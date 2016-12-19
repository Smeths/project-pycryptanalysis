7B is a bifid cipher as can be hinted at by the fact there is no 'j' in the text.

I have written a python script (bifid_period.py) to determine the period in line with the cryptanalysis hints provided at practical cryptography website.

This determines the period to be 4

The practical cryptography website has a cracker for the bifid cipher, which uses simulated annealing and brute force techniques.

However there is a bug in the c code, which means it doesn't work for bifid ciphers with an even period. 

I have modified the source code to rectify this (bifidcrack_even.c)

The 2016 7B cipher has been copied into the code.

The modified c program seems to work however it failed on the last 3 characters of the cipher. Noting the key and using the decipher tool at the practical cryptography website gets around this problem.





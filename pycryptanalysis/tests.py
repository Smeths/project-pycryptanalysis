class crypt_consts:

    def __init__(self):

       self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m', \
                        'n','o','p','q','r','s','t','u','v','w','x','y','z']
       self.alphabet_probs = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228, \
                              0.02015,0.06094,0.06966,0.00153,0.00772,0.04025, \
                              0.02406,0.06749,0.07507,0.01929,0.00095,0.05987, \
                              0.06327,0.09056,0.02758,0.00978,0.02360,0.00150, \
                              0.01974,0.00074]

class chi_squared(crypt_consts):

    def run(self,cipher):
        
        cipher = cipher.lower()
          
        cipher_len = len(cipher)

        # Calculate expected quantity of each letter

        exp_letter_freqs = [i * cipher_len for i in self.alphabet_probs] 

        chi = 0

        for i in range(0,26):
            chi = chi + ((cipher.count(self.alphabet[i]) - exp_letter_freqs[i])**2)/exp_letter_freqs[i]

        return chi

class inc_of_coin(crypt_consts):

    def run(self,cipher):

        sum=0.0
        n = len(cipher)
        cipher = cipher.lower()

        for i in xrange(0,25):
            f= cipher.count(self.alphabet[i])
            sum=sum+f*(f-1)

        ioc = sum/(n*(n-1))

        return ioc

class clean_cipher():

    def run(self,cipher):

        clean = ""

        for i in xrange(len(cipher)):
            if (ord(cipher[i]) > 47 and ord(cipher[i]) < 58) or \
               (ord(cipher[i]) > 64 and ord(cipher[i]) < 91) or \
               (ord(cipher[i]) > 96 and ord(cipher[i]) < 123):
                char = cipher[i].lower()
                clean+=char

        return clean




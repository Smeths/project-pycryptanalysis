class crypt_consts:

    def __init__(self):

       self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m', \
                        'n','o','p','q','r','s','t','u','v','w','x','y','z']

       self.alphabet_ordered = [ "e","t","a","o","i","n", \
                                 "s","h","r","d","l","c", \
                                 "u","m","w","f","g","y", \
                                 "p","b","v","k","j","x", \
                                 "q","z"]

       self.alphabet_probs = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228, \
                              0.02015,0.06094,0.06966,0.00153,0.00772,0.04025, \
                              0.02406,0.06749,0.07507,0.01929,0.00095,0.05987, \
                              0.06327,0.09056,0.02758,0.00978,0.02360,0.00150, \
                              0.01974,0.00074]

       self.sum_prob_squared = 0.0654966995

class chi_squared(crypt_consts):

    def __init__(self,ordered_test):

       crypt_consts.__init__(self)

       if ordered_test == 0:
           self.ordered = 0
       else:
           self.ordered = 1

    def run(self,cipher):
        
        cipher = cipher.lower()          
        cipher_len = len(cipher)

        # Calculate expected quantity of each letter

        exp_letter_freqs = [i * cipher_len for i in self.alphabet_probs]

        # Calculating actual quantity of each letter

        act_letter_freqs = [cipher.count(self.alphabet[i]) for i in xrange(0,26)]

        if self.ordered == 1:
            exp_letter_freqs = sorted(exp_letter_freqs)
            act_letter_freqs = sorted(act_letter_freqs)
            
        chi = 0
        sum = 0

        # Ordering letter
        for i in xrange(0,26):
            chi = chi + ((act_letter_freqs[i] - exp_letter_freqs[i])**2)/exp_letter_freqs[i]            

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




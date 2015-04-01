from crypt_const import crypt_const

class chi_squared(crypt_const):

    def __init__(self):
        crypt_const.__init__(self)
    
    def stat(self,cipher):
        
        cipher_len = len(cipher);

        # Calculate expected quantity of each letter

        exp_letter_freqs = [i * cipher_len for i in self.letter_probs] 

        chi = 0

        for i in range(0,26):
            chi = chi + ((cipher.count(self.alphabet[i]) - exp_letter_freqs[i])**2)/exp_letter_freqs[i]

        return chi


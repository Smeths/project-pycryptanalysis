from crypt_const import crypt_const

class cipher(crypt_const):

    def __init__(self,cipher):

        crypt_const.__init__(self)
        self.cipher_orig = cipher

        # Loop over cipher and eliminate any non letters

        clean = ""

        for i in xrange(len(cipher)):
            if (ord(cipher[i]) > 64 and ord(cipher[i]) < 91) or \
               (ord(cipher[i]) > 96 and ord(cipher[i]) < 123):
                char = cipher[i].lower()
                clean+=char

        self.cipher_clean = clean

    def report(self):
        return len(self.cipher_clean)


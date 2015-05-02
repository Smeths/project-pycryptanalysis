class clean_cipher:

    def stat(self,cipher):
        
        clean = ""

        # Loop over cipher and eliminate any non letter

        for i in xrange(len(cipher)):
            if (ord(cipher[i]) > 64 and ord(cipher[i]) < 91) or \
               (ord(cipher[i]) > 96 and ord(cipher[i]) < 123):
                char = cipher[i].upper()
                clean+=char
 
        return clean


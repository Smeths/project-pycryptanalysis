from itertools import permutations

#Intialising key

c2n = {'1C':1 ,'2C':2 ,'3C': 3,'4C': 4,'5C': 5,'6C': 6,'7C': 7, \
       '8C':8 ,'9C':9 ,'10C':10,'JC':11,'QC':12,'KC':13, \
       '1D':14,'2D':15,'3D':16,'4D':17,'5D':18,'6D':19,'7D':20, \
       '8D':21,'9D':22,'10D':23,'JD':24,'QD':25,'KD':26, \
       '1H':27,'2H':28,'3H':29,'4H':30,'5H':31,'6H':32,'7H':33, \
       '8H':34,'9H':35,'10H':36,'JH':37,'QH':38,'KH':39, \
       '1S':40,'2S':41,'3S':42,'4S':43,'5S':44,'6S':45,'7S':46, \
       '8S':47,'9S':48,'10S':49,'JS':50,'QS':51,'KS':52,'JA':53,'JB':54 }  

cards = ["KH","9H","8S","4C","5C","3S", \
         "4D","KS","7D","KC","JA","3D", \
         "4H","1S","QH","8H","4S","1D", \
         "2S","7C","1H","5S","1C","6C", \
         "7H","2D","JB","10H","5D","JD", \
         "3C","9C","QS","JH","10D","7S", \
         "7S","10C","10C","6D","6D","6D", \
         "6S","QD","QD","2C","9D","9D", \
         "5H","5H","6H","JC","3H","3H"]

key = [str(c2n[card]) for card in cards]

for perm in permutations([8,12,21,26,28,48,49,50]):
# Assigning permutation
    key[36] = str(perm[0])
    key[38] = str(perm[1])
    key[40] = str(perm[2])
    key[41] = str(perm[3])
    key[44] = str(perm[4])
    key[47] = str(perm[5])
    key[49] = str(perm[6])
    key[53] = str(perm[7])
    key_str = ', '.join(key)
    print key_str
    


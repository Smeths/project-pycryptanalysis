# Importing files

import ngram_score_1 as ns

# Opening files

filename = "decipher_first175.txt"
decipher = open(filename,'w')
cipher = open("first175_combs.txt")

# Initialising ngram test

fitness = ns.ngram_score('quadgrams.txt')
fs_max = -105

# Number of deciphered messages to look at 

for h in range(1,841):

    print("At combination")
    print(h)

    col1_init = cipher.readline()
    col1_init = col1_init.strip()
    col1_init = col1_init.upper()

    col2_init = cipher.readline()
    col2_init = col2_init.strip()
    col2_init = col2_init.upper()

    col3_init = cipher.readline()
    col3_init = col3_init.strip()
    col3_init = col3_init.upper()

    col4_init = cipher.readline()
    col4_init = col4_init.strip()
    col4_init = col4_init.upper() 
 

    loopmax = 26
 
    for i in range(1,2):
        col1_cycle = col1_init[i-1:] + col1_init[:i-1]
        for j in range(1,loopmax):
            col2_cycle = col2_init[j-1:] + col2_init[:j-1]
            for k in range(1,loopmax):
                col3_cycle = col3_init[k-1:] + col3_init[:k-1]
                for l in range(1,loopmax):
                    col4_cycle = col4_init[l-1:] + col4_init[:l-1]
#                    for m in range(1,2):
#                        col5_cycle = col5_init[m-1:] + col5_init[:m-1]
#                        for n in range(1,2):
#                            col6_cycle = col6_init[n-1:] \
#                                       + col6_init[:n-1]
#                            for o in range(1,2):
#                                col7_cycle = col7_init[o-1:] \
#                                           + col7_init[:o-1]
                    fs = 0.0
                    text = ""
                    for p in range(1,26):
                        decipher_text = col1_cycle[p-1:p] \
                                  + col2_cycle[p-1:p] \
                                  + col3_cycle[p-1:p] \
                                  + col4_cycle[p-1:p]
                        fs = fitness.score(decipher_text) + fs
                        text = text + decipher_text + "\n"

                    if fs > fs_max:
                        decipher.write("At combination")
                        decipher.write("\n")
                        decipher.write(str(h))
                        decipher.write("\n")                                    
                        decipher.write("With Fitness Score")
                        decipher.write("\n")
                        decipher.write(str(fs))
                        decipher.write("\n")
                        decipher.write("Cycle")
                        decipher.write("\n")
                        decipher.write(str(i))
                        decipher.write("\n")
                        decipher.write(str(j))
                        decipher.write("\n")
                        decipher.write(str(k))
                        decipher.write("\n")
                        decipher.write(text)
                        decipher.write("\n")
                     

                         
decipher.close()
cipher.close()

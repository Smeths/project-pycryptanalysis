from pycryptanalysis import ngram
fitness = ngram("quadgrams.txt")
fs_max = -100000
quadscore = -536
triscore = -385

cipher = open("first175_combs.txt","r")
decipher = open("decipher.txt","w")
dec_count = 0

for i in range(1,25):

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

    print("Reading col set")
    print(i)

    for i in range(1,26):
        col1_cycle = col1_init[i-1:] + col1_init[:i-1]
        for j in range(1,26):
            col2_cycle = col2_init[j-1:] + col2_init[:j-1]
            for k in range(1,26):
                col3_cycle = col3_init[k-1:] + col3_init[:k-1]
                for l in range(1,26):
                    col4_cycle = col4_init[l-1:] + col4_init[:l-1]
                    decipher_text = ""
                    for m in range(1,26):
                        decipher_text = decipher_text + col1_cycle[m-1:m] \
                               + col2_cycle[m-1:m] \
                               + col3_cycle[m-1:m] \
                               + col4_cycle[m-1:m]
                    fs = fitness.run(decipher_text)
                    if fs > fs_max:
                        fs_max = fs
                        decipher.write(str(fs_max))
                        decipher.write("\n")
                        decipher.write(decipher_text)
                        decipher.write("\n")
                        decipher.write("\n")
                        dec_count = dec_count + 1                       
#                    if 
#                    cthe = decipher_text.count("THE")
#                    cand = decipher_text.count("AND")
#                    if cthe > 0 and cand > 0:
#                        decipher.write(decipher_text)
#                        decipher.write("\n")
#                        decipher.write("\n")

                         
print("possible deciphers")
print(dec_count)
decipher.close()
cipher.close()

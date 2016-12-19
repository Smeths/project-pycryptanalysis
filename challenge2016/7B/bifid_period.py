def bivar(step):
    f = open('cipher_3.txt', 'r')
    cipher_str = f.read()
    cipher_len = len(cipher_str)
    f.close()

    bigrams = []
    bigrams_uniq = []
    bigrams_count = []
    bigrams_countsq = []

    for i in range(0, cipher_len-2-step):
        j = i + 1 + step
        bigram = cipher_str[i] + cipher_str[j]
        bigrams.append(bigram)

    for i in range(0,cipher_len-2-step):
        bigram = bigrams[i]
        present = bigram in bigrams_uniq
        if not present:
            num = bigrams.count(bigram)
            bigrams_uniq.append(bigram)
            bigrams_count.append(num)
            bigrams_countsq.append(num*num)

    bimean = sum(bigrams_count)/len(bigrams_count)
    bivar = sum(bigrams_countsq)/len(bigrams_count) - bimean*bimean

    print bivar


bivar(0)
bivar(1)
bivar(2)
bivar(3)
bivar(4)
bivar(5)
bivar(6)
bivar(7)
bivar(8)
bivar(9)
bivar(10)
bivar(11)
bivar(12)
bivar(13)
bivar(14)
bivar(15)
bivar(16)






 




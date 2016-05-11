import itertools as it

# first 175 combs

outfile = open("first175_combs.txt",'w')
infile = open("first175.txt",'r')

col = []
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
for x in it.permutations('0123456',4):
    outfile.write(col[int(x[0])])
    outfile.write(col[int(x[1])])
    outfile.write(col[int(x[2])])
    outfile.write(col[int(x[3])])
#    outfile.write(col[int(x[4])])
#    outfile.write(col[int(x[5])])
#    outfile.write(col[int(x[6])])

outfile.close()
infile.close()

# second 175 combs

outfile = open("second175_combs.txt",'w')
infile = open("second175.txt",'r')

col = []
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())

for x in it.permutations('0123456',4):
    outfile.write(col[int(x[0])])
    outfile.write(col[int(x[1])])
    outfile.write(col[int(x[2])])
    outfile.write(col[int(x[3])])
#    outfile.write(col[int(x[4])])
#    outfile.write(col[int(x[5])])
#    outfile.write(col[int(x[6])])

outfile.close()
infile.close()

outfile = open("third175_combs.txt",'w')
infile = open("third175.txt",'r')

col = []
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())

for x in it.permutations('0123456',4):
    outfile.write(col[int(x[0])])
    outfile.write(col[int(x[1])])
    outfile.write(col[int(x[2])])
    outfile.write(col[int(x[3])])
#    outfile.write(col[int(x[4])])
#    outfile.write(col[int(x[5])])
#    outfile.write(col[int(x[6])])

outfile.close()
infile.close()


outfile = open("fourth175_combs.txt",'w')
infile = open("fourth175.txt",'r')

col = []
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())
col.append(infile.readline())

for x in it.permutations('0123456',4):
    outfile.write(col[int(x[0])])
    outfile.write(col[int(x[1])])
    outfile.write(col[int(x[2])])
    outfile.write(col[int(x[3])])
#    outfile.write(col[int(x[4])])
#    outfile.write(col[int(x[5])])
#    outfile.write(col[int(x[6])])

outfile.close()
infile.close()






    
    

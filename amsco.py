from pycryptanalysis import ngram_score

cipher = 'EFGF'

ns = ngram_score('quadgrams.txt')
fs = ns.score(cipher)

print fs


from pycryptanalysis import chi_squared
from pycipher import Caesar

chi = chi_squared()
chi_old = 2000
cipher = 'EFGFOEUIFFBTUXBMMPGUIFDBTUMF'

for i in range(1,27):
    decipher = Caesar(key=i).decipher(cipher)
    chi_new = chi.stat(decipher)
    if chi_new < chi_old:
        decipher_final = decipher
        key = i
        chi_old = chi_new

print decipher_final
print key
print chi_old


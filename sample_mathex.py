from Mathex import *

string1 = Mathex('-1x^7+2x^5-15.1x^2+1030')

print string1.get_terms()
print string1.get_coeffs_and_exponents()
print string1.get_exponents()
print '========='
print string1.get_complete_coeffs()

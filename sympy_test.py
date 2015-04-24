##from sympy import *
##
##x = symbols('x')
##expr = poly('32*x**5 + 2*x + 2')
##expr2 = poly('-14*x**5 + 14*x**3 + -3*x + 5')
##
##plus = expr + expr2
####print expr
####print expr.all_coeffs()
##
##print plus
##print plus.all_coeffs()

from sympy import *
from mathex_format import Mathex

##for idx, char in enumerate('32x5 + 2x + 2'):
##    print idx, char


x = symbols('x')
##string = Mathex('32x5 + 2x + 2')
string = Mathex('32x5 - 2x + 2')
print string
new = poly(string.formattize())
print new
print new.all_coeffs()

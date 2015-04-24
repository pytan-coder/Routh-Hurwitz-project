from routh_class_4 import Routh

string1 = Routh('1000/1x^3+10x^2+31x+1030')
string4 = Routh('10/1x^5+2x^4+3x^3+6x^2+5x+3')
string5 = Routh('10/1x^5+7x^4+6x^3+42x^2+8x+56')
string6 = Routh('128/1x^8+3x^7+10x^6+24x^5+48x^4+96x^3+128x^2+192x+128')
string7 = Routh('20/1x^8+1x^7+12x^6+22x^5+39x^4+59x^3+48x^2+38x+20')

##new = []
##new.append(string1)
##print new

string7.update_matrix()

lista = string7.get_matrix()
print len(lista)
for idx, sub in enumerate(lista):
    print idx, sub
    print

from mathex_class import Mathex
from routh_class_2 import Routh

string = []
value = []

file = open("sample_routh_text.txt", "w")

string.append(Routh(Mathex('-1x^7+2x^5-15.1x^2+1030')))
string.append(Routh(Mathex('1x^3+10x^2+31x+1030')))
string.append(Routh(Mathex('3x^7+9x^6+6x^5+4x^4+7x^3+8x^2+2x+6')))
string.append(Routh(Mathex('1x^5+2x^4+3x^3+6x^2+5x+3')))
string.append(Routh(Mathex('1x^5+7x^4+6x^3+42x^2+8x+56')))
string.append(Routh(Mathex('1x^8+1x^7+12x^6+22x^5+39x^4+59x^3+48x^2+38x+20')))

for idx in range(len(string)):
    string[idx].update_matrix()
    value.append(string[idx].get_matrix())


file.write('This is it\n')
#pickle.dump(value, file)

for element in range(len(string)):
    for idx, item in enumerate(value[element]):
        contain = [element for num, element in enumerate(item)]
        file.write(str(idx) + " " + str(contain) + '\n')
    file.write("\n")
    
file.close()
print 'Success!'

##### main body
#print extracted
#get_top_bottom_lists()
#print 'top', top_list
#print 'bottom', bottom_list
#print '===='
#update_lists()

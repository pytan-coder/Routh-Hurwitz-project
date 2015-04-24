from Mathex import *

string1 = Mathex('1x^3+10x^2+31x+1030')
string2 = Mathex('-1x^7+2x^5-15.1x^2+1030')
string3 = Mathex('3x^7+9x^6+6x^5+4x^4+7x^3+8x^2+2x+6')
string4 = Mathex('1x^5+2x^4+3x^3+6x^2+5x+3')
string5 = Mathex('1x^5+7x^4+6x^3+42x^2+8x+56')

#global variables
extracted = string5.get_complete_coeffs()
extract_expo = string5.get_exponents()
top_list = []
bottom_list = []

# helper functions
def get_top_bottom_lists():
    # extract top and bottom lists of coefficients
    global top_list, bottom_list
    top_list = []
    bottom_list = []

    for idx, item in enumerate(extracted):
        if idx % 2 == 0:
            top_list.append(item[0])
        else:
            bottom_list.append(item[0])
    top_list.append(0)
    bottom_list.append(0)

def update_lists():
    # list operation to determine new bottom list
    global top_list, bottom_list

    for num in range(max(extract_expo) - 1):
        temp_list = []

        # matrix operation
        for idx in range(len(top_list) - 1):
            matrix = (top_list[0] * bottom_list[idx + 1] - bottom_list[0] * top_list[idx + 1]) * -1 / bottom_list[0]
            temp_list.append(matrix)

        row = max(extract_expo) - num
        print row, temp_list

        # special conditions check
        if (temp_list.count(0) == 1) and (temp_list[0] == 0):
            zero_in_first_column(temp_list)
        elif temp_list.count(0) == len(temp_list):
            zeros_in_row(row, temp_list)

        #update lists
        top_list = bottom_list
        bottom_list = temp_list
        bottom_list.append(0)
    
def zero_in_first_column(temp):
    temp[0] = 0.001
    
def zeros_in_row(row_number, temp):
    for idx in range(len(temp) - 1):
        temp[idx] = temp[idx] * (row_number - 2 * idx)

##### main body
print extracted
get_top_bottom_lists()
print 'top', top_list
print 'bottom', bottom_list
print '===='
update_lists()

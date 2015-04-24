from mathex_class import Mathex
import fractions

# helper
def simplify_coeffs(temp):
    contain = []
    divisor = reduce(fractions.gcd, temp)
    if (divisor < 1) or ((len(temp) - temp.count(0)) < 2):
        return temp
    for idx in range(len(list(temp))):
        contain.append(temp[idx] / divisor)
    return contain

# class
class Routh:

    def __init__(self, transfer_func):
        self.func = transfer_func
        self.func_strings = []
        self.num_set = None
        self.den_set = None
        
        self.string = []
        self.expo = []
        self.top_list = []
        self.bottom_list = []
        self.routh_matrix = []

    def get_nums_and_dens(self):

        separated = self.func.split('/')

        self.num_set = Mathex(separated[0])
        self.den_set = Mathex(separated[1])

    def prep_denominator_lists(self):
                            
        self.string = self.den_set.get_complete_coeffs()
        self.expo = self.den_set.get_exponents()
        
        # fill top and bottom lists
        for idx, item in enumerate(self.string):
            if idx % 2 == 0:
                self.top_list.append(item[0])
            else:
                self.bottom_list.append(item[0])

        if len(self.top_list) != len(self.bottom_list):
            self.bottom_list.append(0)

        # prime routh matrix
        self.top_list = simplify_coeffs(self.top_list)
        self.bottom_list = simplify_coeffs(self.bottom_list)

        self.routh_matrix.append(self.top_list)
        self.routh_matrix.append(self.bottom_list)

    def __str__(self):
        return str(self.string) + '\n' + str(self.expo)

    def update_matrix(self):

        self.get_nums_and_dens()
        self.prep_denominator_lists()
                            
        for num in range(max(self.expo) - 1):
            temp_list = []
            row_number = max(self.expo) - (num)
            
            # check for zero in first column of bottom list or row of zeroes
            if (self.bottom_list.count(0) == len(self.bottom_list)):
                self.bottom_list = self.zeroes_row(self.top_list, self.bottom_list, row_number)
                self.routh_matrix[-1] = simplify_coeffs(self.bottom_list)
   
            self.zero_in_1st_col(self.bottom_list)
            
             
            # matrix operation
            for idx in range(len(self.top_list) - 1):
                matrix = (self.top_list[0] * self.bottom_list[idx + 1] - self.bottom_list[0] * self.top_list[idx + 1]) * -1 / self.bottom_list[0]
                temp_list.append(matrix)
            temp_list.append(0)

##            print self.bottom_list
            # update lists
            self.top_list = self.bottom_list
            self.bottom_list = simplify_coeffs(temp_list)
                            
            # update matrix list
            self.routh_matrix.append(self.bottom_list)
##            print self.routh_matrix
##            print " ========= "

    def get_matrix(self):
        return self.routh_matrix

    def zero_in_1st_col(self, temp):
        if (temp.count(0) < len(temp)) and (temp[0] == 0):
                temp[0] = 0.001

    def zeroes_row(self, temp1, temp, num):
        contain = list(temp)
        for idx in range(len(temp)):
            contain[idx] = temp1[idx] * (num - 2 * idx)
        return contain

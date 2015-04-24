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

    def __init__(self, trans_func):
        self.func = trans_func
        self.func_strings = []
        self.num_set = []
        self.den_set = []

    def get_nums_and_dens(self):

        separated = self.trans_func.split('/')

        for idx in range(len(separated)):
            self.func_strings.append(Mathex(separated[idx]))
        
        self.num_set.append(self.func_strings[0])
        self.den_set.append(self.func_strings[1])

    def prep_lists(self, func_string):
        self.string = func_string.get_complete_coeffs()
        self.expo = func_string.get_exponents()
        self.top_list = []
        self.bottom_list = []
        self.routh_matrix = []

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
        for num in range(max(self.expo) - 1):
            temp_list = []
            row_number = max(self.expo) - (num + 1)

            # check for zero in first column of bottom list
            self.zero_in_1st_col(self.bottom_list)

            # matrix operation
            for idx in range(len(self.top_list) - 1):
                matrix = (self.top_list[0] * self.bottom_list[idx + 1] - self.bottom_list[0] * self.top_list[idx + 1]) * -1 / self.bottom_list[0]
                temp_list.append(matrix)
            temp_list.append(0)

            # special conditions check
            self.zero_in_1st_col(temp_list)
            
            if temp_list.count(0) == len(temp_list):
                for idx in range(len(self.bottom_list)):
                    temp_list[idx] = self.bottom_list[idx] * (row_number - 2 * idx)

            # update lists
            self.top_list = self.bottom_list
            self.bottom_list = simplify_coeffs(temp_list)

            # extend final list
            self.routh_matrix.append(self.bottom_list)

    def get_matrix(self):
        return self.routh_matrix

    def zero_in_1st_col(self, temp):
        if (temp.count(0) < len(temp)) and (temp[0] == 0):
                temp[0] = 0.001

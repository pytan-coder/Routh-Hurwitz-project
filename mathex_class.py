import fractions

class Mathex:

    def __init__(self, expression):
        self.expression = expression


    def __str__(self):
        return self.expression

    def get_terms(self):
        contain = self.expression

        if '-' in self.expression:
            prev_idx = -1
            for count in range(self.expression.count('-')):
                prev_idx = self.expression.find('-', prev_idx + 1,)
                contain = contain[: prev_idx + count] + '+' + contain[prev_idx + count:]
        contain = contain.split('+')
        
        while '' in contain:
            contain.remove('')
        return contain

    def get_coeffs_and_exponents(self):
        coeff_list = []
        
        for item in self.get_terms():
            idx = item.find('x')
            if '^' in item:
                coeff_list.append([float(item[: idx]), int(item[idx + 2])])
            elif 'x' in item:
                coeff_list.append([float(item[: idx]), 1])
            else:                
                coeff_list.append([float(item), 0])

        return coeff_list

    def get_exponents(self):
        return [item[1] for item in self.get_coeffs_and_exponents()]

    def get_complete_coeffs(self):
        temp_list = list(self.get_coeffs_and_exponents())
        incomplete = True

        if temp_list[-1][-1] != 0:
            temp_list.append([0, 0])
        
        while incomplete:
            copy_list = []
            count = 0

            for idx, item in enumerate(temp_list[: -1]):
                if item[1] != (temp_list[idx + 1][1] + 1):
                    copy_list.append([idx + 1 + count, temp_list[idx][1] - 1])
                    count += 1
                
            if len(copy_list) >= 1:
                for item in copy_list:
                    temp_list.insert(item[0], [0, item[1]])
            else:
                incomplete = False

        return temp_list

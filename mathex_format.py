class Mathex:

    def __init__(self, expression):
        self.expression = expression


    def __str__(self):
        return self.expression

    def formattize(self):
        contain = self.expression
        rel_idx = 0
        for idx, char in enumerate(self.expression):
            if char is 'x':
                if self.expression[idx - 1] not in ['+', '-']:
                    contain = contain[:idx + rel_idx] + '*' + contain[idx + rel_idx:]
                    rel_idx += 1
##                    print contain
                    
                if self.expression[idx + 1] is not ' ':
                    contain = contain[:idx + rel_idx + 1] + '**' + contain[idx + rel_idx + 1:]
                    rel_idx += 2
##                    print contain
        return contain        
        

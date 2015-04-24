from mathex_class import Mathex

def get_nums_and_denoms(trans_func):

    holder = []
    
    separated = trans_func.split('/')
    print separated

    for idx, item in enumerate(separated):
        holder.append(Mathex(item))
    
    for idx, item in enumerate(holder):
        print item.get_complete_coeffs()
    
def get_final_denom(expo_1, coeffs_1, expo_2, coeffs_2):
    pass

###
G = '507/1x^4+3x^3+10x^2+30x+169'
H = '1/1x'

get_nums_and_denoms(G)
get_nums_and_denoms(H)


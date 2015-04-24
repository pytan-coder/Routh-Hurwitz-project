sample = 'x^3+2x^2-15x-1'
contain = sample

if '-' in sample:
    prev_idx = -1
    for count in range(sample.count('-')):
        prev_idx = sample.find('-', prev_idx + 1,)
        contain = contain[: prev_idx + count] + '+' + contain[prev_idx + count:]
        print count, prev_idx
        print sample
        print contain

print
print contain.split('+')

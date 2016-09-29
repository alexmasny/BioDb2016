from scipy.misc import comb

def iprb(k, m, n):
    '''k individuals are homozygous dominant for a factor,
    m are heterozygous, and n are homozygous recessive.'''
    summa = k + m + n
    total_comb = 4 * comb(summa, 2)
    total_comb_rec = 4 * comb(n, 2) + 2 * n * m + comb(m, 2)
    return 1 - total_comb_rec/total_comb

iprb(2,2,2)
iprb(18,19,15)

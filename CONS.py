from read_dataset import read_fasta
from collections import Counter

def cons(str_in):
    dct_fasta = read_fasta(str_in)
    prof_matr = [i for i in dct_fasta.values()]
    nucl_counts = []

    for i in range(len(prof_matr[0])):
        str_nucl = ''
        for j in prof_matr:
            str_nucl += j[i]
        nucl_counts.append(Counter(str_nucl))

    consensus = ''
    for i in nucl_counts:
        consensus += max(i, key=i.get)

    with open('output', 'w') as ouf:
        ouf.write('{}\n'.format(consensus))
        for nucl in ['A', 'C', 'G', 'T']:
            ouf.write('{}: '.format(nucl))
            nucl_numb = [i.get(nucl, 0) for i in nucl_counts]
            ouf.write(' '.join(map(str, nucl_numb)))
            ouf.write('\n')

# cons('input')
cons('cons')

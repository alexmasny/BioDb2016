def read_dataset_str(filename):
    '''Returns a string.'''
    with open(filename) as inf:
        return [i.strip() for i in inf.readlines()][0]

def dna(str_in):
    answer = [str_in.count(nucl) for nucl in ['A', 'C', 'G', 'T']]
    print(*answer)

dna('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
dna(read_dataset_str('rosalind_dna.txt'))

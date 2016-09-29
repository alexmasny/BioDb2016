def read_dataset_str(filename):
    '''Returns a string.'''
    with open(filename) as inf:
        return [i.strip() for i in inf.readlines()][0]

def rna(str_in):
    return str_in.replace('T', 'U')

rna('GATGGAACTTGACTACGTAAATT')
rna(read_dataset_str('rosalind_rna.txt'))

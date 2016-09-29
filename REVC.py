def read_dataset_str(filename):
    '''Returns a string.'''
    with open(filename) as inf:
        return [i.strip() for i in inf.readlines()][0]

def revc(str_in):
    tr_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    str_out = ''.join(tr_dict.get(nucl) for nucl in str_in)
    return str_out[::-1]

revc('AAAACCCGGT')
revc(read_dataset_str('rosalind_revc.txt'))

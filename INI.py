from Bio.Seq import Seq

def ini(sequence):
    my_seq = Seq(sequence)
    nucl_counts = [my_seq.count(i) for i in ['A', 'C', 'G', 'T']]
    print(*nucl_counts)

ini('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
ini(read_dataset_str('rosalind_ini.txt'))

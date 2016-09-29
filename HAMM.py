def read_dataset_list(filename):
    '''Returns a list.'''
    with open(filename) as inf:
        return [i.strip() for i in inf.readlines()]

def hamm(lst_in):
    hamm_count = int()
    for i in range(len(lst_in[0])):
        if lst_in[0][i] != lst_in[1][i]:
            hamm_count += 1
    return hamm_count

hamm(read_dataset_list('input.txt'))
hamm(read_dataset_list('rosalind_hamm.txt'))

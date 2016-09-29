def read_dataset_list(filename):
    '''Returns a list.'''
    with open(filename) as inf:
        return [i.strip() for i in inf.readlines()]

def subs(lst_in):
    string, sub_string = lst_in
    res_lst = [0]

    while -1 not in res_lst:
        res_lst.append(string.find(sub_string, res_lst[-1] + 1))
    res_lst = [str(i + 1) for i in res_lst[1:-1]]
    print(' '.join(res_lst))

subs(['GATATATGCATATACTT', 'ATAT'])
subs(read_dataset_list('rosalind_subs.txt'))

from itertools import permutations

def perm(int_in):
    int_in = int(int_in)
    lst_numb = list(range(1, int_in + 1))
    lst_perm = list(permutations(lst_numb, int_in))
    with open('output', 'w') as ouf:
        ouf.write('{}\n'.format(str(len(lst_perm))))
        for i in lst_perm:
            ouf.write(' '.join(map(str, i)))
            ouf.write('\n')

# perm(3)
perm(read_dataset_str('perm'))

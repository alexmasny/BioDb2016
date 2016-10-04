def read_dataset_str(task_shortcut):
    '''Returns a string.'''
    filename = 'rosalind_{}.txt'.format(task_shortcut)
    with open(filename) as inf:
        return [i.strip() for i in inf.readlines()][0]

def read_dataset_list(task_shortcut):
    '''Returns a list.'''
    filename = 'rosalind_{}.txt'.format(task_shortcut)
    with open(filename) as inf:
        return [i.strip() for i in inf.readlines()]

def read_fasta(task_shortcut):
    '''Transform fasta in txt into dictionary: name[sequence]'''
    filename = 'rosalind_{}.txt'.format(task_shortcut)
    with open(filename) as inf:
        fasta_list = [i.strip() for i in inf.readlines()]
    records_dict = {}
    for line in fasta_list:
        if '>' in line:
            new_key = line[1:]
            records_dict[new_key] = ''
            continue
        else:
            records_dict[new_key] += line[:]
    return records_dict

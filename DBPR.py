from Bio import ExPASy
from Bio import SwissProt

def read_dataset_str(task_shortcut):
    '''Returns a string.'''
    filename = 'rosalind_{}.txt'.format(task_shortcut)
    with open(filename) as inf:
        return [i.strip() for i in inf.readlines()][0]

def dbpr(up_id):
    handle = ExPASy.get_sprot_raw(up_id)
    record = SwissProt.read(handle)
    go_functions = [i[2][2:] for i in record.cross_references if i[0] == 'GO' and i[2][0] == 'P']
    for i in go_functions:
        print(i)

dbpr('Q5SLP9')
dbpr(read_dataset_str('dbpr'))

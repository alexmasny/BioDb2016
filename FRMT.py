from read_dataset import read_dataset_list
from Bio import Entrez
from Bio import SeqIO

def record_key(rec):
    return len(rec.seq)

def frmt(str_in):
    lst_in = str_in.split(' ')
    Entrez.email = 'the.pazitiff@gmail.com'
    handle = Entrez.efetch(db='nucleotide', id=lst_in, rettype='fasta')
    records = list(SeqIO.parse(handle, 'fasta'))
    min_rec = min(records, key=record_key)
    return print(min_rec.format('fasta'))

# frmt("FJ817486 JX069768 JX469983")
frmt(read_dataset_str('frmt'))

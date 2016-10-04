import requests, os, re
from bs4 import BeautifulSoup
from read_dataset import read_fasta
from read_dataset import read_dataset_list

def mprt(lst_in):
    answer = []
    for prot_id in lst_in:
        url = 'http://www.uniprot.org/uniprot/{}.fasta'.format(prot_id)
        with open('rosalind_prot_fasta.txt', 'w') as ouf:
            ouf.write(requests.get(url).text.strip())
        d = read_fasta('prot_fasta')
        for value in d.values():
            pseq = str(value)
        starts = []
        for i in range(len(pseq)-3):
            if pseq[i] == 'N' and pseq[i+1] != 'P' \
            and pseq[i+2] in ['S', 'T'] \
            and pseq[i+3] != 'P':
                starts.append(i + 1)
#         pattern = re.compile(r'N[^P][S|T][^P]')
#         result = re.finditer(pattern, prot_sequence)
#         starts = [i.start(0) + 1 for i in re.finditer(pattern, prot_sequence)]
# give result: P07204_TRBM_HUMAN
# 47 115 382 409 instead of 47 115 116 382 409
        if len(starts) != 0:
            print(prot_id)
            print(*starts)


# mprt(read_dataset_list('input'))
mprt(read_dataset_list('mprt'))
#     os.remove('/Users/alex/bit/BioDb2016/', 'rosalind_prot_fasta.txt')

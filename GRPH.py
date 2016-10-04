from read_dataset import read_fasta

def grph(str_in):
    dct_fasta = read_fasta(str_in)
    lst_seq = [[key, value[:3], value[-3:]] for key, value in dct_fasta.items()]
    answer = []
    for i in lst_seq:
        for j in lst_seq:
            if i[1] == j[2] and i[0] != j[0]:
                answer.append([j[0], i[0]])
    return [print(*i) for i in answer][0]

# grph('input')
grph('grph')

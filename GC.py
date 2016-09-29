def fasta_read(fastafile):
    '''Transform fasta in txt into dictionary: name[sequence]'''
    with open(fastafile) as inf:
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

def gc(fastafile):
    records_dict = fasta_read(fastafile)
    GC_content_max = 0

    for record in records_dict.keys():
        dna = records_dict[record]
        GC_content = ((dna.count('G')+dna.count('C'))/len(dna)*100)
        if GC_content > GC_content_max:
            GC_content_max = GC_content
            record_max = record
    print(record_max, round(GC_content_max, 6), sep='\n')

gc('input_gc.txt')
gc('rosalind_gc.txt')

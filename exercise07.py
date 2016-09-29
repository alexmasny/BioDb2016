import os, re, json
fd = open(os.sep.join(('..','data','reading_searching_sending','interactions.txt')))

lines = [i.strip() for i in fd.readlines()]

pattern_def = 'p\((?P<namespace_subject>\w+)\:(?P<protein_subject>\w+)\)\s(?P<relationship>\W+?)\s(?P<if_activation>act)*\(*p\((?P<namespace_object>\w+)\:(?P<protein_object>\w+)\)\)*'
pattern = re.compile(pattern_def)

result = [pattern.match(i) for i in lines]


with open('exercise07.json', 'w') as ouf:
    ouf.write(json.dumps(result[0].groupdict()))
    ouf.write('\n')
    ouf.write(json.dumps(result[1].groupdict()))

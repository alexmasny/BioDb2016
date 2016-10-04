from read_dataset import read_dataset_str

def iev(str_in):
    lst_couples = [int(i) for i in str_in.split()]
    lst_prob_coup = [1, 1, 1, .75, .5, 0]
    lst_prob_total = list()
    lst_prob_total.append(2 * no_coup * lst_prob_coup[i] for i, no_coup in enumerate(lst_couples))
    result = sum(*lst_prob_total)
    return result

# iev('1 0 0 1 0 1')
iev(read_dataset_str('iev'))

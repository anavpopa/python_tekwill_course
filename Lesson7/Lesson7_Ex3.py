a = [[[1,2],3,4],5]
flat_list = []
def make_list_flat (l):
    if (type(l) is not list):
        return flat_list.extend ([l])
    else:
        [make_list_flat(e) for e in l]

make_list_flat(a)
print (flat_list)
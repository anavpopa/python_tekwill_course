l = [1, 2, [3, 4, [5]]]
# [3,4,[5]]]


def new_list(l):
    if (type(l) is not list):
        return l**2
    else:
         return [new_list(e) for e in l]
        #return map(lambda x: print('x',x), l)


print(list(new_list(l)))

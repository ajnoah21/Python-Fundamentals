alist = ['stuff',1,2,3]

def list_sort(blist):
    blist = list(blist)
    blist.append('morestuff')
    print(blist)
    return blist

def tuple_sort(clist):
    dlist = tuple(clist)
    #dlist = (2,1)
    return dlist

p_list = list_sort(tuple(alist))
print(alist, p_list)

p_list = tuple_sort(alist)
print(alist, p_list)

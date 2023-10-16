def addtwo(lista):
    for i in range(len(lista)):
        lista[i] = lista[i]*2

def addtwo_int(a):
    a=a+2

def main():
    mini_list = ['bob','alice']
    listb = [1,2,3, mini_list]
    listc = listb # super shallow copy, basically just another name for same list in memory
                # what happens to listc, happens to listb, they are the same thing
    print(listb, listc) 

    shallow_listb = listb.copy() #shallow copy is a different list, but if the list contains another list, it doesn't make a deep copy of that
    shallow_listb[0] = 10
    shallow_listb[3][0] = 'Veronica'
    print('Shallow copy listb')
    print(shallow_listb, listb)

    addtwo(listb)
    print(listb)

    a = 5
    print(a)
    addtwo_int(a)
    print(a)

main()
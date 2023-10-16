import copy

mini_list = ['a','b']

lista = [1,2,3,mini_list]
print(lista)
print()

listb = lista.copy() #shallow copy of lista, inner lists aren't copied
listc = copy.deepcopy(lista)
listb[0] = 5 #this won't affter lista
mini_list[0] = 'c'
print("fourth element of lista: ", lista[3])
print("also forth element of lista: ", mini_list)
lista[3][1] = 'd' #same as mini_list[1] = 'd'

print(lista)
print(listb)
listb.extend(['e','f'])
print(listb)

print("listc: ")
print(listc) # listc remain unaffected because it is a deep copy
import copy

l1 = ['Corin',"Chepko"]
m_l1 = [1,2,l1]
c_ml1 = m_l1.copy()
dc_ml1 = copy.deepcopy(m_l1)
l1[1] = 'Dawg'
print(c_ml1)
print(dc_ml1)
#자료구조 변경

menu = {'A', 'B', 'C'}
print(menu, type(menu)) #{'B', 'A', 'C'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) #['C', 'A', 'B'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) #('A', 'C', 'B') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) #{'A', 'C', 'B'} <class 'set'>
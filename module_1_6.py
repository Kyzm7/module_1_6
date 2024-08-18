my_dict = {'Ivan' : 1999, 'Maria': 1998, 'Irina': 1976}
print(my_dict)
print(my_dict ['Ivan'])
print(my_dict.get ('Kamila','Такого ключа нет'))
my_dict ['Vika'] = 2005
my_dict ['Lena'] = 2001
a = my_dict.pop('Maria')
print(a)
print(my_dict)

my_set = {1, 1, 'Яблоко', 43.115, 2, 1, 2}
print(my_set)
my_set.add(5)
my_set.add ('Груша')
print (my_set.discard(2))
print(my_set)
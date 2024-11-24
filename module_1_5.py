immutable_var = 1, 2, 3, True
print(immutable_var)
#immutable_var[0] = 10
#print(immutable_var)  #попытка изменить элемент кортежа
mutable_list =[1, 2, 3, False, 'apple']
print(mutable_list)
mutable_list[0] = 5
mutable_list[4] = 'coconut'
print(mutable_list)

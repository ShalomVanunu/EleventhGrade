

tuple_a = ("hello",1.577,'moshe',"name")
number = tuple_a[1]
print('%.1f'%number)

list_a = list(tuple_a)
print(type(list_a))
print(list_a)
list_a.append("shalom")
tuple_a = tuple(list_a)
print(tuple_a)


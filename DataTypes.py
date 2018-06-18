# number
num_int = 100000000000000000111111111111111111111110000000000000000011111111111111111111111000000000000000001111111111111111111111
# string
str_data = 'Hello World!'
print(num_int, str_data)

# list
list_data = [1, 2, 3, 100, 200, "300"]
print(list_data[:], list_data[2:], list_data[:2], list_data[1])

# tuple
tuple_data = (1, 2, 3, 100, 200, "300")
print(tuple_data[:], tuple_data[2:], tuple_data[:2], tuple_data[1])

# dictionary
dic_data = {'1': 'khoibv', '2': 'tuannm', '3': 'trungpt'}
for key in dic_data.keys():
    print('{%s: %s}' % (key, dic_data[key]))

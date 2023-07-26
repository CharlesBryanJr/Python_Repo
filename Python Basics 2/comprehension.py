'''comprehension'''
print(" ")

comp_list = [i for i in range(1, 11)]
print(comp_list)
print(" ")

comp_list2 = [i+1 for i in range(1, 11)]
print(comp_list2)
print(" ")

comp_list3 = [i / 2 for i in range(1, 11)]
print(comp_list3)
print(" ")

comp_list4 = [i / 2 for i in range(1, 11) if i % 2 == 0]
print(comp_list4)
print(" ")

comp_tuple = tuple([i * j for i in range(1, 11) for j in range(5)])
print(comp_tuple)
print(" ")

comp_set = {i * j for i in range(1, 11) for j in range(5)}
print(comp_set)
print(" ")

comp_dict = {i: j * j for i in range(1, 11) for j in range(5)}
print(comp_dict)
print(" ")

print(" ")
tuple1 = (2, 7, [5,7,8], 'Tutor', True, 'T', 3.21)
temp = []
for idx in range(len(tuple1)-1):
    if idx != 1:
        temp.append(tuple1[idx])
tuple2 = tuple(temp)
print("Before: ", tuple1, "Id: ", id(tuple1))
print("After: ", tuple2, "Id:", id(tuple2))
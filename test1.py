
list1 = []
for i in range(2,100):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count = count + 1
    if count == 2:
        list1.append(i)
        count = 0
print(list1)
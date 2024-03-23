
temp = []
for i in range(100, 999, 1):
    # 个位
    index1 = i % 10
    index2 = (i % 100 - i % 100 % 10) / 10
    index3 = (i - i % 100) / 100
    if 20 == index1 + index2 + index3:
        temp.append(i)
    print('i:', i, '个位：', index1, '十位', index2, '百位', index3)

print(temp)
print('总数：', len(temp))

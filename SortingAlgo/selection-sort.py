lst = [3, 5, 8, 1, 9]
n = len(lst)
for i in range(n):

    for j in range(i + 1, n):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

    print(lst)
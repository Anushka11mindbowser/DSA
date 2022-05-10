print("Bubble Sort\n")
lst = []
size = int(input("Enter the size of array:\n"))
for iteration in range(0,size):
    number = int(input("Enter a number\n"))
    lst.append(number)
print(lst)

def bubble_sort(array):
    for i in range(size):
        for j in range(0, size-i-1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
                print(lst)
    return lst

print(bubble_sort(lst))



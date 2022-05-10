print("Quick Sort\n")

arr1 = [4,8,2,0,1,5,7]
l = len(arr1) - 1


def partition(arr, l, h):


  pivot = arr[h]


  i = l - 1


  for j in range(l, h):
    if arr[j] <= pivot:

        i = i + 1


        temp = arr[i]
        arr[i]=arr[j]
        arr[j]=temp

  t = arr[i+1]
  arr[i+1]=arr[h]
  arr[h]=t



  return i + 1


def quickSort(arr, lb, hb):
  if lb < hb:


    pivot = partition(arr, lb, hb)


    quickSort(arr, lb, pivot - 1)


    quickSort(arr, pivot + 1, hb)








quickSort(arr1, 0, l)

print('Sorted Array:')
print(arr1)
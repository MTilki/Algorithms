#create empty list
arr = []

#input number of elements
n = int(input("Enter neumber of elements for the array: "))

#asking for values until n
for i in range(0, n):
    values = int(input())
    #append values to the arr
    arr.append(values)

print(arr)

#ask for target value
target = int(input("Enter the target value"))

#define left and right of array
left=0
right= n -1

def iteration(arr,target):
    while left <= right:
        middle = (left + right) / 2
    if middle == target:
          return middle
    elif target < arr[middle]:
        right = middle - 1
    else:
        left = mid + 1
    return
print("Not found")
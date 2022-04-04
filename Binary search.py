
#create empty list
n=0
arr = []
target=0

#input number of elements
n = int(input("Enter neumber of elements for the array: "))

#asking for values until n
for i in range(0, n):
    values = int(input())
    #append values to the arr
    arr.append(values)

 #ask for target value
target = int(input("Enter the target value"))

def binary_search(arr,target):
   
    #define left and right of array
    left=0
    right= len(arr) -1
    mid=0
   
    #search the array
    while mid != target:
        
        mid = (left + right) // 2
        
        if arr[mid] <  target:
            left = mid + 1

        elif arr[mid] > target:
            right = mid - 1
        
        else:
            return mid
    return  -1
result  = binary_search(arr, target)

if result != -1:
    print("Target is at index", str(result))
else:
    print("Target not found")

quit()
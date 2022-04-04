#create empty list
n=0
arr = []
x=0
#input number of elements
n = int(input("Enter neumber of elements for the array: "))

#asking for values until n
for i in range(0, n):
    values = int(input())
    #append values to the arr
    arr.append(values)

x = int(input("Enter the target value"))

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
 
# Test array

 
# Function call
result = binary_search(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
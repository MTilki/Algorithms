def main():
    #create empty list
    n=0
    arr = []
    target=0

    #input number of elements
    n = int(input("Enter neumber of elements for the array: "))

    #asking for values until n
    for i in range(0, n):
        values = int(input("Enter array values"))
        #append values to the arr
        arr.append(values)

    #ask for target value
    target = int(input("Enter the target value: "))
    print("-----------------------------------")
    print("array: ",arr)
    print("Search target: ",target)
    print("-----------------------------------")

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
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")

    restart = input("Search again? [Y/N]: ").upper()
    if restart== "Y":
        main()
    else:
        quit()
    
if __name__ == "__main__":
    main()
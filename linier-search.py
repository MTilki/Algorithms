def main():
    #create empty list
    n=0
    arr = []
    target=0

    #input number of elements
    print("-----------------------------------")
    n = int(input("Enter neumber of elements for the array: "))

    #asking for values until n
    for i in range(0, n):
        values = int(input("Enter array value: "))
        print()
        #append values to the arr
        arr.append(values)

    #ask for target value
    target = int(input("Enter the target value: "))
    print("-----------------------------------")
    print("array: ",arr)
    print("Search target: ",target)
    print("-----------------------------------")

    def linier_search(arr,target):

        #define left and right of array
        found = False
        pointer = 0
        last_element = len(arr) -1

        #search the array
        while (found is False) or (pointer < last_element):
            if arr[pointer] == target:
                found = True
                return pointer
            else:
                pointer = pointer +1
        return  -1

    result  = linier_search(arr, target)

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
def main():
    #create empty list
    n=0
    arr=[]

    #input number of elements
    print("-----------------------------------")
    n = int(input("Enter number of elements for the array: "))

    #asking for balues until n
    for i in range(0,n):
        values  = int(input("Enter array value: "))
        print()
        #append values to the arr
        arr.append(values)
    
    #ask for targer value
    print("-----------------------------------")
    print("unsorted array: ",arr)
    print("-----------------------------------")

    def bubble_sort(arr):
        sorted = False
        
        while not sorted:
            sorted = True
            for b in range(0,len(arr) - 1):
                if arr[b] > arr[b+1]:
                    sorted = False
                    arr[b],arr[b+1] = arr[b+1],arr[b]
        return arr       
    result = bubble_sort(arr)
    print("-----------------------------------")
    print("sorted array: ",arr)
    print("-----------------------------------")
if __name__ == "__main__":
    main()
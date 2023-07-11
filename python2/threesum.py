def findTriplets(arr):
    number= len(arr)
    if number < 3:
        print("Array Input Length Must More Than 2")
        return []

    arr.sort()  
    triplets = []
    for i in range(number - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue  

        left = i + 1
        right = number - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
                triplets.append([arr[i], arr[left], arr[right]])
                while left < right and arr[left] == arr[left + 1]:
                    left += 1  
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1  
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    print(triplets)

arr = input("Enter Your List : ").split()
arr = [int(num) for num in arr]
findTriplets(arr)


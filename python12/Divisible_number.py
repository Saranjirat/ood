print(" *** Divisible number ***")
n = int(input("Enter a positive number : "))
divisible_numbers = []
if n <= 0 :
    print("0 is OUT of range !!!")
else :
    for i in range(1, n + 1):
        if n % i == 0:
            divisible_numbers.append(i)
    print("Output ==>", " ".join(str(num) for num in divisible_numbers))
    print("Total ==>", len(divisible_numbers))
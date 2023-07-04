print(" ***Function Odd List***")
def odd_list(numbers):
    odd_list = [num for num in numbers if num % 2 != 0]
    return odd_list
Input_list = input("Enter list numbers : ").split()
Input_list = [int(num) for num in Input_list]

output_list = odd_list(Input_list)

print("Input list : ", Input_list)
print("Output list : ", output_list)
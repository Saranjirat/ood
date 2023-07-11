def Rshift(num, shift):
    result = num >> shift
    return result

n, s = input("Enter number and shiftcount : ").split()
print(Rshift(int(n), int(s)))



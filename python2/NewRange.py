def my_range(*args):
    num_args = len(args)
    start = 0.0
    end = 0.0
    step = 1.0

    if num_args == 1:
        end = args[0]
    elif num_args == 2:
        start = args[0]
        end = args[1]
    elif num_args == 3:
        start = args[0]
        end = args[1]
        step = args[2]
    else:
        raise ValueError("Invalid number of arguments")

    result = []
    while start < end:
        result.append(round(start, 3))  
        start += step
    return tuple(result)

print("*** New Range ***")
inputs = input("Enter Input : ").split()
inputs = [float(x) for x in inputs]
if len(inputs) == 1:
    result = my_range(inputs[0])
elif len(inputs) == 2:
    result = my_range(inputs[0], inputs[1])
elif len(inputs) == 3:
    result = my_range(inputs[0], inputs[1], inputs[2])
else:
    print("Invalid number of arguments")

print(result)




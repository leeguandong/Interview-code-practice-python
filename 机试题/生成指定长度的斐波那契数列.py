def fibs(x):
    result = [0,1]
    for index in range(x-2):
        result.append(result[-1]+result[-2])
    return result

num = int(input('Enter a number'))
print(fibs(num))


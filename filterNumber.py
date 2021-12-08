def filterNumber(numbers):
    result = []
    for i in numbers:
        if (i not in result) and (i <= 5 or i >= 9):
            result.append(i)
    result = sorted(result)
    return result

#print(filterNumber([3,2,1,2,1,4,6,5,7,8,8,9,2]))
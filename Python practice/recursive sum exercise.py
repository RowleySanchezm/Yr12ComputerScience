def addNums(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + addNums(numbers[1:])
    #End if
#End function

marks = [3,6,2,8,1]
total = addNums(marks)
print(total)

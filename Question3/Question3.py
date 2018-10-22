a = range(0,51,5)

def Test1():
    b = [1,2,3,4,5,9]
    return(list(reversed(b)))

print(Test1())


biglist = [5,1,4,2,8,9]
biggerlist = [51,12,43,24,85,96]
biggestlist = [75,61,45,42,38,29]

def second_largest(arr):
    # input param: list/array
    i = arr.index(max(arr))
    del arr[i]
    return(max(arr))


print(second_largest([1,2,3]))
print(second_largest(biglist))
print(second_largest(biggerlist))
print(second_largest(biggestlist))




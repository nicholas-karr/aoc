file = open('day1/input')
lines = file.readlines()

strNums = ['one','two','three','four','five','six','seven','eight','nine']
strNumsRev = [i[::-1] for i in strNums]

def findIn(st, strNums):
    results = {} # index to value

    for index, j in enumerate(strNums):
        results[ st.find(j) ] = int(index + 1)

    for j in range(0,10):
        results[ st.find(str(j)) ] = j

    del results[-1]

    res = min(results)

    return results[res]


def ends(i):
    first = findIn(i, strNums)
    last = findIn(i[::-1], strNumsRev)

    return int(str(first) + str(last))

nums = [ends(i) for i in lines]
print(sum(nums))
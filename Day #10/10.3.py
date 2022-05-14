def findMin(digitLen, sum):
    count = 0
    minList = [0] * digitLen
    if sum > digitLen*9 or (sum == 0 and digitLen > 1):
        return -1
    sum -= 1
    for index in range(digitLen-1, 0, -1):
        if sum > 9:
            minList[index] = 9
            sum -= 9
        else:
            minList[index] = sum
            sum = 0
    minList[0] = sum +1
    for index in range(digitLen):
        count = count * 10 + minList[index]
    return count

def findMax(digitLen, sum):
    count = 0
    maxList = [0] * digitLen
    if sum == 0 or sum > digitLen*9 :
        return -1
    for index in range(digitLen):
        if sum >= 9:
            maxList[index] = 9
            sum -= 9
        else:
            maxList[index] = sum
            sum = 0
        count = count * 10 + maxList[index]
    return count

def main():
    userInput = input().split()
    userInput = list(map(int, userInput))
    digitLen, Sum = userInput[0], userInput[1]
    min = findMin(digitLen, Sum)
    max = findMax(digitLen, Sum)
    print(min,max)

if __name__ == '__main__':
    main()

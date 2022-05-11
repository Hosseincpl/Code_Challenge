def find_min(digitLen, Sum):
    maxList = [9] * digitLen
    tmp = Sum//9
    

def find_max(DigitLen, Sum):
    pass

def main():
    UserInput = input().split()
    UserInput = list(map(int, UserInput))
    digitLen, Sum = UserInput[0], UserInput[1]
    min = find_min(digitLen, Sum)
    max = find_max(digitLen, Sum)
    print(min,max)

if __name__ == '__main__':
    main()

import random

def max_min(numbers):
    minimum= numbers[0]
    for num in numbers:
        if num < minimum:
            minimum= num
        print(f"Currrent minimum {minimum}")
    return minimum

def getValues():
    list = random.sample(range(50,100),k=5)
    #list=[5,4,3,2,1]
    print(list)
    result =max_min(list)
    print(f"value is {result}")

    
getValues()
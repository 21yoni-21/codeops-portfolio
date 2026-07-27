#Test 01
def getonlyEvens(numbers):
    result =[]

    for index in range(len(numbers)):
       if index % 2 == 0 and numbers[index] % 2 == 0:
          result.append(numbers[index])

          print(result)

#Test 1
getonlyEvens([1, 2, 3, 6, 4, 8,])

# Test 1
getonlyEvens([0, 1, 2, 3, 4])


#Question 2.......................................

def reverscompare(number):
    Aonce = number % 10 
    Atens = number // 10
    reversed_number = Aonce * 10 + Atens

    if number > reversed_number:

        print("ok")

    else: 
          print("Not ok")

#Test 1
reverscompare(72)

#Test 2
reverscompare(23) # n


# Question 3 ..............................................

def returnFactorial(number):

    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result 

#Test1
print(returnFactorial(5))
#Test2
print(returnFactorial(6))
#Test3
print(returnFactorial(0))


#Question 4 ....................................

def checkMeera(arr):

    for number in arr:

        if number * 2 in arr:
            print("I am Not a Meera array")
            return

    print("I am a Meera array")


# Test1
checkMeera([10, 4, 0, 5])
#Test 2
checkMeera([7, 4, 9])
#Test 3
checkMeera([1, -6, 4, -3])


#Question ...........................................

def isDual(arr):
    counts = {}

    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for value in counts.values():
        if value != 2:
            return 0

    return 1
#test  .............. 
print(isDual([1, 2, 1, 3, 3, 2]))
print(isDual([2, 5, 2, 5, 5]))
print(isDual([3, 1, 1, 2, 2]))



#Qeutsion.............................................


def digitalClock(seconds):

    seconds = seconds % 86400

    hours = seconds // 3600
    remaining = seconds % 3600

    minutes = remaining // 60
    secs = remaining % 60

    return f"{hours:02}:{minutes:02}:{secs:02}"


# Test cases
print(digitalClock(5025))
print(digitalClock(61201))
print(digitalClock(87000))


 


  
        


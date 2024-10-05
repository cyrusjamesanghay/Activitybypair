usernum = int(input("How many numbers do you want to enter :"))
list = []

for i in range(usernum):
    numbers = int(input("Enter a number :"))
    list.append(numbers)

    if numbers > 0:
        print("The number is positive")
    elif numbers < 0:
        print("The number is negative")
    else:
        print("The number is zero")
        list.append(list)

print(list)
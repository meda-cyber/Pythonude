user_list = []
sum_list = 0

# Looking the even number from 10 given number
for i in range(10):
    userInput = int(input("Enter number here :"))

    try:
        number = userInput
        user_list.append(number)
        if number % 2 == 0:
            sum_list += number

    except ValueError:
        print("Incorrect Value . that is not int")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(sum_list))

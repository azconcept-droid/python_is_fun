#!/usr/bin/python3
# Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

# write your code here
# HINT: You can use the modulo operator to find a factor
message = "{} is NOT a prime number, because {} is a factor of {}"
for number in check_prime:
    for i in range(2, number):
        if (number % i) == 0:
            print(message.format(number, i, number))
            break
        # if i == number -1:
            # print("{} IS a prime number".format(number))
    else:
        print("{} IS a prime number".format(number))

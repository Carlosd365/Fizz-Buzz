#method to know if it is divisible by 3
def is_multiple_of_3(number):
    return number % 3 == 0

#method to know if it is divisible by 5
def is_multiple_of_5(number):
    return number % 5 == 0

#method to know if it is divisible by 3 and 5
def is_multiple_of_5_3(number):
    return number % 5 == 0 and number % 3 == 0


def main():
    # Loop through numbers from 1 to 100
    for i in range (1, 100 + 1):
        #check if i is divisible by 3 and 5 using the method
        if is_multiple_of_5_3(i):
            print("fizz-buzz")
        #check if i is divisible by 3 using the method
        elif is_multiple_of_3(i):
            print("fizz")
        #check if i is divisible by 5 using the method
        elif is_multiple_of_5(i):
            print("buzz")
        #prints only the number if the above conditions are not met
        else:
            print(i)
main()


# take input from the keyboard until it is identical to a PIN.

# created a PIN
correct_pin = 4567

# restrict the number of attempts to 3 and use a variable
# created a variable of maximum attempts
maximum_attempts = 3
# created a counter variable for attempts completed
attempt = 1
# created a while loop to establish how many attempts have been made

while attempt < maximum_attempts:
    supplied_pin = input("Enter your PIN: ")
# while the attempts are less than 3, users are able to input their PIN

# if input incorrect pin, another attempt will be added to the attempt variable

# create remaining_attempts variable to be able to print the number of attempts left
    remaining_attempts = maximum_attempts - attempt

    if remaining_attempts < maximum_attempts:
# using f in the string to add a function within to be able to print message showing how many attempts are left
        print(f"Incorrect Pin. You have {remaining_attempts} attempts left")
    else:
            print("Incorrect PIN. Maximum attempts reached")

# # if statement added to check if the PIN has been entered correctly.
if correct_pin == 4567:
    print("Correct PIN")


#
# # loop will end if correct pin is entered due to the break statement
#
# # if incorrect pin submitted, else statement will be initiated
# else:

# # if input incorrect pin, another attempt will be added to the attempt variable
#
# # create remaining_attempts variable to be able to print the number of attempts left
# remaining_attempts = maximum_attempts - attempt
# if remaining_attempts > 0:
# # using f in the string to add a function within to be able to print message showing how many attempts are left
#     print(f"Incorrect Pin. You have {remaining_attempts} attempts left")
# else:
#     print("Incorrect PIN. Maximum attempts reached")













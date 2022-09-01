from random import randint
Length_of_passwd = int(input("Enter the total lenght of the password :"))
upper_char_count = int(input("Enter the number of upper case characters required : "))
lower_char_count = int(input("Enter the number of lower case character required :"))
digits_count = int(input("Enter the number of digits required :"))
special_count = int(input("Enter the number of special characters required :"))
char_count = upper_char_count+lower_char_count+digits_count+special_count


def password_gen():
    upper_sum=""
    lower_sum=""
    digit_sum=""
    special_sum=""

    for i in range(0,upper_char_count):
        upper = chr(randint(65,90))
        upper_sum +=upper
    for i in range(0,lower_char_count):
        lower = chr(randint(97,122))
        lower_sum+=lower
    for i in range(0,digits_count):
        digit = chr(randint(48,57))
        digit_sum+=digit
    for i in range(special_count):
        special = chr(randint(128,152))
        special_sum+=special
    return upper_sum+lower_sum+digit_sum+special_sum


if char_count == Length_of_passwd:
    print(password_gen())
elif char_count > Length_of_passwd:
    print(f"The passowrd length you requested is {char_count} and requirement is {Length_of_passwd} .please check")
else:
    print(f"The passowrd length you requested is {char_count} and requirement is {Length_of_passwd} .please check")

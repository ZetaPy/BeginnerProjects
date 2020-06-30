# This program computes for the compound interest through loops

while True:
    principal = int(input('What is your principal amount? >>> '))
    interest_rate = float(input('What is the interest rate? >>> '))
    duration = int(input('How many years will you let the money sit? >>> '))
    interest_rate = interest_rate / 100


    i = 1

    while i <= duration:

        income = principal * interest_rate  # calculates for income (e.g '7% of 500')
        total = round(income + principal)   # adds the income to the principal (e.g add 7% of 500 to 500)
        principal = total                   # new principal amount
        i_list = list(str(i))

        if (len(i_list) >= 2) and (i_list[-1] == '1') and (i_list[-2] == '1'):
            print('You will have $' + str(total) + ' in the ' + str(i) + 'th year.')

        elif (len(i_list) >= 2) and (i_list[-2] == '1') and (i_list[-1] == '2'):
            print('You will have $' + str(total) + ' in the ' + str(i) + 'th year.')

        elif (len(i_list) >= 2) and (i_list[-2] == '1') and (i_list[-1] == '3'):
            print('You will have $' + str(total) + ' in the ' + str(i) + 'th year.')

        elif i_list[-1] == '1':
            print('You will have $' + str(total) + ' in the ' + str(i) + 'st year.')

        elif i_list[-1] == '2':
            print('You will have $' + str(total) + ' in the ' + str(i) + 'nd year.')

        elif i_list[-1] == '3':
            print('You will have $' + str(total) + ' in the ' + str(i) + 'rd year.')

        else:
            print('You will have $' + str(total) + ' in the ' + str(i) + 'th year.')

        i += 1

    choice = input('Would you like to continue? >>> ')

    if choice in ['yes', 'yup', 'yupperoo', 'oo']:
        print('OKAY, LET\'S CONTINUE!')

    elif choice in ['no', 'nope', 'nah', 'nah dude']:
        print('OKAY, GOODBYE!')
        break

    else:
        print("ERROR, WRONG INPUT")
        break

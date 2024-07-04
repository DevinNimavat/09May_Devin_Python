'''Write python program that user to enter only odd numbers, else will 
raise an exception. '''

try:
    number=int(input('Enter Number : '))

    if number%2==0:
        raise EnvironmentError(number)
    print('Number is Odd', number)
except ValueError:
    print('Pleace Enter  odd Number Only...')
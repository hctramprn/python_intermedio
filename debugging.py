#List comprehension containing all the divisors for the given number
def divisors(num):
    divisors = [number for number in range(1, num + 1) if num % number == 0]
    return divisors

#Validating the user's input using try and except
def run():
    try:
        num = int(input('Choose a number: '))
        if num < 0:
            raise ValueError
        print(divisors(num))
    except ValueError:
        print('The number must be greater than 0')
    finally:
        print('Ending program')


#Validating the user's input using assert statements
def run():
    num = input('Choose a number: ')
    assert num.isnumeric(), 'The number must be greater than 0'
    print(divisors(int(num)))


if __name__ == '__main__':
    run()
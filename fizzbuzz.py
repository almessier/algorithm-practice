# iterate through 1-100
# if divisible by 15 print FizzBuzz
# if divisible by 5 print Buzz
# if divisible by 3 print Fizz
# if none of the above pass just print the current iterator

def print_fizz_buzz():
    for number in range(1, 101):
        if number % 15 == 0:
            print('Fizz Buzz')
        elif number % 5 == 0:
            print('Buzz')
        elif number % 3 == 0:
            print('Fizz')
        else:
            print(number)


print_fizz_buzz()

# FIZZBUZZ

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and 5 == 0:
            print(i, "- FizzBuzz")
        elif i % 3 == 0:
            print(i, "- Fizz")
        elif i % 5 == 0:
            print(i, "- Buzz")
        else:
            print(i)


# testando números de 1 a 20:
fizzbuzz(20)

'''
Today, we will be writing and analyzing two different recursive
cases in both space and time complexity:

1 - Factorial (not to be confused with factorial time)

Where n! = n*(n-1)*(n-2)*…*1, and 0! = 1 by definition.

2 - Power

Where n^m = n * (n ^ m-1), anything to the power of 0 is 1

'''

# Big O -> O(n) Linear (for space and time)
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)

# Big O -> O(n) Linear, where n is the absolute value of exponent
# (both space and time)
def power(base, exp):
    if base == 0:
        print("The base is 0!")
        return 0
    elif exp == 0:
        print("The exponent is 0!")
        return 1
    elif exp == 1 or base == 1:
        print("The exponent or base is 1!")
        return base
    elif exp > 1:
        print("This is the postive recursive step!")
        return base * power(base, exp - 1)
    else:
        print("This is the negative recursive step!")
        return power(base, exp + 1)/base


if __name__ == '__main__':
    #print(factorial(5))
    #print(power(3, 4))
    print(power(5, -3))
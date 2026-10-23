def is_even(num:int) -> bool:
    return num % 2 == 0

def max_of_three(a:int|float, b:int|float, c:int|float) -> int|float:
    return max([a,b,c])

def power(base:int|float, exp:int|float=2) -> int|float:
    return base ** exp

print("IsEven:")
print("IsEven(4) =", is_even(4))
print("IsEven(7) =", is_even(7))
print("IsEven(0) =", is_even(0))

print("\nMaxOfThree:")
print("MaxOfThree(3, 8, 5) =", max_of_three(3, 8, 5))
print("MaxOfThree(-7, -2, -10) =", max_of_three(-7, -2, -10))
print("MaxOfThree(4.5, 4.5, 2) =", max_of_three(4.5, 4.5, 2))

print("\npower:")
print("power(5) =", power(5))
print("power(2, 3) =", power(2, 3))
print("power(4, -1) =", power(4, -1))
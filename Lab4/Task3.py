def power(base: int | float, exp: int = 2) -> int | float:
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)

    return base * power(base, exp - 1)


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Число має бути невід’ємним")

    return 1 if number == 0 else number * factorial(number - 1)


print("power:")
print("power(2, 3) =", power(2, 3))
print("power(5, 0) =", power(5, 0))
print("power(2, -3) =", power(2, -3))

print("\nfactorial:")
print("factorial(0) =", factorial(0))
print("factorial(1) =", factorial(1))
print("factorial(5) =", factorial(5))
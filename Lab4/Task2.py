def sum_list(numbers: list[int | float]) -> int | float:
    return sum(numbers)

NumStats = dict[str, int | float]
def stats(*numbers: int | float) -> NumStats:
    total = sum(numbers)

    return {
        "min": min(numbers),
        "max": max(numbers),
        "sum": total,
        "avg": total / len(numbers),
    }

print("sum_list:")
print("sum_list([1, 2, 3]) =", sum_list([1, 2, 3]))
print("sum_list([2.5, 3.5]) =", sum_list([2.5, 3.5]))
print("sum_list([]) =", sum_list([]))

print("\nstats:")
print("stats(5) =", stats(5))
print("stats(2, 8) =", stats(2, 8))
print("stats(-3, 2.5, 7, 1.5) =", stats(-3, 2.5, 7, 1.5))
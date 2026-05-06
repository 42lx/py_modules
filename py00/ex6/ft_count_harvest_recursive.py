def rec(i: int):
    if i > 1:
        rec(i - 1)
    print("Day", i)

def ft_count_harvest_recursive():
    days: int = int(input("Days until harvest: "))
    rec(days)
    print("Harvest time!")

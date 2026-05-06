def ft_count_harvest_recursive():
    def rec(i: int):
        if i > 1:
            rec(i - 1)
        print("Day", i)
    days: int = int(input("Days until harvest: "))
    rec(days)
    print("Harvest time!")

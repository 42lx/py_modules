def ft_harvest_total():
    weight: int = 0
    for i in [1, 2, 3]:
        weight += int(input("Day " + str(i) + " harvest: "))
    print("Total harvest:", weight)

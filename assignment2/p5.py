monthly_incomes = ( ("January", 5000), ("February", 5500),
("March", 6000), ("April", 5800),
("May", 6200), ("June", 7000),
("July", 7500), ("August", 7300),
("September", 6800), ("October", 6500),
("November", 6000),("December", 5500) )

print("Total income :",sum(a[1] for a in monthly_incomes))
Quarter = 0
for idx,(month, sal) in enumerate(monthly_incomes):
    print(f"{month}: {sal}")
    Quarter += sal
    if idx%3 == 2:
        print("-"*10)
        print(f"Quarter: {Quarter}\n\n")
        Quarter = 0

def calculate_bill(units):
    if units <= 100:
        return units * 2.5
    elif units <= 200:
        return (100 * 2.5) + (units - 100) * 3.5
    else:
        return (100 * 2.5) + (100 * 3.5) + (units - 200) * 5.0

def main():
    n = int(input("Enter number of customers: "))
    total_revenue = 0

    for i in range(1, n + 1):
        print(f"\nCustomer {i}")
        name = input("Enter customer name: ")
        units = float(input("Enter units consumed: "))

        bill = calculate_bill(units)
        total_revenue += bill

        print(f"Bill for {name}: {bill:.2f}")


    print(f"Total Revenue : {total_revenue:.2f}")

main()




























# n = int(input("Enter number of customers "))
# name = input("enter name ")
# units = int(input("Enter units used  "))

# if(units >= 0 and units <= 100):
#     cost1 = units * 25
#     print(cost1)

# elif(units >= 101 and units <= 200):
#     cost2 = (100 * 25) + (units-100) * 39
#     print(cost2)

# else:
#     cost3 = (100 * 25) + (100 * 39) + (units-200) * 50
#     print(cost3)

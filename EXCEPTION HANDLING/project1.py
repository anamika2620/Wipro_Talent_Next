
try:
    filename = input("Enter the file name: ") + ".txt"

    file = open(filename, "r")
    lines = file.readlines()

    items = 0
    free_items = 0
    amount = 0
    discount = 0

    for line in lines:
        line = line.strip()

        if line == "":
            continue   # blank line skip

        name, price = line.split()

        if name.lower() == "discount":
            discount = int(price)

        elif price.lower() == "free":
            free_items += 1

        else:
            items += 1
            amount += int(price)

    final_amount = amount - discount

    print("No of items purchased:", items)
    print("No of free items:", free_items)
    print("Amount to pay:", amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

    file.close()

except FileNotFoundError:
    print("File not found!")

except ValueError:
    print("Invalid file data!")

except Exception as e:
    print("Error:", e)

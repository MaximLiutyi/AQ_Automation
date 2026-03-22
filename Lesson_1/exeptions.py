num = None
while num is None:

    try:
        num = int(input("Enter a number: "))
        num += 5
        print(num)
    except ValueError:
        print("Please enter a number")


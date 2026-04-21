def main():
    print("Welcom to our cinema")
    toPay = 0
    try:
        age = int(input("What is your age? "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if age < 18:
        toPay += 7
    else:
        toPay += 12
    popCorn = input("Would you like some popcorn? say 'yes' or 'no'")
    if popCorn.lower() == 'yes':
        toPay += 5
    print("The sum to pay is: {}$ ".format(toPay))


if __name__ == "__main__":
    main()
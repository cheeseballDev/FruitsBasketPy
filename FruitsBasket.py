def main():
    basket = []
    while True:
        try:
            number_of_fruits = int(input("How many fruits would you like to catch? "))
            break
        except:
            continue
    print("What fruit would you like to catch?, A for Apple, O for Orange, M for Mango, G for Guava")
    for i in range(number_of_fruits):
        user_input = input("Fruit", i, "of", number_of_fruits, ":").upper()
        basket.append(addFruit())
    print("Your basket now has: ", basket)
    while basket:
        user_eat_choice = str(input("Press E to eat fruit: ")).upper()
        if user_eat_choice != 'E':
            continue
        basket.pop()
        if basket:
            print("Your basket now has: ", basket)
    print("There are no more fruits in the basket! ")
    
def addFruit() -> str:
    while True:
        user_fruit = str(input()).upper()
        if user_fruit == 'A':
            return "Apple"
        elif user_fruit == 'O':
            return "Orange"
        elif user_fruit == 'M':
            return "Mango"
        elif user_fruit == 'G':
            return "Guava"
        else:
            continue

if __name__ == "__main__":
    main()
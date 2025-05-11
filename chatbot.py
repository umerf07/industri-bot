import smtplib

print("Welcome to Inventory Management Chatbot!")

# Chatbot Asking the question
ask = input("Do you have anything to request?: (y/n): ")

inventory = {}

# Options to choose for questioning
while True:
    def question():
        if ask == "y":
            options = input("What would you like help in?:\n 1. Add or Remove Inventory,\n 2. Request supplies to be sent over to a specific location,\n 3. If low on stock I can send a message to the manager to let him know,\n 4. Track incoming shipments: \n ")
            # Inventory view or changes
            if options == "1":
                    add_item = input("What would you like to add?: ")
                    quantity = int(input(f"Type in how much would you like to add of the {add_item}?: "))
                    if add_item in inventory:
                        inventory[add_item] += quantity
                        inventory.append({"name": add_item, "quantity": quantity})
                    else:
                        inventory[add_item] = quantity
                    print(f"{quantity} {add_item}(s) has been added")

                    remove_item = input("What would you like to remove?: ")
                    if remove_item in inventory:
                        quantity = int(input("How much would you like to remove?: "))
                        inventory[add_item] -= quantity
                    else:
                        inventory[add_item] = quantity
                    print(f"You have {quantity} of {add_item}(s) left.")
                
            # Requesting supplies to a specific location
            elif options == "2":
                message = input("Where do you want to send the supplies and where to?: ")
                print(message)
            # Low on Stock
            elif options == "3":
                print("We're low on stock please contact the supply manager immediately!...")
            # Tracking ongoing shipment vice versa
            elif options == "4":
                shipment_update = input("How far is the shipment to the site?: ")
                print(shipment_update)
            else:
                print("Invalid")

    question()

    # If you want to go again?
    go_again = input("Would you like to go again? (y/n): ")

    if go_again == "y":
        print("Let's go!")
        question()
    elif go_again == "n":
        print("Thanks for everything hope you have a good day!")
        break

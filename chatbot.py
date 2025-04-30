import smtplib

print("Welcome to my own personal Chatbot!")

# Chatbot Asking the question
ask = input("Do you have anything to request?: (y/n): ")

inventory = []

# Options to choose for questioning
while True:
    def question():
        if ask == "y":
            options = input("What would you like help in?:\n 1. Track Inventory,\n 2. Request supplies to be sent over to a specific location,\n 3. If low on stock I can send a message to the manager to let him know,\n 4. Track incoming shipments: \n ")
            if options == "1":
                print("Ok here is the full list: We have 2 bananas and 5 apples.")
            elif options == "2":
                message = input("Where do you want to send the supplies and where to?: ")
                print(message)
            elif options == "3":
                print("We're low on stock please contact the supply manager immediately!...")
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

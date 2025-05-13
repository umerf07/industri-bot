import smtplib
from email.message import EmailMessage
import csv

print("Welcome to Inventory Management Chatbot!")

# Chatbot Asking the question
ask = input("Do you have anything to request?: (y/n): ")

filename = "inventory.csv"
inventory = {}

# Options to choose for questioning
while True:
    def question():
        if ask == "y":
            options = input("What would you like help in?:\n 1. Add or Remove Inventory,\n 2. Request supplies to be sent over to a specific location,\n 3. If low on stock I can send a message to the manager to let him know,\n 4. Track incoming shipments: \n ")
            # Inventory view or changes
            if options == "1":
                    global inventory
                    item = input("What would you like to add?: ")
                    quantity = int(input(f"Type in how much would you like to add of the {item}?: "))
                    if item in inventory:
                        inventory[item] += quantity
                        inventory.append({"name": item, "quantity": quantity})
                    else:
                        inventory[item] = quantity
                    print(f"{quantity} {item}(s) has been added")
                    with open("inventory.csv", "w") as file:
                        writer = csv.writer(file)
                        writer.writerow(["item", "quantity"])
                        for key, value in inventory.items():
                            writer.writerow([key, value])
                    
                    print("Inventory updated")
                
                    item = input("What would you like to remove?: ")
                    if item in inventory:
                        quantity = int(input(f"How much would you like to remove the {item}?: "))
                        inventory[item] -= quantity
                    else:
                        inventory[item] = quantity
                    print(f"You have {quantity} of {item}(s) left.")
                    with open("inventory.csv", "w", newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(["item", "quantity"])
                        for key, value in inventory.items():
                            writer.writerow([key, value])
                    
                    print("Inventory updated")

            # Requesting supplies to a specific location
            elif options == "2":
                info = input("Where do you want to send the supplies and where to?: ")
                print(info)
            # Low on Stock
            elif options == "3":
                print("We're low on stock please contact the supply manager immediately!...")
                email = input("SENDER EMAIL: ")
                receiver_email = input("RECEIVER EMAIL: ")

                subject = input("SUBJECT: ")
                message = input("MESSAGE: ")

                text = f"Subject: {subject}\n\n{message}"

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()

                server.login(email, "xcjpniffepbiqfay")

                server.sendmail(email, receiver_email, text)

                print("Email has been sent to " + receiver_email)
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

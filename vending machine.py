# This the Vending Machine's Welcome page
print("""

████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█
█░░░░░░▄▀░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░████████████░░▄▀░░██░░▄▀░░███░░▄▀░░█████████░░▄▀░░██░░▄▀░░█
█████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀░░░░░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█
█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█
█████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░████████████░░▄▀░░████░░▄▀░░█████████░░▄▀░░█░░▄▀░░██░░▄▀░░█
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█████░░░░░░█████░░░░░░██░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░███░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░░░▄▀▄▀░░█░░░░▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░█████████
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░█████████
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█
█░░▄▀▄▀░░▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█
█░░░░▄▀▄▀▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░▄▀▄▀░░█░░░░▄▀░░░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█
███░░░░▄▀░░░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█████░░░░░░█████░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░███░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░░░▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░█████████
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████
█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░░░▄▀░░░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░██████████░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████""")
#Items in the vending machine 
class VendingMachine:
    def __init__(self):
        self.menu = {
            'A1': {'name': 'Pepsi (Drinks)', 'price': 2.00,  'quantity': 10},
            'A2': {'name': 'Nestle water', 'price': 1.00,  'quantity': 5},
            'A3': {'name': 'Monster Energy', 'price': 3.00,  'quantity': 3},
            'A4': {'name': 'Ice Tea', 'price': 2.00,  'quantity': 12},
            'B1': {'name': 'Doritos (Snacks)', 'price': 1.00,  'quantity': 5},
            'B2': {'name': 'Lays', 'price': 0.50,  'quantity': 0},
            'B3': {'name': 'M&Ms', 'price': 1.50,  'quantity': 25},
            'B4': {'name': 'Takis', 'price': 3.00,  'quantity': 12},
            'B5': {'name': 'Oman Chips', 'price': 0.50,  'quantity': 79},
            'C1': {'name': 'Dairy Milk (Chocolate)', 'price': 1.25,  'quantity': 98},
            'C2': {'name': 'Galaxy', 'price': 3.50,  'quantity': 110},
            'C3': {'name': 'Toblerone', 'price': 4.00,  'quantity': 27},
            'C4': {'name': 'Hersheys', 'price': 2.50,  'quantity': 17},
            'D1': {'name': 'DU Prepaid Card 100 dhs', 'price': 100.50,  'quantity': 80},
            'D2': {'name': 'DU Prepaid Card 50 dhs', 'price': 50.50,  'quantity': 100},
            'D3': {'name': 'DU Prepaid Card 30 dhs', 'price': 30.50,  'quantity': 79},
            'D4': {'name': 'Etisalat Prepaid Card 100 dhs', 'price': 100.25,  'quantity': 98},
            'D5': {'name': 'Etisalat Prepaid Card 50 dhs', 'price': 50.25,  'quantity': 90},
            'D6': {'name': 'Etisalat Prepaid Card 30 dhs', 'price': 30.25,  'quantity': 89},
        }
        self.money_inserted = 0.0
        self.user_selection = None
#This is the display on the wending machine before the purchase
    def display_menu(self):
        print("Welcome to the BSU Vending Machine!")
        print("Menu:")
        for code, item in self.menu.items():
            print(f"{code}: {item['name']} - dhs {item['price']} : {item['quantity']} pcs ")
#This is where the insert money option comes in ,
#In this option we have to insert the amount of money added and then just enter the number 0 to finalise the amount.
    def accept_money(self):
        while True:
            try:
                money = float(input("Insert money (enter 0 when done): dhs"))
                if money == 0:
                    break
                elif money < 0:
                    print("Invalid amount. Please insert a positive amount.")
                else:
                    self.money_inserted += money
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
#Here the machine gives you an option to select an item that should be despenced.
    def select_item(self):
        while True:
            self.user_selection = input("Enter the code of the item you want to purchase: ")
            if self.user_selection in self.menu:
                break
            else:
                print("Invalid code. Please enter a valid code.")
#This is where the item is being despensed and it also shows the price of the item and the amount that should be returned to the customer.
#If the amount inserted is less it will also display insufficient funds and more amount money should be inserted into the vending machine.
#This is where the stock table also is , if the item is in stock it will normally dispense the item if the item is not in stock then it will display the message showing the item out of stock. Just for checking that item no 'B2' is kept out of stock.
    def dispense_item(self):
        item = self.menu[self.user_selection]
        if item['quantity'] > 0:
            if self.money_inserted >= item['price']:
                self.money_inserted -= item['price']
                item['quantity'] -= 1
                print(f"Dispensing {item['name']}. Enjoy!")
            else:
                print("Insufficient funds. Please insert more money.")
        else:
            print(f"Sorry, {item['name']} is out of stock.")

#This is where the machine returns the balance amount back to the customer 
#Or if the amount added is equal to the amount added into the machine Then a messag of no change will be displayed on the screen.
    def return_change(self):
        if self.money_inserted > 0:
            print(f"Returning cash: dhs {self.money_inserted}")
            self.money_inserted = 0
        else:
            print("No change to return.")
#This code provides a basic frame work for a vending machine simulation.
    def run(self):
        self.display_menu()
        self.accept_money()
        self.select_item()
        self.dispense_item()
        self.return_change()


# This is the example usage
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()

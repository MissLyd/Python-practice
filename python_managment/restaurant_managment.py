
class Restaurant:
    def __init__(self):
        self.menu_items = {} # Dico
        self.book_table = []
        self.customer_orders = []
    
    # Menu
    def add_item_to_menu(self,item,price):
        self.menu_items[item] = price

    def print_menu(self):
        print("\n Our menu: ")
        for item, price in self.menu_items.items():
            print(f"{item}: {price}DA")

    # Booking tables
    def book_tables(self,table_nbr):
        if table_nbr not in self.book_table:
            self.book_table.append(table_nbr)
            print(f"Table {table_nbr} booked successfully.")
        else:
            print(f"Table {table_nbr} already booked.")

    def print_table_reservations(self):
        print("Booked tables:")
        if self.book_table:
            for table_nbr in self.book_table:
                print(f"Table {table_nbr}.")
        else:
            print("No reservations yet.")

    # Orders
    def customer_order(self,order,table_nbr):
        order_details ={"table_number": table_nbr, "order": order}
        self.customer_orders.append(order_details)
        print(f"Order taken for table {table_nbr}: {order}")

    def print_orders(self):
        print("Customer orders:")
        if self.customer_orders:
            for order_details in self.customer_orders:
                print(f"Table {order_details['table_nbr']}: {order_details['order']}")
            else:
                print("No orders yet.")

def show_menu(menu_options):
    choice = input("Enter you choice: ")
    if choice =="0":
        print("See you again soon!")
        return 
    elif choice in menu_options:
        try: 
            menu_options[choice]()
        except ValueError:
                print("Invalid choice")
    else:
                print("Invalid choice")


my_restaurant = Restaurant()
customer_options = {
    "A" : my_restaurant.print_menu,
    "B" : lambda: my_restaurant.book_tables(int(input("Enter table number: "))),
    "C" : lambda: my_restaurant.customer_order(
        input("Enter order: "),
        int(input("Enter table number: "))
    )
}

employee_options = {
    "A": lambda: my_restaurant.add_item_to_menu(
        input("Enter item: "),
        int(input("Enter price: "))
    ),
    "B": my_restaurant.print_table_reservations,
    "C": my_restaurant.print_orders,

}

while True:
    person = input("Are you an employee or a customer? (answer customer/employee or 0 to exit): ")
    if person == "0":
        break
    elif person == "customer":
        while True:
            print("--------Welcome to our restaurant!--------")
            print("What can we do for you?")
            print("A- Show Menu") 
            print("B- Book a table")
            print("C- Order")
            print("0- Exit")
                
            show_menu(customer_options)

    elif person == "employee":
        while True:
            print("A- Add item to the menu")
            print("B- Show table reservations")
            print("C- Show orders")
            print("0- Exit")
            show_menu(employee_options)

    else:
        print("Invalid choice")
        
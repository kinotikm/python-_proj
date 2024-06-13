from clients import ClientsDB
from cars import CarsDB
from orders import OrdersDB
from colorama import init, Fore, Style

init(autoreset=True)

def print_menu():
    print(Fore.YELLOW + Style.BRIGHT + "\n===== CARS DATABASE MENU =====")
    print("1.) Add Client")
    print("2.) Add Car")
    print("3.) Add Order")
    print("4.) Search Client by Name")
    print("5.) Search Client by ID")
    print("6.) List Clients")
    print("7.) List Cars")
    print("8.) List Orders")
    print("9.) Delete Client")
    print("10.) Exit")
    print(Fore.YELLOW + "===============================")

def main():
    clients_db = ClientsDB()
    cars_db = CarsDB()
    orders_db = OrdersDB()

    clients_db.create_table()
    cars_db.create_table()
    orders_db.create_table()

    while True:
        print_menu()
        choice = input(Fore.CYAN + "Select an option: ")

        if choice == "1":
            name = input("Enter the name of the client: ")
            phone_number = input("Enter the phone number of the client: ")
            email = input("Enter the email of the client: ")
            clients_db.add_client(name, phone_number, email)

        elif choice == "2":
            brand = input("Enter the brand of the car: ")
            year_of_make = input("Enter the year of make: ")
            price = input("Enter the price: ")
            cars_db.add_car(brand, year_of_make, price)

        elif choice == "3":
            client_id = int(input("Enter the ID of the client: "))
            order_date = input("Enter the order date (YYYY-MM-DD): ")
            quantity = input("Enter the quantity: ")
            total_price = input("Enter the total price: ")
            orders_db.add_order(client_id, order_date, quantity, total_price)

        elif choice == "4":
            name = input("Enter the name of the client: ")
            clients = clients_db.search_client_by_name(name)
            for client in clients:
                print(Fore.GREEN + f"ID: {client[0]}, Name: {client[1]}, Phone: {client[2]}, Email: {client[3]}")

        elif choice == "5":
            client_id = int(input("Enter the ID of the client: "))
            client = clients_db.search_client_by_id(client_id)
            if client:
                print(Fore.GREEN + f"ID: {client[0]}, Name: {client[1]}, Phone: {client[2]}, Email: {client[3]}")
            else:
                print(Fore.RED + "Client does not exist")

        elif choice == "6":
            clients = clients_db.list_clients()
            for client in clients:
                print(Fore.GREEN + f"ID: {client[0]}, Name: {client[1]}, Phone: {client[2]}, Email: {client[3]}")

        elif choice == "7":
            cars = cars_db.list_cars()
            for car in cars:
                print(Fore.GREEN + f"Brand: {car[0]}, Year of Make: {car[1]}, Price: {car[2]}")

        elif choice == "8":
            orders = orders_db.list_orders()
            for order in orders:
                print(Fore.GREEN + f"Order ID: {order[0]}, Order Date: {order[1]}, Client Name: {order[2]}, Quantity: {order[3]}, Total Price: {order[4]}")

        elif choice == "9":
            client_id = int(input("Enter the ID of the client to delete: "))
            clients_db.delete_client(client_id)

        elif choice == "10":
            break

        else:
            print(Fore.RED + "Invalid input")

if __name__ == "_main_":
    main()
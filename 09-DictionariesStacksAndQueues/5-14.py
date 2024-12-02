import queue

def customer_service():
    customer_queue = queue.Queue()
    ticket_number = 1
    
    while True:
        print("\nCustomer Service System")
        print("1. Add new customer")
        print("2. Serve next customer")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            customer_queue.put(ticket_number)
            print(f"Customer with ticket number {ticket_number} added to the queue.")
            ticket_number += 1
        
        elif choice == '2':
            if customer_queue.empty():
                print("No customers in the queue to serve.")
            else:
                served_customer = customer_queue.get()
                print(f"Serving customer with ticket number {served_customer}.")
        
        elif choice == '3':
            print("Exiting the Customer Service System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

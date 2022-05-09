
from sys import exit
from StaycationBookingRecordInitaliser import StaycationBookingRecordInitaliser

class StaycationBookingRecordFactory:
    while 1:
        initalise = StaycationBookingRecordInitaliser()
        query = input(
            "Would you like to sort, search & update, filter or display (Enter 'exit' to quit): ").lower().strip()
        if query == "sort":
            types = input(
                "\n1. Bubble sort (Customer name) \n2. Selection sort (Package name)\n3. Insertion sort (Package cost)\nWhat would you like to sort: ").strip()
            if types == "1":
                initalise.bubble_sort()
            elif types == "2":
                initalise.selection_sort()
            elif types == "3":
                initalise.insertion_sort()
            else:
                print("Not a proper value for sort")
        elif query == "search & update":
            selection = input("1. Linear search (Customer name)\n2. Binary search (Package name)\nWhat would you like to search and update: ").strip()
            if selection == "1":
                print(initalise.linear_search(input("Customer name: ")))
            elif selection == "2":
                print(initalise.binary_search(input("Package name: ")))
            else:
                print("Not a proper value search & update")
        elif query == "filter":
            filterquery = input("1. Filter by package cost per pax\nWhat is your choice: ")
            if filterquery == "1":
                while 1:
                    try:
                        print(initalise.range_filter((input("Enter your range: "))))
                        break
                    except ValueError:
                        print("Not a proper range")
            else:
                print("Not a proper value for range filter")

        elif query == "display":
           [print(x) for x in initalise.initaliser]
        elif query == "exit":
            print("You have exited out.")
            exit()
        else:
            print("That is not a query")

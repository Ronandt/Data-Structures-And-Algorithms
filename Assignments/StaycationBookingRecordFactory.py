
from sys import exit
from StaycationBookingRecord import StaycationBookingRecord
from StaycationBookingRecordInitaliser import StaycationBookingRecordInitaliser


class StaycationBookingRecordFactory:
    initalise = StaycationBookingRecordInitaliser([
        StaycationBookingRecord("Sick Package", "Potimas", 12, 69.69),
        StaycationBookingRecord("Sick Package", "Mother", 2, 69.420),
        StaycationBookingRecord("Amazing Package", "Shiraori", 4, 21),
        StaycationBookingRecord("Royal Package", "Ronandt", 8, 727),
        StaycationBookingRecord("Royal Package", "Felmina", 423, 727.727),
        StaycationBookingRecord("Maximum Package", "D", 893, 177013),
        StaycationBookingRecord("Phantasmal Package", "D", 23, 10),
        StaycationBookingRecord("Mythical Package", "Sariel", 420, 65),
        StaycationBookingRecord("Legendary Package", "Gyurie", 1, 7),
        StaycationBookingRecord("Normal Package", "Sophia", 3, 3)])
    formating = 15 * "="
    formatingTwo = 90 * "*"
    while 1:
        query = input(
            f"\n{formating}CHOICES{formating}\n1.sort\n2.search & update\n3.filter\n4.display\n5.exit\n{formating}{formating}======\nWhat is your choice: ").lower().strip()
        if query == "1":
            types = input(f"\n{formating}SORT{formating}\n1. Bubble sort (Customer name)\n2. Selection sort (Package name)\n3. Insertion sort (Package cost)\n{formating}===={formating}\nWhat would you like to sort:").strip()
            if types == "1":
                print(initalise.bubble_sort())
            elif types == "2":
                print(initalise.selection_sort())
         
            elif types == "3":
                print(initalise.insertion_sort())
     
            else:
                print("Not a proper value for sort")
            print("\n"+formatingTwo)
            [print(x) for x in initalise.initaliser]
            print(formatingTwo)
        elif query == "2":
            selection = input(
                f"\n{formating}SEARCH{formating}\n1. Linear search (Customer name)\n2. Binary search (Package name)\n{formating}{formating}=====\nWhat would you like to search and update: ").strip()
            if selection == "1":
                print(initalise.linear_search(input("Customer name: ")))
            elif selection == "2":
                print(initalise.binary_search(input("Package name: ")))
            else:
                print("Not a proper value for search & update")
        elif query == "3":
            filterquery = input(
                f"\n{formating}FILTER{formating}\n1. Filter by package cost per pax\n{formating}{formating}\nWhat is your choice: ")
            if filterquery == "1":
                while 1:
                    try:
                        print(initalise.range_filter(
                            (input("Enter your range: "))))
                        break
                    except ValueError:
                        print("Not a proper range")
            else:
                print("Not a proper value for range filter")

        elif query == "4":
        
            print(f"\n{formatingTwo}")
            [print(x) for x in initalise.initaliser]
            print(f"{formatingTwo}")

        elif query == "5":
            print("You have exited out.")
            exit()
        else:
            print("That is not a query")

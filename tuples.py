 # 1. Tuple Mastery in Python
 

#Task1

my_tuple=[("Pheona", "Texas", "Nigeria"),("Bob", "Florida", "California")]
name = my_tuple[0][0]
name2 = my_tuple[1][0]

departure = my_tuple [0][1]
departure2 = my_tuple[1][1]

arrival = my_tuple[0][2]
arrival2 = my_tuple [1][2]


print("Itinerary 1:", name,"- From", departure, "to" , arrival)
print("Itinerary 2:", name2,"- From", departure2, "to" , arrival2)
     




 


#Task2

library_books = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

#Add functionality to insert new books into library.
#Ensure that adding a duplicate book is handled appropriately.

def add_new_books(library):
    
    for book, title in library_books:
        if library[0] == book:
            print("Book already exists")
            return library_books
    library_books.append(library)
    return library_books   
print(add_new_books(("Think and Grow Rich", "Napoleon Hill")))
print(add_new_books(("The Power of Now", "Eckhart Tolle")))
print(add_new_books(("Think and Grow Rich", "Napoleon Hill")))



#========================================3==========================================================
# Task 1: 

# Problem Statement:   Your task is to unpack each tuple and print the order details in a user-friendly format.

orders = [
 ("Alice", "Laptop", 1),
 ("Bob", "Camera", 2),
 ("Pheona", "Phone", 4),
 ("Eze" ,  "charger", 3)
]
for name, item, quantity, in orders:
 print(f"{name}, order placed! Item: '{item}' quantity: {quantity}.")




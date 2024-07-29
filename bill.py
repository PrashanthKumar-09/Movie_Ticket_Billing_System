seating_chart = []
rows = 5
seats_per_row = 10
def login():
    username=input("enter your username")
    password=input("enter your password")
    if username == "prashanth" and password == "123" :
        print('Login  Successful')
    else:
        print("Incorrect Username or Password .Try again")

login()

for i in range(rows):
    row = ["O"] * seats_per_row
    seating_chart.append(row)

def display_seating_chart():
    print("Seating Chart:")
    for row in seating_chart:
        print(" ".join(row))
    print()

def book_seat():
    display_seating_chart()
    row = int(input("Enter the row number (1-10): ")) - 1
    seat = int(input("Enter the seat number (1-50): ")) - 1
    if 0 <= row < rows and 0 <= seat < seats_per_row:
        if seating_chart[row][seat] == "O":
           seating_chart[row][seat] = "X"
           for i in range(rows):
                 row = ["O"] * seats_per_row
                 seating_chart.append(row)
           print("Seat booked successfully!")

        else:
            print("Sorry, this seat is already taken.")
    else:
        print("Invalid row or seat number. Please try again.")

while True:
    print("1. View available seats")
    print("2. Book a seat")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        display_seating_chart()
    elif choice == "2":
        book_seat()
    elif choice == "3":
         print("Thank you for using the movie reservation system. Goodbye!")
         break
    else:
        print("Invalid choice. Please select 1, 2,or 3")
        break
    

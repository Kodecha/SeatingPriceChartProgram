# Seating Price Chart Program
# By Brendan Kunderas
import random

def display_title():
    # This displays the title of the program with a description of its functions
    print("-----------------------------------------------")
    print("Seating Price Chart Program in Python")
    print()
    print("Created by: Brendan Kunderas")
    print("Created on: 7-24-23")
    print("Description: This program is designed to:")
    print("1. Create an airplane seating-chart")
    print("2. Display the seating-price chart")
    print("3. Find and display the highest seating-chart")
    print("4. Find and display the lowest seating-chart")
    print("5. Calculate the average Price")
    print("6. Find all seats (rows and columns) that have the lowest price")        
    print("7. Find all seats (rows and columns) that have the highest price")   
    print("8. Find a seat (row and column) based onm price entered by the user")
    print("-----------------------------------------------")

def create_seating_chart(row,column):
# This returns list of lists seating_price_chart by gen a rand num and assigning it to a seat.
    seating_price_chart = []
    for r in range(row): # len(chart_2d) is the number of rows
        seating_price_chart.append([]) # add an empty list to seating_price_chart
        for c in range(column): # len(chart_2d[r]) is the number of columns
            seating_price_chart[r].append(random.randint(500,999)) 

    return seating_price_chart

def display_seating_chart(seating_price_chart):
    # This displays the seating chart in a 2d list format.abs
    print("--------Current Seating-Price Chart--------")
    print(f"There are {len(seating_price_chart)} rows and {len(seating_price_chart[0])} columns")
    print()

    for r in range(len(seating_price_chart)): # len(seating_price_chart) is the number of rows
        for c in range(len(seating_price_chart[r])): # len(seating_price_chart[r]) is the number of columns
            # first column of each row gets an open bracket [ while last column gets a close bracket ]
            if c == 0:
                print("[" + str(seating_price_chart[r][c]) + ", ", end="")
            elif c == len(seating_price_chart[r]) - 1:
                print(str(seating_price_chart[r][c]) + "]\n", end="")
            else:
                print(str(seating_price_chart[r][c]) + ", ", end="")

    print("-------------------------------------------")

def find_max_value(seating_price_chart):
    # This returns the max value in the 2d list and its location
    max_value = seating_price_chart[0][0]
    max_row = 0
    max_column = 0

    for r in range(len(seating_price_chart)): # len(seating_price_chart) is the number of rows
        for c in range(len(seating_price_chart[r])): # len(seating_price_chart[r]) is the number of columns
            if seating_price_chart[r][c] > max_value:
                max_value = seating_price_chart[r][c]
                max_row = r
                max_column = c

    return max_value, max_row, max_column # returns the max value and its location as a tuple

def find_min_value(seating_price_chart):
    # This returns the min value in the 2d list and its location (reference find_max_value()
    min_value = seating_price_chart[0][0]
    min_row = 0
    min_column = 0

    for r in range(len(seating_price_chart)):
        for c in range(len(seating_price_chart[r])):
            if seating_price_chart[r][c] < min_value:
                min_value = seating_price_chart[r][c]
                min_row = r
                min_column = c

    return min_value, min_row, min_column # returns the min value and its location as a tuple

def calculate_average_price(seating_price_chart):
    # This returns the average price of all the seats in the 2d list
    total = 0
    for r in range(len(seating_price_chart)): # len(seating_price_chart) is the number of rows
        for c in range(len(seating_price_chart[r])): # len(seating_price_chart[r]) is the number of columns
            total += seating_price_chart[r][c]

    return total / (len(seating_price_chart) * len(seating_price_chart[0])) # returns the average price

def find_seats_with_price(seating_price_chart, price):
    # This returns a list of tuples of all the seats with the price entered by the user
    seats_with_price = []
    for r in range(len(seating_price_chart)): # len(seating_price_chart) is the number of rows
        for c in range(len(seating_price_chart[r])): # len(seating_price_chart[r]) is the number of columns
            if seating_price_chart[r][c] == price:
                seats_with_price.append((r, c))

    return seats_with_price # returns a list of tuples of all the seats with the price entered by the user

def display_seat_list(seat_list):
    # This displays a list of tuples in a readable format
    for seat in seat_list:
        print(f"Row: {seat[0]} Column: {seat[1]}")

def menu():

    # This gets the number of rows and columns from the user
    print ("Please enter the number of rows and columns for the seating chart to begin.")
    print ("Otherwise, enter 0 to exit the program.")

    while True:
        try:
            row = int(input("Enter the number of rows (1-30): ")) # This gets the number of rows from the user
            if row >= 1 and row <= 30:
                break
            elif row == 0:
                print("GoodBye...")
                exit()
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            column = int(input("Enter the number of columns (1-10): ")) # This gets the number of columns from the user
            if column >= 1 and column <= 10:
                break
            elif column == 0:
                print("GoodBye...")
                exit()
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # This creates the seating chart
    seating_price_chart = create_seating_chart(row,column)

    # This displays the seating chart
    display_seating_chart(seating_price_chart)

    # This prompts the user what to do next
    print("What would you like to do next?")
    print("1. Display the seating-price chart")
    print("2. Display the highest price")
    print("3. Display the lowest price")
    print("4. Calculate the average price")
    print("5. Find all seats with a specific price")
    print("6. Recreate the seating chart")
    print("7. Credits")
    print("0. Exit the program")

    # This gets the user's choice and validates it
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice >= 0 and choice <= 7:
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        if choice == 1: # Display the current seating-price chart
            display_seating_chart(seating_price_chart)
        elif choice == 2: # This displays the highest price and its location
            max_value, max_row, max_column = find_max_value(seating_price_chart)
            print()
            print(f"The highest price is {max_value} at row {max_row} column {max_column}")
            print()        
        elif choice == 3: # This displays the lowest price and its location
            lowest_value, lowest_row, lowest_column = find_min_value(seating_price_chart)
            print()
            print(f"The lowest price is {lowest_value} at row {lowest_row} column {lowest_column}")
            print()
        elif choice == 4: # This displays the average price and rounds it to 2 decimal places   
            print()
            print(f"The average price is {round(calculate_average_price(seating_price_chart), 2)}")
            print()
        elif choice == 5: # This displays all the seats with the price entered by the user
            try:
                seats_by_price = find_seats_with_price(seating_price_chart, int(input("Enter the price to search for: ")))
                if len(seats_by_price) == 0:
                    print()
                    print("No seats found with that price.")
                    print()
                else:
                    print()
                    display_seat_list(seats_by_price)
                    print()
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                print()
        elif choice == 6: # This recreates the seating chart
            return True
        elif choice == 7: # This displays the credits
            display_title()
        elif choice == 0: # This exits the program
            print("GoodBye...")
            exit()

        try:
            print("What would you like to do next?")
            print("1. Display the seating-price chart")
            print("2. Display the highest price")
            print("3. Display the lowest price")
            print("4. Calculate the average price")
            print("5. Find all seats with a specific price")
            print("6. Recreate the seating chart")
            print("7. Credits")
            print("0. Exit the program")
            
            choice = int(input("Enter your choice: "))
            if choice < 0 or choice > 6:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return False

def main():
    display_title()
    while True:
        if menu():
            continue
        else:
            break

if __name__ == "__main__":
    main()
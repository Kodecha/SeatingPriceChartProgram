import tkinter as tk
from tkinter import PhotoImage
import random

class SeatingChartGUI:  # GUI for the Seating Price Chart Program
    def __init__(self, root):
        self.root = root
        self.root.title("Seating Price Chart Program")
        self.create_widgets()

    def create_widgets(self): # Creates the widgets for the GUI
        self.display_title()

        # Entry for the number of rows
        self.row_entry = tk.Entry(self.root, width=10)
        self.row_entry.pack()
        tk.Label(self.root, text="Enter the number of rows (1-30):").pack()

        # Entry for the number of columns
        self.column_entry = tk.Entry(self.root, width=10)
        self.column_entry.pack()
        tk.Label(self.root, text="Enter the number of columns (1-10):").pack()

        # Button to create seating chart
        tk.Button(self.root, text="Create Seating Chart", command=self.create_seating_chart).pack()

        # Canvas to display seating chart
        self.canvas = tk.Canvas(self.root, width=800, height=400)
        self.canvas.pack()

    def display_title(self): # Displays the title of the program
        title_label = tk.Label(self.root, text="Seating Price Chart Program", font=("Helvetica", 16, "bold"))
        title_label.pack()
 
    def create_seating_chart(self): # Creates a seating chart based on the number of rows and columns entered
        try:
            num_rows = int(self.row_entry.get())
            num_columns = int(self.column_entry.get())
            seating_price_chart = self.generate_seating_chart(num_rows, num_columns)
            self.display_seating_chart(seating_price_chart)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid numbers for rows and columns.")

    def generate_seating_chart(self, rows, columns): # Returns a 2D list of random prices
        seating_price_chart = []
        for r in range(rows):
            seating_price_chart.append([])
            for c in range(columns):
                seating_price_chart[r].append(random.randint(500, 999))
        return seating_price_chart

    def display_seating_chart(self, seating_price_chart): # Displays the seating chart on the canvas
        self.canvas.delete("all")  # Clear canvas

        seat_width = 50 # Width of each seat
        seat_height = 50 # Height of each seat

        for r in range(len(seating_price_chart)): # len(seating_price_chart) is the number of rows
            for c in range(len(seating_price_chart[r])): # len(seating_price_chart[r]) is the number of columns
                price = seating_price_chart[r][c]
                x = c * seat_width
                y = r * seat_height

                # Rectangle outline around the seat
                self.canvas.create_rectangle(x, y, x + seat_width, y + seat_height, outline="black")

                # Seat image above each seat
                seat_image = PhotoImage(file="seat.png") # Must be a .png file!!
                self.canvas.create_image(x, y, anchor=tk.NW, image=seat_image)

                # Price text (smaller)
                self.canvas.create_text(x + seat_width // 2, y + seat_height // 2,
                                        text=str(price), font=("Helvetica", 8, "bold"))

def main():
    root = tk.Tk()
    app = SeatingChartGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

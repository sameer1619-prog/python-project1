import tkinter as tk
from tkinter import messagebox

class ModernSeatSystem:
    def __init__(self, root, rows=4, cols=6):
        self.root = root
        self.root.title("Smart Seat Allocation System")
        self.root.geometry("900x600")
        self.root.configure(bg="#1e1e2f")

        self.rows = rows
        self.cols = cols
        self.total_seats = rows * cols
        self.seats = [None] * self.total_seats

        # Title
        tk.Label(root, text="SMART SEAT ALLOCATION",
                 font=("Segoe UI", 20, "bold"),
                 bg="#1e1e2f", fg="white").pack(pady=15)

        # ===== Control Panel =====
        control_frame = tk.Frame(root, bg="#2c2f4a", bd=0)
        control_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(control_frame, text="Seat No:",
                 bg="#2c2f4a", fg="white").grid(row=0, column=0, padx=10)

        self.seat_entry = tk.Entry(control_frame, width=8)
        self.seat_entry.grid(row=0, column=1)

        tk.Label(control_frame, text="Roll No:",
                 bg="#2c2f4a", fg="white").grid(row=0, column=2, padx=10)

        self.roll_entry = tk.Entry(control_frame, width=10)
        self.roll_entry.grid(row=0, column=3)

        tk.Button(control_frame, text="Allocate",
                  bg="#00c853", fg="white",
                  command=self.allocate).grid(row=0, column=4, padx=10)

        tk.Button(control_frame, text="Deallocate",
                  bg="#d50000", fg="white",
                  command=self.deallocate).grid(row=0, column=5, padx=10)

        tk.Button(control_frame, text="Search",
                  bg="#2962ff", fg="white",
                  command=self.search).grid(row=0, column=6, padx=10)

        # ===== Statistics =====
        self.stats_label = tk.Label(root,
                                    text="",
                                    font=("Segoe UI", 12),
                                    bg="#1e1e2f",
                                    fg="white")
        self.stats_label.pack(pady=5)

        # ===== Seat Grid =====
        self.grid_frame = tk.Frame(root, bg="#1e1e2f")
        self.grid_frame.pack(pady=20)

        self.draw_grid()
        self.update_stats()

    # Draw seat grid
    def draw_grid(self):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        for i in range(self.total_seats):
            row = i // self.cols
            col = i % self.cols

            if self.seats[i] is None:
                color = "#424874"   # empty
                text = f"{i}\nEmpty"
            else:
                color = "#00e676"   # occupied
                text = f"{i}\n{self.seats[i]}"

            lbl = tk.Label(self.grid_frame,
                           text=text,
                           width=10,
                           height=4,
                           bg=color,
                           fg="white",
                           font=("Segoe UI", 10, "bold"),
                           relief="flat")
            lbl.grid(row=row, column=col, padx=8, pady=8)

    # Allocate seat
    def allocate(self):
        try:
            seat_no = int(self.seat_entry.get())
            roll_no = self.roll_entry.get()

            if seat_no < 0 or seat_no >= self.total_seats:
                messagebox.showerror("Error", "Invalid Seat Number")
            elif self.seats[seat_no] is None:
                self.seats[seat_no] = roll_no
                self.draw_grid()
                self.update_stats()
            else:
                messagebox.showwarning("Warning", "Seat Already Occupied")
        except:
            messagebox.showerror("Error", "Enter valid data")

    # Deallocate seat
    def deallocate(self):
        try:
            seat_no = int(self.seat_entry.get())
            if self.seats[seat_no] is not None:
                self.seats[seat_no] = None
                self.draw_grid()
                self.update_stats()
            else:
                messagebox.showwarning("Warning", "Seat Already Empty")
        except:
            messagebox.showerror("Error", "Enter valid seat number")

    # Linear Search
    def search(self):
        roll_no = self.roll_entry.get()
        for i in range(self.total_seats):
            if self.seats[i] == roll_no:
                messagebox.showinfo("Found",
                                    f"Roll No {roll_no} found at Seat {i}")
                return
        messagebox.showwarning("Not Found", "Roll Number Not Found")

    # Update statistics
    def update_stats(self):
        occupied = sum(1 for seat in self.seats if seat is not None)
        empty = self.total_seats - occupied
        self.stats_label.config(
            text=f"Total Seats: {self.total_seats}   |   "
                 f"Occupied: {occupied}   |   Empty: {empty}"
        )


# Run
root = tk.Tk()
app = ModernSeatSystem(root, rows=4, cols=6)
root.mainloop()
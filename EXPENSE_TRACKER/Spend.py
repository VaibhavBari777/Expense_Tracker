import customtkinter as ctk

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("600x600")

        # Frame 1
        frame1 = ctk.CTkFrame(self.root, width=1500, height=650)
        frame1.pack(side=ctk.LEFT, padx=5, pady=5)
        
        
        # Frame 2 - In Hand Salary
        frame2 = ctk.CTkFrame(frame1, width=330, height=50)
        frame2.pack(side=ctk.TOP, anchor=ctk.NE, padx=5, pady=5)

        ctk.CTkLabel(frame2, text="Money to Spend", font=("Arial", 18)).pack(side=ctk.LEFT, padx=5)
        self.salary_entry = ctk.CTkEntry(frame2, font=("Arial", 18), width=300)
        self.salary_entry.pack(side=ctk.LEFT, padx=5)
        ctk.CTkButton(frame2, text="Save", font=("Arial", 18), width=10, height=2, command=self.save_salary).pack(side=ctk.LEFT, padx=5)

        # Frame 3 - Saved Money
        frame3 = ctk.CTkFrame(frame1, width=330, height=50)
        frame3.pack(side=ctk.TOP, anchor=ctk.NE, padx=5, pady=5)

        ctk.CTkLabel(frame3, text="You will save money per month", font=("Arial", 18)).pack(side=ctk.LEFT, padx=5)
        self.saved_money_label = ctk.CTkLabel(frame3, text="", font=("Arial", 18))
        self.saved_money_label.pack(side=ctk.LEFT, padx=5)

        # Frame 4 - Expense Entry Boxes
        frame4 = ctk.CTkFrame(frame1, width=330, height=300)
        frame4.pack(side=ctk.TOP,padx=200, pady=5)
       
        

        self.expense_entries = {}
        expenses = ["House Rent", "EMI", "Food and Grocery", "Travelling", "Healthcare", "Clothes & Personal Care"]
        for expense in expenses:
            label = ctk.CTkLabel(frame4, text=expense, font=("Arial", 18))
            label.pack(side=ctk.TOP, anchor=ctk.W, padx=5, pady=5)

            entry = ctk.CTkEntry(frame4, font=("Arial", 18), width=200)
            entry.pack(side=ctk.TOP, anchor=ctk.W, padx=5, pady=5)

            self.expense_entries[expense] = entry

    def save_salary(self):
        try:
            salary = float(self.salary_entry.get())
            total_expense = sum(float(entry.get()) for entry in self.expense_entries.values())
            saved_money = salary - total_expense
            self.saved_money_label.configure(text=f"₹{saved_money:.2f}")


        except ValueError:
            # Handle invalid input
            ctk.tkinter.messagebox.showerror("Error", "Please enter valid numbers.")

if __name__ == "__main__":
    root = ctk.CTk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

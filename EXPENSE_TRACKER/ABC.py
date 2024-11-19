from tkinter import Tk, Frame, Entry, Button, Label

# Function to calculate future value based on investment amount and years
def calculate_investment():
    try:
        investment_amount = float(entry_investment.get())
        years = int(entry_years.get())

        # Realistic average annual growth rates for investments (as decimals)
        mutual_funds_growth_rate = 0.07  # 7% average annual growth rate for mutual funds
        etf_growth_rate = 0.08  # 8% average annual growth rate for ETFs
        real_estate_growth_rate = 0.05  # 5% average annual growth rate for real estate

        # Calculate future values for mutual funds, ETFs, and real estate
        mutual_funds_value = investment_amount * (1 + mutual_funds_growth_rate) ** years
        etf_value = investment_amount * (1 + etf_growth_rate) ** years
        real_estate_value = investment_amount * (1 + real_estate_growth_rate) ** years

        # Additional text to be added to the result
        additional_text = "Here are the projected values for investment after {} years:".format(years)

        # Construct the result message with realistic growth rates and increased line spacing
        result_message = (
            f"{additional_text}\n\n"
            f"\u2022 Mutual Funds: Rs {mutual_funds_value:.2f}\n"
            f"\u2022 ETFs: Rs {etf_value:.2f}\n"
            f"\u2022 Real Estate: Rs {real_estate_value:.2f}"
        )

        # Update the label to display the result with bullet points and increased line spacing
        result_label.config(text=result_message)

    except Exception as e:
        result_label.config(text="Error: " + str(e))

# Create main window
root = Tk()
root.title("Investment Calculator")
root.geometry("600x400")

# Create Frame widget
frame = Frame(root, width=600, height=400)
frame.pack(padx=10, pady=10)

# Create labels, entry fields, and calculate button with larger font size and centered alignment
font_size = 20
entry_font = ("Arial", font_size)

label_investment = Label(frame, text="Enter Investment Amount (Rs):", font=entry_font)
label_investment.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_investment = Entry(frame, font=entry_font, width=10)
entry_investment.grid(row=0, column=1, padx=10, pady=10)

label_years = Label(frame, text="Enter Number of Years:", font=entry_font)
label_years.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_years = Entry(frame, font=entry_font, width=10)
entry_years.grid(row=1, column=1, padx=10, pady=10)

calculate_button = Button(frame, text="Calculate", font=("Arial", font_size), command=calculate_investment)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Label to display the result with bullet points and increased line spacing
result_label = Label(frame, text="", font=("Arial", 18), justify="left")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")

# Run the main loop
root.mainloop()

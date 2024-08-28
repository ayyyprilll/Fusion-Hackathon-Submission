import tkinter as tk
from tkinter import messagebox

import tkinter as tk
from tkinter import messagebox

# Step 3: Create the Main Application Window
root = tk.Tk()
root.title("Weather Forecast Device")
root.geometry("300x200")  # Width x Height

# Label for location input
location_label = tk.Label(root, text="Enter Location:")
location_label.pack(pady=10)

# Entry widget for location input
location_entry = tk.Entry(root)
location_entry.pack(pady=5)

def predict_weather():
    location = location_entry.get()
    if location:
        # Simulate a weather prediction (this should be replaced with actual prediction logic)
        weather = "Sunny" if location.lower() == "lagos" else "Rainy"
        messagebox.showinfo("Weather Prediction", f"The weather in {location} is {weather}.")
    else:
        messagebox.showwarning("Input Error", "Please enter a location.")

# Button to predict weather
predict_button = tk.Button(root, text="Predict Weather", command=predict_weather)
predict_button.pack(pady=20)

root.mainloop()

input("Press Enter to exit")

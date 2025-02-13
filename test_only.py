import tkinter as tk
from PIL import Image, ImageTk  # Import PIL for JPG support

# Function to insert text into the entry field
def on_button_click(value):
    entry.insert(tk.END, value)

# Function to clear the last character in the entry field
def clear_text():
    current_text = entry.get()
    entry.delete(len(current_text) - 1, tk.END)  # Delete last character
    
# Function to handle enter key and display results
def enter_pressed():
    user_input = entry.get()
    display_data(f"Entered: {user_input}\nFetching data...\n")
    fetch_data(user_input)  # Simulate fetching from database

# Function to simulate fetching data from a database
def fetch_data(user_input):
    # Simulate returning data (Replace this with actual database query)
    mock_result = f"Data for {user_input}: Sample Database Result"
    display_data(mock_result)

# Function to update the text display
def display_data(data):
    result_display.config(state=tk.NORMAL)  # Enable editing
    result_display.delete(1.0, tk.END)  # Clear previous results
    result_display.insert(tk.END, data)  # Insert new data
    result_display.config(state=tk.DISABLED)  # Disable editing

# Create main window
root = tk.Tk()
root.title("Adaptive Keyboard")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size to full screen
root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg="skyblue")

# Entry widget for input
tk.Label(root, text="PaRECEIVED", font=("Arial", int(screen_width * 0.02)), bg="lightgray").pack()
entry = tk.Entry(root, font=("Arial", int(screen_width * 0.03)), justify="center", bd=5)
entry.pack(pady=10, padx=20, fill="both", expand=True)

# **New Result Display Widget**
result_display = tk.Text(root, font=("Arial", int(screen_width * 0.015)), height=2, wrap="word", bg="white", state=tk.DISABLED)
result_display.pack(pady=10, padx=20, fill="both", expand=True)

# Keyboard frame (Centered)
keyboard_frame = tk.Frame(root, bg="lightgray")
keyboard_frame.pack(pady=5, expand=True)

num_frame = tk.Frame(keyboard_frame, bg="lightgray")
num_frame.pack()

alpha_frame = tk.Frame(keyboard_frame, bg="lightgray")
alpha_frame.pack()

bottom_frame = tk.Frame(root, bg="lightgray")
bottom_frame.pack(pady=5, fill="x")

# Define button characters
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]  # 10 buttons
alphabets = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

# Dynamically adjust button sizes (Smaller sizes for better alignment)
btn_font_size = int(screen_width * 0.015)  # Smaller font size
btn_width = 5  # Fixed width
btn_height = 2  # Fixed height

# Add number buttons in center alignment
for i, num in enumerate(numbers):
    btn = tk.Button(num_frame, text=num, font=("Arial", btn_font_size), width=btn_width, height=btn_height,
                    command=lambda n=num: on_button_click(n))
    btn.grid(row=0, column=i, padx=2, pady=2)

# Add alphabet buttons
row, col = 0, 0
for char in alphabets:
    btn = tk.Button(alpha_frame, text=char, font=("Arial", btn_font_size), width=btn_width, height=btn_height,
                    command=lambda c=char: on_button_click(c))
    btn.grid(row=row, column=col, padx=2, pady=2)

    col += 1
    if col >= 13:  # Move to next row after 13 columns
        col = 0
        row += 1

# Add Clear and Enter buttons (Smaller sizes)
clear_btn = tk.Button(bottom_frame, text="Clear", font=("Arial", btn_font_size, "bold"),
                      bg="red", fg="white", width=10, height=2, command=clear_text)
clear_btn.pack(side=tk.LEFT, padx=10, expand=True, fill="both")

enter_btn = tk.Button(bottom_frame, text="Enter", font=("Arial", btn_font_size, "bold"),
                      bg="green", fg="white", width=10, height=2, command=enter_pressed)
enter_btn.pack(side=tk.RIGHT, padx=10, expand=True, fill="both")

# Run the application
root.mainloop()

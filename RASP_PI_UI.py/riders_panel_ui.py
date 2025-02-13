import tkinter as tk
from PIL import Image, ImageTk  # Import PIL for JPG support

# Function to insert text into the entry field
def on_button_click(value):
    entry.insert(tk.END, value)

# Function to clear the entry field
# Function to clear the last character in the entry field
def clear_text():
    current_text = entry.get()
    entry.delete(len(current_text) - 1, tk.END)  # Delete last character
    
# Function to handle enter key
def enter_pressed():
    print("Entered:", entry.get())

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

# Keyboard frames (Adjusted Sizes)
keyboard_frame = tk.Frame(root, bg="lightgray")
keyboard_frame.pack(fill="both", expand=True)

num_frame = tk.Frame(keyboard_frame, bg="lightgray")
num_frame.pack(pady=(5, 2), fill="x")

alpha_frame = tk.Frame(keyboard_frame, bg="lightgray")
alpha_frame.pack(pady=(2, 0), fill="x")

# Image Frame (Scales with screen)
image_frame = tk.Frame(root, bg="lightgray")
image_frame.pack(pady=(0, 5), fill="x")

# Load and display the image
image_path = "RASP_PI_UI.py/286-2862255_top-tier-japan-japan-jdm-logo-png-transparent.png"  # Update with correct image path
pil_img = Image.open(image_path)
pil_img = pil_img.resize((300, 200))  # Adjust the size of the picture
img = ImageTk.PhotoImage(pil_img)

image_label = tk.Label(image_frame, image=img, bg="lightgray")
image_label.pack()

bottom_frame = tk.Frame(root, bg="lightgray")
bottom_frame.pack(pady=5, fill="x")

# Define button characters
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]  # 10 buttons
alphabets = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

# Dynamically adjust button sizes
btn_font_size = int(screen_width * 0.02)  # Responsive font size
btn_width = int(screen_width * 0.005)  # Responsive width
btn_height = int(screen_height * 0.002)  # Responsive height

# Center the number buttons
col_count = 13
col_offset = (col_count - len(numbers)) // 2  # Center-align the numbers

for i, num in enumerate(numbers):
    btn = tk.Button(num_frame, text=num, font=("Arial", btn_font_size), width=btn_width, height=btn_height,
                    command=lambda n=num: on_button_click(n))
    btn.grid(row=0, column=i + col_offset, padx=2, pady=2)

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

# Add Clear and Enter buttons (Adaptive Size)
clear_btn = tk.Button(bottom_frame, text="Clear", font=("Arial", btn_font_size, "bold"),
                      bg="red", fg="white", width=int(screen_width * 0.02), height=int(screen_height * 0.002), command=clear_text)
clear_btn.pack(side=tk.LEFT, padx=10, expand=True, fill="both")

enter_btn = tk.Button(bottom_frame, text="Enter", font=("Arial", btn_font_size, "bold"),
                      bg="green", fg="white", width=int(screen_width * 0.02), height=int(screen_height * 0.002), command=enter_pressed)
enter_btn.pack(side=tk.RIGHT, padx=10, expand=True, fill="both")

# Run the application
root.mainloop()

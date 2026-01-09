import random
import math
import tkinter as tk
from tkinter import messagebox, filedialog
import winsound 

# --- 1. THE BRAIN (Randomized Range & Logic) ---
# The computer picks a random playground size
lower = random.randint(1, 20)
upper = random.randint(100, 500)
secret_number = random.randint(lower, upper)

# Binary Search Formula: log2(upper - lower + 1)
chances = round(math.log(upper - lower + 1, 2))
attempts = 0
hints_left = 3

# --- 2. GAME FUNCTIONS ---

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1
        
        # Logic for a correct guess
        if guess == secret_number:
            try:
                winsound.PlaySound("win.wav", winsound.SND_ASYNC)
            except:
                pass
            messagebox.showinfo("WINNER!", f"Congratulations! You did it in {attempts} try!")
            root.destroy()
            
        # Logic for running out of chances
        elif attempts >= chances:
            messagebox.showinfo("GAME OVER", f"The number was {secret_number}\nBetter Luck Next Time!")
            root.destroy()
            
        # Feedback logic: too small or too high
        elif guess < secret_number:
            label_result.config(text="Try Again! You guessed too small.", fg="#FFD700")
        elif guess > secret_number:
            label_result.config(text="Try Again! You guessed too high.", fg="#FF4500")
            
        entry.delete(0, tk.END)
    except ValueError:
        label_result.config(text="Please enter a valid number!", fg="white")

def give_hint():
    global hints_left
    if hints_left > 0:
        used = 3 - hints_left 
        
        # Your specific "Squeeze" levels
        if used == 0:     # Hint 1: 50 numbers wide
            spread = 50
        elif used == 1:   # Hint 2: 30 numbers wide
            spread = 30
        else:             # Hint 3: 15 numbers wide
            spread = 15
            
        # Calculate a random range that STILL contains the secret number
        h_low = max(lower, secret_number - random.randint(0, spread))
        h_high = min(upper, h_low + spread)
        
        label_range.config(text=f"Hint: Between {h_low} and {h_high}", fg="#F1C40F")
        hints_left -= 1
        hint_btn.config(text=f"Hints Left: {hints_left}")
        
        if hints_left == 0:
            hint_btn.config(state="disabled", bg="grey")
    else:
        messagebox.showinfo("Hints", "No more hints available!")

def change_bg():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.gif")])
    if file_path:
        new_bg = tk.PhotoImage(file=file_path)
        bg_label.config(image=new_bg)
        bg_label.image = new_bg 
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Lift all components above the new background
        for widget in [label_title, label_range, entry, btn, hint_btn, bg_btn, label_result]:
            widget.lift()

# --- 3. THE DESIGN (User Interface) ---
root = tk.Tk()
root.title("Advanced Guessing Game")
root.geometry("400x600")

# Set the initial background
bg_label = tk.Label(root, bg="#2C3E50")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title and Subheading
label_title = tk.Label(root, text="NUMBER GUESSING GAME", font=("Impact", 24), bg="#2C3E50", fg="white")
label_title.pack(pady=(30, 0))

label_range = tk.Label(root, text=f"Between {lower} and {upper}", font=("Arial", 14, "italic"), bg="#2C3E50", fg="#BDC3C7")
label_range.pack(pady=(0, 10))

# Interaction Widgets
entry = tk.Entry(root, font=("Arial", 32), width=5, justify='center')
entry.pack(pady=20)

btn = tk.Button(root, text="GUESS!", command=check_guess, bg="#27AE60", fg="white", font=("Arial", 14, "bold"), width=15)
btn.pack(pady=10)

hint_btn = tk.Button(root, text=f"Hints Left: {hints_left}", command=give_hint, bg="#F39C12", fg="white", font=("Arial", 10, "bold"), width=15)
hint_btn.pack(pady=5)

bg_btn = tk.Button(root, text="Upload Background Photo", command=change_bg, bg="#3498DB", fg="white", width=20)
bg_btn.pack(pady=20)

# Chances Display
label_result = tk.Label(root, text=f"Total Chances: {chances}", font=("Arial", 12), bg="#2C3E50", fg="white")
label_result.pack(pady=10)

root.mainloop()
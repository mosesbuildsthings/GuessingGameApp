import random
import math
import tkinter as tk
from tkinter import messagebox, filedialog
import winsound 

# --- 1. THE BRAIN (Game Variables) ---
try:
    with open("highscore.txt", "r") as f:
        high_score = int(f.read())
except:
    high_score = 1

current_level = 1
total_score = 0 # NEW: Keeps track of your points
lower = 1
upper = 100
secret_number = random.randint(lower, upper)
chances = round(math.log(upper - lower + 1, 2))
attempts = 0
hints_left = 3

# --- 2. GAME FUNCTIONS ---

def celebrate():
    colors = ["#f1c40f", "#e74c3c", "#3498db", "#2ecc71", "#9b59b6", "#e67e22"]
    for _ in range(50):
        x = random.randint(0, 400)
        y = random.randint(0, 150)
        color = random.choice(colors)
        size = random.randint(5, 12)
        dot = canvas.create_oval(x, y, x+size, y+size, fill=color, outline="")
        root.after(2000, lambda d=dot: canvas.delete(d))

def next_level():
    global current_level, upper, secret_number, chances, attempts, hints_left, high_score
    if current_level >= high_score:
        high_score = current_level
        with open("highscore.txt", "w") as f:
            f.write(str(high_score))
            
    current_level += 1
    upper += 100 
    secret_number = random.randint(lower, upper)
    chances = round(math.log(upper - lower + 1, 2))
    attempts = 0
    hints_left = 3
    
    label_title.config(text=f"LEVEL {current_level}")
    label_range.config(text=f"Between {lower} and {upper}")
    label_highscore.config(text=f"Best: Level {high_score}")
    label_result.config(text=f"Chances: {chances}")
    hint_btn.config(text=f"Hints Left: {hints_left}", state="normal", bg="#F39C12")

def check_guess():
    global attempts, total_score
    try:
        guess = int(entry.get())
        attempts += 1
        
        if guess == secret_number:
            # --- BONUS POINTS CALCULATION ---
            bonus = (chances - (attempts - 1)) * 100
            total_score += bonus
            label_score.config(text=f"Score: {total_score}")
            
            celebrate()
            try:
                winsound.PlaySound("win.wav", winsound.SND_ASYNC)
            except:
                pass
            messagebox.showinfo("WINNER!", f"Correct! Bonus +{bonus} points!")
            next_level()
        elif attempts >= chances:
            messagebox.showinfo("GAME OVER", f"Better Luck Next Time!\nThe number was {secret_number}.")
            root.destroy()
        elif guess < secret_number:
            label_result.config(text="Try Again! Too small.", fg="#FFD700")
        elif guess > secret_number:
            label_result.config(text="Try Again! Too high.", fg="#FF4500")
        entry.delete(0, tk.END)
    except ValueError:
        label_result.config(text="Type a number!", fg="white")

# ... (Include give_hint and change_bg functions here from previous version)

# --- 3. THE DESIGN ---
root = tk.Tk()
root.title("Score Run Guessing Game")
root.geometry("400x750")

bg_label = tk.Label(root, bg="#2C3E50")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas = tk.Canvas(root, height=150, bg="#2C3E50", highlightthickness=0)
canvas.pack(fill="x")

label_title = tk.Label(root, text=f"LEVEL {current_level}", font=("Impact", 32), bg="#2C3E50", fg="white")
label_title.pack()

# NEW Score Label
label_score = tk.Label(root, text=f"Score: {total_score}", font=("Arial", 12, "bold"), bg="#2C3E50", fg="#3498DB")
label_score.pack()

label_highscore = tk.Label(root, text=f"Best: Level {high_score}", font=("Arial", 10, "bold"), bg="#2C3E50", fg="#27AE60")
label_highscore.pack()

# ... (Add the rest of the labels and buttons as before)

root.mainloop()

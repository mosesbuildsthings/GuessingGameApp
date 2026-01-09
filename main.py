import random
import math
import tkinter as tk
from tkinter import messagebox, filedialog
import winsound 

# --- 1. THE BRAIN (Game Variables & Memory) ---
try:
    with open("highscore.txt", "r") as f:
        high_score = int(f.read())
except:
    high_score = 1

current_level = 1
lower = 1
upper = 100
secret_number = random.randint(lower, upper)
chances = round(math.log(upper - lower + 1, 2)) # Binary search formula
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
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1
        
        if guess == secret_number:
            celebrate()
            try:
                winsound.PlaySound("win.wav", winsound.SND_ASYNC)
            except:
                pass
            messagebox.showinfo("LEVEL COMPLETE!", f"Great job! Level {current_level} cleared.")
            next_level()
        elif attempts >= chances:
            messagebox.showinfo("GAME OVER", f"Better Luck Next Time!\nThe number was {secret_number}.")
            root.destroy()
        elif guess < secret_number:
            label_result.config(text="Try Again! Too small.", fg="#FFD700") # Too small feedback
        elif guess > secret_number:
            label_result.config(text="Try Again! Too high.", fg="#FF4500") # Too high feedback
        entry.delete(0, tk.END)
    except ValueError:
        label_result.config(text="Type a number!", fg="white")

def give_hint():
    global hints_left
    if hints_left > 0:
        used = 3 - hints_left 
        spread = 50 if used == 0 else 30 if used == 1 else 15
        h_low = max(lower, secret_number - random.randint(0, spread))
        h_high = min(upper, h_low + spread)
        label_range.config(text=f"Hint: Between {h_low} and {h_high}", fg="#F1C40F")
        hints_left -= 1
        hint_btn.config(text=f"Hints Left: {hints_left}")
        if hints_left == 0: hint_btn.config(state="disabled", bg="grey")

def change_bg():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.gif")])
    if file_path:
        new_bg = tk.PhotoImage(file=file_path)
        bg_label.config(image=new_bg)
        bg_label.image = new_bg 
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        canvas.lift()
        for w in [label_title, label_highscore, label_range, entry, btn, hint_btn, bg_btn, label_result]: w.lift()

# --- 3. THE DESIGN ---
root = tk.Tk()
root.title("Confetti Level Game")
root.geometry("400x700")

bg_label = tk.Label(root, bg="#2C3E50")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Celebration Canvas
canvas = tk.Canvas(root, height=150, bg="#2C3E50", highlightthickness=0)
canvas.pack(fill="x")

label_title = tk.Label(root, text=f"LEVEL {current_level}", font=("Impact", 32), bg="#2C3E50", fg="white")
label_title.pack()

label_highscore = tk.Label(root, text=f"Best: Level {high_score}", font=("Arial", 10, "bold"), bg="#2C3E50", fg="#27AE60")
label_highscore.pack()

label_range = tk.Label(root, text=f"Between {lower} and {upper}", font=("Arial", 14, "italic"), bg="#2C3E50", fg="#BDC3C7")
label_range.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 32), width=5, justify='center')
entry.pack(pady=10)

btn = tk.Button(root, text="GUESS!", command=check_guess, bg="#27AE60", fg="white", font=("Arial", 14, "bold"), width=15)
btn.pack(pady=10)

hint_btn = tk.Button(root, text=f"Hints Left: {hints_left}", command=give_hint, bg="#F39C12", fg="white", font=("Arial", 10, "bold"), width=15)
hint_btn.pack(pady=5)

bg_btn = tk.Button(root, text="Custom Background", command=change_bg, bg="#3498DB", fg="white", width=20)
bg_btn.pack(pady=10)

label_result = tk.Label(root, text=f"Chances: {chances}", font=("Arial", 12), bg="#2C3E50", fg="white")
label_result.pack(pady=10)

root.mainloop()
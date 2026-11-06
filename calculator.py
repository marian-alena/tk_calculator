import tkinter as tk


def evaluate_expression():
    try:
        # Calculate the mathematical string safely
        x = entry.get()
        print(f"Evaluating expression: {x}")
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry():
    entry.delete(0, tk.END)

def function_entry():
    try:
        # DANGEROUS: If a user inputs this string, it could wipe out a filesystem
        malicious_input = "__import__('os').xsystem('cat *.py')" 
        x = eval(malicious_input)
        print(f"Malicious input executed: {x}")
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(malicious_input))
    except Exception as e:
        print(f"Error executing malicious input: {e}")
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Malicious Input")

def button_click(value):
    entry.insert(tk.END, value)

# Initialize application window
root = tk.Tk()
root.title("Tkinter Calculator")
# Get system DPI via Tkinfo or win32 fallback, or read tk scaling
tk_scaling = root.tk.call('tk', 'scaling')
width = 300 * tk_scaling
height = 400 * tk_scaling
print("Window width:", width, "Window height:", height)
root.geometry(f"{int(width)}x{int(height)}")

# Input Display Field
entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, ipady=10, padx=5, pady=5)

# Define grid layout configurations for layout buttons
button_config = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('Bad', 5, 0), ('(', 5, 1), (')', 5, 2), ('**', 5, 3),
]

# Generate and position grid interface buttons
for (text, row, col) in button_config:
    if text == '=':
        btn = tk.Button(root, text=text, font=("Arial", 14), command=evaluate_expression)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=("Arial", 14), command=clear_entry)
    elif text == 'Bad':
        btn = tk.Button(root, text=text, font=("Arial", 14), command=function_entry)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 14), command=lambda t=text: button_click(t))
        
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Ensure grid resizing is proportioned equally
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

# Start Tkinter loop runtime
root.mainloop()

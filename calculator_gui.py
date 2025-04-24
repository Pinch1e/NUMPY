import tkinter as tk
import numpy as np

# Define calculator functions
def add(x, y): return np.add(x, y)
def subtract(x, y): return np.subtract(x, y)
def multiply(x, y): return np.multiply(x, y)
def divide(x, y): return np.divide(x, y)

# GUI functionality
def calculate():
    x = float(entry1.get())
    y = float(entry2.get())
    operation = op.get()
    try:
        if operation == "Add":
            result.set(add(x, y))
        elif operation == "Subtract":
            result.set(subtract(x, y))
        elif operation == "Multiply":
            result.set(multiply(x, y))
        elif operation == "Divide":
            result.set(divide(x, y))
    except Exception as e:
        result.set(f"Error: {e}")

# Build GUI
root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

op = tk.StringVar(root)
op.set("Add")
tk.OptionMenu(root, op, "Add", "Subtract", "Multiply", "Divide").pack()

tk.Button(root, text="Calculate", command=calculate).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()

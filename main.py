import tkinter as tk
import functions as f


root = tk.Tk()

root.title("Calculator")
root.geometry("230x285")

previous = tk.Label(root, text="", width=12, height=1, bg="white", anchor='e', font=("Arial", 24)).grid(row=0, column=0, columnspan=4)
current = tk.Label(root, text="", width=12, height=1, bg="white", anchor='e', font=("Arial", 24)).grid(row=1, column=0, columnspan=4)


### Action buttons
button_clear = tk.Button(root, text="C",width=7, height=2).grid(row=2, column=0)
button_divide = tk.Button(root, text="/",width=7, height=2).grid(row=4, column=3)
button_multiply = tk.Button(root, text="*",width=7, height=2).grid(row=5, column=3)
button_subtract = tk.Button(root, text="-",width=7, height=2).grid(row=2, column=3)
button_add = tk.Button(root, text="+",width=7, height=2).grid(row=3, column=3)
button_equals = tk.Button(root, text="=",width=16, height=2, command=lambda: print(f.add(5,6))).grid(row=6, column=2, columnspan=2)
button_decimal = tk.Button(root, text=".",width=7, height=2).grid(row=6, column=1)

### Number buttons
button_zero = tk.Button(root, text="0",width=7, height=2).grid(row=6, column=0)
button_one = tk.Button(root, text="1",width=7, height=2).grid(row=5, column=0)
button_two = tk.Button(root, text="2",width=7, height=2).grid(row=5, column=1)
button_three = tk.Button(root, text="3",width=7, height=2).grid(row=5, column=2)
button_four = tk.Button(root, text="4",width=7, height=2).grid(row=4, column=0)
button_five = tk.Button(root, text="5",width=7, height=2).grid(row=4, column=1)
button_six = tk.Button(root, text="6",width=7, height=2).grid(row=4, column=2)
button_seven = tk.Button(root, text="7",width=7, height=2).grid(row=3, column=0)
button_eight = tk.Button(root, text="8",width=7, height=2).grid(row=3, column=1)
button_nine = tk.Button(root, text="9",width=7, height=2).grid(row=3, column=2)

root.mainloop()
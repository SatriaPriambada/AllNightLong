import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
from dependency.test import dep


def show_dataframe():
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["Jakarta", "Bandung", "Surabaya"],
    }
    df = pd.DataFrame(data)

    # Display the DataFrame in the text area
    output.delete(1.0, tk.END)
    output.insert(tk.END, df.to_string(index=False))


# GUI setup
root = tk.Tk()
root.title("Pandas Hello App")
root.geometry("400x300")

button = tk.Button(root, text="Show Data", command=show_dataframe)
button.pack(pady=10)

output = scrolledtext.ScrolledText(root, width=50, height=10)
output.pack(padx=10, pady=10)
dep()
root.mainloop()

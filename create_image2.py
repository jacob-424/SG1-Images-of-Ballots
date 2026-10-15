import tkinter as tk

root = tk.Tk()
root.withdraw()

# Create a 250 x 250 white image with no plus patterns
image = tk.PhotoImage(width=250, height=250)
image.put("white", to=(0, 0, 250, 250))

image.write("IMAGE2.PNG")

root.destroy()

print("Created IMAGE2.PNG with zero patterns.")
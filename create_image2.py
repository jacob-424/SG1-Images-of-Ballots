import tkinter as tk
import random

root = tk.Tk()
root.withdraw()

# Create a 250 x 250 white image
image = tk.PhotoImage(width=250, height=250)
image.put("white", to=(0, 0, 250, 250))

# -------------------------------------------------
# Add random black noise around the image
# -------------------------------------------------

random.seed(4500)

for i in range(700):
    x = random.randint(0, 249)
    y = random.randint(0, 249)

    # Keep the area around our real pattern untouched
    if not (90 <= x <= 110 and 90 <= y <= 110):
        image.put("black", to=(x, y))


# Add some random lines/shapes that are NOT valid patterns

# Horizontal line
for x in range(20, 60):
    image.put("black", to=(x, 40))

# Vertical line
for y in range(150, 200):
    image.put("black", to=(210, y))

# Small box
for x in range(30, 51):
    image.put("black", to=(x, 180))
    image.put("black", to=(x, 200))

for y in range(180, 201):
    image.put("black", to=(30, y))
    image.put("black", to=(50, y))


# -------------------------------------------------
# Add ONE exact valid 11 x 11 pattern
# Center = (100, 100)
# -------------------------------------------------

center_x = 100
center_y = 100

# Horizontal black line
for x in range(center_x - 5, center_x + 6):
    image.put("black", to=(x, center_y))

# Vertical black line
for y in range(center_y - 5, center_y + 6):
    image.put("black", to=(center_x, y))


# Save the test image
image.write("IMAGE2.PNG")

root.destroy()

print("Created complicated IMAGE2.PNG.")
print("Expected patterns: 1")
print("Expected center (row, column): (100, 100)")
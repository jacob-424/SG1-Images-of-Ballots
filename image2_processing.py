import tkinter as tk

	
def image2ToMatrix():
    # Load IMAGE2
    image = tk.PhotoImage(file="IMAGE2.PNG")

    width = image.width()
    height = image.height()

    zerosAndOnes = []

    # Go through every pixel in IMAGE2
    for row in range(height):
        currentRow = []

        for col in range(width):
            pixel = image.get(col, row)

            # Black pixel = 0, anything else = 1
            if pixel == (0, 0, 0):
                currentRow.append(0)
            else:
                currentRow.append(1)

        zerosAndOnes.append(currentRow)

    return zerosAndOnes


def searchForPattern(zerosAndOnes):
    # Exact 11X11 pattern required by the specification
    pattern = [
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
    ]

    coords = []

    rows = len(zerosAndOnes)
    cols = len(zerosAndOnes[0])

    # Try every possible location where an 11x11 pattern can fit
    for row in range(rows - 10):
        for col in range(cols - 10):

            match = True

            # Compare the 11x11 area with the required pattern
            for patternRow in range(11):
                for patternCol in range(11):
                    if zerosAndOnes[row + patternRow][col + patternCol] != pattern[patternRow][patternCol]:
                        match = False
                        break

                if not match:
                    break

            # Save the center of the pattern
            if match:
                coords.append((row + 5, col + 5))

    return coords